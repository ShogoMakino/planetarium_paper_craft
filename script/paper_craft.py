#!/usr/bin/python3
# -*- coding: utf-8 -*-

import svgwrite
import numpy as np
import math

class PaperCraft:
    def __init__(self, filename,
                 stroke='black', fill='white', stroke_width=0.1,
                 glue_width=5, glue_angle=math.pi/3):
        self.dtype='f8'
        self.__dwg = svgwrite.Drawing(filename,
                                      size=('210mm', '297mm'),
                                      viewBox=('0 0 210 297'))
        self.__shapes = [{'type': 'group', 'name': 'root', 'child': [],
                          'draw': True, 'object_type': None}]

        self.stroke = stroke
        self.fill = fill
        self.stroke_width = stroke_width
        self.glue_width = glue_width
        self.glue_angle = glue_angle
        self.draw_order = ['glue', 'surface', 'texture']

    def begin_group(self, name=None, svg_group=False,
                    object_type='surface', **kwargs):
        name = (name if name is not None
                      else self.__generate_name('group'))
        object_type = object_type if svg_group else None
        elem = {'type': 'group', 'name': name, 'child': [],
                'draw': True, 'object_type': object_type}
        elem.update(kwargs)
        self.__shapes.append(elem)

    def end_group(self):
        last_group = self.__shapes.pop()
        self.__shapes[-1]['child'].append(last_group)

    def draw(self):
        for object_type in self.draw_order:
            self.__draw_target(self.__shapes[0], self.__dwg, {'object_type': object_type})
        self.__dwg.save()

    def translate(self, dx):
        self.__apply_group(self.__shapes[-1], self.__translate_sub, dx)

    def rotate(self, rad):
        self.__apply_group(self.__shapes[-1], self.__rotate_sub, rad)

    def adjust_points(self, move_object_name, move_index0, move_index1,
                     target_object_name, target_index0, target_index1):
        move_object = self.__get_object_by_name(move_object_name, root='active')
        target_object = self.__get_object_by_name(target_object_name, root='root')
        if move_object is None or target_object is None:
            print("Objects were not found.")
            return
        move_p0 = move_object['points'][move_index0]
        move_p1 = move_object['points'][move_index1]
        target_p0 = target_object['points'][target_index0]
        target_p1 = target_object['points'][target_index1]
        move_vector = move_p1 - move_p0
        move_midpoint = (move_p0 + move_p1) / 2.0
        target_vector = target_p1 - target_p0
        target_midpoint = (target_p0 + target_p1) / 2.0
        move_vector_theta = math.atan2(move_vector[1], move_vector[0])
        target_vector_theta = math.atan2(target_vector[1], target_vector[0])
        self.translate(-move_midpoint)
        self.rotate(target_vector_theta - move_vector_theta)
        self.translate(target_midpoint)

    def polygon(self, points, name=None, **kwargs):
        name = (name if name is not None
                      else self.__generate_name('polygon'))
        np_points = [np.array(l, dtype=self.dtype) for l in points]
        elem = {'type': 'path',
                'name': name,
                'points': np_points,
                'object_type': 'surface',
                'draw': True}
        elem.update(kwargs)
        self.__shapes[-1]['child'].append(elem)

    def rect(self, x1, x2, name=None, **kwargs):
        name = (name if name is not None
                      else self.__generate_name('rect'))
        p0 = [min(x1[0], x2[0]), min(x1[1], x2[1])]
        p1 = [max(x1[0], x2[0]), min(x1[1], x2[1])]
        p2 = [max(x1[0], x2[0]), max(x1[1], x2[1])]
        p3 = [min(x1[0], x2[0]), max(x1[1], x2[1])]
        points = [np.array(p0, dtype=self.dtype), np.array(p1, dtype=self.dtype),
                  np.array(p2, dtype=self.dtype), np.array(p3, dtype=self.dtype)]
        self.polygon(points, name=name, loop=True, **kwargs)

    def regular_polygon(self, n, name=None, skip=None,
                        side=None, circumscribe=None, inscribe=None,
                        **kwargs):
        name = (name if name is not None
                      else self.__generate_name('regular_polygon'))
        r = None
        if circumscribe is not None:
            r = circumscribe
        elif side is not None:
            r = side / math.sin(math.pi / n) / 2
        elif inscribe is not None:
            r = inscribe / math.cos(math.pi / n)
        if r is None:
            return
        points = []
        for i in range(n):
            theta = 2 * math.pi * i / n
            if skip is not None and i in skip:
                continue
            points.append(np.array([r * math.cos(theta), r * math.sin(theta)],
                                   dtype=self.dtype))
        self.polygon(points, name=name, loop=True, **kwargs)

    def circle(self, center, radius, name=None, **kwargs):
        name = (name if name is not None
                      else self.__generate_name('circle'))
        elem = {'type': 'circle',
                'name': name,
                'draw': True,
                'points': [np.array(center, dtype=self.dtype)],
                'radius': radius,
                'object_type': 'surface'}
        elem.update(kwargs)
        self.__shapes[-1]['child'].append(elem)

    def point(self, x, name=None, **kwargs):
        name = (name if name is not None
                      else self.__generate_name('point'))
        elem = {'type': 'point',
                'name': name,
                'points': [np.array(x, dtype=self.dtype)],
                'draw': False}
        elem.update(kwargs)
        self.__shapes[-1]['child'].append(elem)

    def glue(self, target_name, index0, index1, width=None,
             angle0=None, angle1=None, root='root', **kwargs):
        target = self.__get_object_by_name(target_name, root=root)
        if target is None:
            return
        angle0 = angle0 if angle0 is not None else self.glue_angle
        angle1 = angle1 if angle1 is not None else self.glue_angle
        width = width if width is not None else self.glue_width
        name = self.__generate_name('glue')
        p0 = target['points'][index0]
        p1 = target['points'][index1]
        vec01 = p1 - p0
        glue_min_length = width * (math.tan(math.pi / 2 - angle0)
                                   + math.tan(math.pi / 2 - angle1))
        vec01n = vec01 / np.linalg.norm(vec01)
        vec03n = np.dot(self.__rot_matrix(-angle0), vec01n)
        if np.linalg.norm(vec01) < glue_min_length:
            vec03 = vec03n * np.linalg.norm(vec01) / glue_min_length * width / math.sin(angle0)
            p3 = p0 + vec03
            points = [p0, p3, p1]
        else:
            vec12n = np.dot(self.__rot_matrix(angle1), -vec01n)
            vec03 = vec03n * width / math.sin(angle0)
            vec12 = vec12n * width / math.sin(angle1)
            p2 = p1 + vec12
            p3 = p0 + vec03
            points = [p0, p3, p2, p1]
        self.polygon(points, name=name, object_type='glue', **kwargs)

    def __get_object_by_name(self, name_list, root='root'):
        if root == 'root':
            target_object = self.__shapes[0]
            next_index = 1 if len(self.__shapes) >= 2 else None
        elif root == 'active':
            target_object = self.__shapes[-1]
            next_index = None
        else:
            print("root should be 'root' or 'active'")
            return

        filter_keys = ["name", "type", "child"]
        for name in name_list:
            if target_object['type'] == 'group':
                match_flag = False
                for i in range(len(target_object['child'])):
                    if target_object['child'][i]['name'] == name:
                        target_object = target_object['child'][i]
                        next_index = None
                        match_flag = True
                        break
                if match_flag:
                    continue
            if next_index is not None:
                if self.__shapes[next_index]['name'] == name:
                    target_object = self.__shapes[next_index]
                    next_index = (next_index + 1
                                  if next_index < len(self.__shapes) - 1 else None)
                    continue
            print("'" + name + "' was not found")
            return
        return target_object

    def __filter_by_key(self, target, filter_keys):
        ret_dict = {}
        for key in target.keys():
            if key in filter_keys and key in target:
                if type(target[key]) == dict:
                    ret_dict[key] = self.__filter_by_key(target[key], filter_keys)
                elif type(target[key]) == list:
                    ret_dict[key] = list(map(lambda x: self.__filter_by_key(x, filter_keys), target[key]))
                else:
                    ret_dict[key] = target[key]
        return ret_dict

    def __generate_name(self, prefix):
        existing_names = self.__shapes[-1].keys()
        i = 0
        while prefix + str(i) in existing_names:
            i += 1
        return prefix + str(i)

    def __apply_group(self, target, func, *args):
        if target['type'] == 'group':
            for i in target['child']:
                self.__apply_group(i, func, *args)
        else:
            func(target, *args)

    def __translate_sub(self, target, dx):
        for i in range(len(target['points'])):
            target['points'][i] += np.array(dx, dtype=self.dtype)

    def __rotate_sub(self, target, rad):
        rot_matrix = self.__rot_matrix(rad)
        for i in range(len(target['points'])):
            target['points'][i] = np.dot(rot_matrix, target['points'][i])

    def __rot_matrix(self, rad):
        return np.array([[math.cos(rad), -math.sin(rad)],
                         [math.sin(rad), math.cos(rad)]],
                        dtype=self.dtype)

    def __draw_target(self, target, dwg, draw_filter=None):
        if not target['draw']:
            return
        if target['type'] == 'group' and target['object_type'] is None:
            for child in target['child']:
                self.__draw_target(child, dwg, draw_filter)
        else:
            if not self.__check_filter(target, draw_filter):
                return
            if target['type'] == 'group':
                grp = dwg.add(self.__dwg.g(id=target['name']))
                for object_type in self.draw_order:
                    for child in target['child']:
                        self.__draw_target(child, grp, {'object_type': object_type})
            elif target['type'] == 'path':
                self.__draw_path(target, dwg)
            elif target['type'] == 'circle':
                self.__draw_circle(target, dwg)

    def __check_filter(self, target, filter_dict):
        for key in filter_dict.keys():
            if key not in target or target[key] != filter_dict[key]:
                return False
        return True

    def __draw_path(self, target, dwg):
        d = [(['M'] if i == 0 else['L']) + list(l)
             for i, l in enumerate(target['points'])]
        if 'loop' in target and target['loop']:
            d.append(['Z'])
        stroke, fill, stroke_width = self.__draw_style(target)
        dwg.add(self.__dwg.path(d, stroke=stroke, fill=fill,
                                stroke_width=stroke_width))

    def __draw_circle(self, target, dwg):
        stroke, fill, stroke_width = self.__draw_style(target)
        dwg.add(self.__dwg.circle(center=target['points'][0],
                                  r=target['radius'],
                                  stroke=stroke, fill=fill,
                                  stroke_width=stroke_width))

    def __draw_style(self, target):
        stroke = (target['stroke']
                  if ('stroke' in target
                      and target['stroke'] is not None)
                  else self.stroke)
        fill = (target['fill']
                if ('fill' in target
                    and target['fill'] is not None)
                else self.fill)
        stroke_width = (target['stroke_width']
                        if ('stroke_width' in target
                            and target['stroke_width'] is not None)
                        else self.stroke_width)
        return stroke, fill, stroke_width
