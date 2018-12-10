#!/usr/bin/python3
# -*- coding: utf-8 -*-

from paper_craft import PaperCraft
import numpy as np
import math

shiitake_config = [
    {'name': 'n0', 'n': 5, 'circle': True, 'adjust': None, 'glue': None},
    {'name': 'n1', 'n': 6, 'circle': True, 'glue': [[1, 2]],
     'adjust': {'target': 'n0', 'target_index': [1, 0], 'move_index': [0, 1]}},
    {'name': 'n2', 'n': 6, 'circle': True, 'glue': [[1, 2]],
     'adjust': {'target': 'n0', 'target_index': [2, 1], 'move_index': [0, 1]}},
    {'name': 'n3', 'n': 6, 'circle': True, 'glue': [[1, 2]],
     'adjust': {'target': 'n0', 'target_index': [3, 2], 'move_index': [0, 1]}},
    {'name': 'n4', 'n': 6, 'circle': True, 'glue': [[1, 2]],
     'adjust': {'target': 'n0', 'target_index': [4, 3], 'move_index': [0, 1]}},
    {'name': 'n5', 'n': 6, 'circle': True, 'glue': [[1, 2]],
     'adjust': {'target': 'n0', 'target_index': [0, 4], 'move_index': [0, 1]}},
    {'name': 'n6', 'n': 5, 'circle': True, 'glue': [[1, 2]],
     'adjust': {'target': 'n1', 'target_index': [3, 2], 'move_index': [0, 1]}},
    {'name': 'n7', 'n': 5, 'circle': True, 'glue': [[1, 2]],
     'adjust': {'target': 'n2', 'target_index': [3, 2], 'move_index': [0, 1]}},
    {'name': 'n8', 'n': 5, 'circle': True, 'glue': [[1, 2]],
     'adjust': {'target': 'n3', 'target_index': [3, 2], 'move_index': [0, 1]}},
    {'name': 'n9', 'n': 5, 'circle': True, 'glue': [[1, 2]],
     'adjust': {'target': 'n4', 'target_index': [3, 2], 'move_index': [0, 1]}},
    {'name': 'n10', 'n': 5, 'circle': True, 'glue': [[1, 2]],
     'adjust': {'target': 'n5', 'target_index': [3, 2], 'move_index': [0, 1]}},
    {'name': 'n11', 'n': 6, 'circle': True, 'glue': [[1, 2], [2, 3], [3, 4], [4, 5]],
     'adjust': {'target': 'n6', 'target_index': [3, 2], 'move_index': [0, 1]}},
    {'name': 'n12', 'n': 6, 'circle': True, 'glue': [[1, 2], [2, 3], [3, 4], [4, 5]],
     'adjust': {'target': 'n7', 'target_index': [3, 2], 'move_index': [0, 1]}},
    {'name': 'n13', 'n': 6, 'circle': True, 'glue': [[1, 2], [2, 3], [3, 4], [4, 5]],
     'adjust': {'target': 'n8', 'target_index': [3, 2], 'move_index': [0, 1]}},
    {'name': 'n14', 'n': 6, 'circle': True, 'glue': [[1, 2], [2, 3], [3, 4], [4, 5]],
     'adjust': {'target': 'n9', 'target_index': [3, 2], 'move_index': [0, 1]}},
    {'name': 'n15', 'n': 6, 'circle': True, 'glue': [[1, 2], [2, 3], [3, 4], [4, 5]],
     'adjust': {'target': 'n10', 'target_index': [3, 2], 'move_index': [0, 1]}},
    {'name': 'n16', 'n': 6, 'circle': False, 'skip': [3, 4], 'glue': [[1, 2], [2, 3]],
     'adjust': {'target': 'n6', 'target_index': [4, 3], 'move_index': [0, 1]}},
    {'name': 'n17', 'n': 6, 'circle': False, 'skip': [3, 4], 'glue': [[1, 2], [2, 3]],
     'adjust': {'target': 'n7', 'target_index': [4, 3], 'move_index': [0, 1]}},
    {'name': 'n18', 'n': 6, 'circle': False, 'skip': [3, 4], 'glue': [[1, 2], [2, 3]],
     'adjust': {'target': 'n8', 'target_index': [4, 3], 'move_index': [0, 1]}},
    {'name': 'n19', 'n': 6, 'circle': False, 'skip': [3, 4], 'glue': [[1, 2], [2, 3]],
     'adjust': {'target': 'n9', 'target_index': [4, 3], 'move_index': [0, 1]}},
    {'name': 'n20', 'n': 6, 'circle': False, 'skip': [3, 4], 'glue': [[1, 2], [2, 3]],
     'adjust': {'target': 'n10', 'target_index': [4, 3], 'move_index': [0, 1]}}
]

pipe = {168: 2, 160: 3, 140: 2}
angle = {58: 11, 177: 6, 68: 6, 24: 4}

if __name__ == '__main__':
    pc = PaperCraft("planetarium.svg")
    pc.glue_width = 2
    pc.glue_angle = math.pi / 4
    pc.begin_group("shiitake", svg_group=True)
    for elem in shiitake_config:
        pc.begin_group(elem['name'])
        skip = elem['skip'] if 'skip' in elem else None
        pc.regular_polygon(elem['n'], name='surface',
                           side=10, skip=skip, fill='lightgray')
        if elem['glue']:
            for glue in elem['glue']:
                pc.glue(['surface'], *glue, root='active')
        if elem['circle']:
            pc.circle([0.0, 0.0], 4.5, fill='white', object_type='texture')
        if elem['adjust'] is not None:
            pc.adjust_points(['surface'],
                             elem['adjust']['move_index'][0],
                             elem['adjust']['move_index'][1],
                             ['shiitake', elem['adjust']['target'], 'surface'],
                             elem['adjust']['target_index'][0],
                             elem['adjust']['target_index'][1])
        pc.end_group()
    pc.translate([50, 50])
    pc.end_group()

    x = 0
    for key in pipe.keys():
        for i in range(pipe[key]):
            pc.begin_group('pipe_' + str(key) + '_' + str(i), svg_group=True)
            pc.rect([0, 0], [4, key], fill='black', stroke='darkgray')
            pc.rect([4, 0], [8, key], fill='black', stroke='darkgray')
            pc.rect([8, 0], [12, key], fill='black', stroke='darkgray')
            pc.rect([12, 0], [16, key], fill='black', stroke='darkgray')
            pc.glue(['rect0'], 3, 0, root='active')
            pc.translate([x, 110])
            pc.end_group()
            x += 25

    for key in angle.keys():
        for i in range(angle[key]):
            pc.begin_group('angle_' + str(key) + '_' + str(i), svg_group=True)
            pc.rect([0, 0], [4, key], fill='black', stroke='darkgray')
            pc.rect([4, 0], [8, key], fill='black', stroke='darkgray')
            pc.rect([8, 0], [12, key], fill='black', stroke='darkgray')
            pc.rect([12, 0], [16, key], fill='black', stroke='darkgray')
            pc.translate([x, 110])
            pc.end_group()
            x += 25

    for i in range(8):
        pc.begin_group("plate" + str(i), svg_group=True)
        pc.polygon([[0, 0], [12, 0], [0, 12]], loop=True, fill='lightgray')
        pc.polygon([[0, 0], [0, -12], [12, 0]], loop=True, fill='lightgray')
        pc.circle([2, 2], 0.3, object_type='texture', fill='none')
        pc.circle([2, 6], 0.3, object_type='texture', fill='none')
        pc.circle([2, 8], 0.3, object_type='texture', fill='none')
        pc.circle([8, 2], 0.3, object_type='texture', fill='none')
        pc.circle([2, -2], 0.3, object_type='texture', fill='none')
        pc.circle([2, -6], 0.3, object_type='texture', fill='none')
        pc.circle([2, -8], 0.3, object_type='texture', fill='none')
        pc.circle([8, -2], 0.3, object_type='texture', fill='none')
        pc.translate([100 + i * 20, 15])
        pc.end_group()

    for i in range(2):
        pc.begin_group("latitude_gearbox_channel" + str(i), svg_group=True)
        pc.rect([0, 0], [5, 35], fill='lightgray')
        pc.rect([5, 0], [15, 35], fill='lightgray')
        pc.rect([15, 0], [20, 35], fill='lightgray')
        pc.rect([20, 0], [25, 35], fill='lightgray')
        pc.rect([25, 0], [35, 35], fill='lightgray')
        pc.rect([35, 0], [40, 35], fill='lightgray')

        pc.begin_group("final_bearing_unit" + str(i))
        pc.rect([-1, -3.5], [1, 3.5], stroke='none', fill='gray', object_type='texture')
        pc.circle([0, 3.5], 1, stroke='none', fill='gray', object_type='texture')
        pc.circle([0, -3.5], 1, stroke='none', fill='gray', object_type='texture')
        pc.circle([0, 3.5], 0.3, fill='none', object_type='texture')
        pc.circle([0, -3.5], 0.3, fill='none', object_type='texture')
        pc.circle([0, 0], 2.75, stroke='none', fill='gray', object_type='texture')
        pc.circle([0, 0], 2, stroke='none', fill='black', object_type='texture')
        pc.circle([0, 0], 1, fill='white', object_type='texture')
        pc.circle([20, 0], 1, fill='white', object_type='texture')
        pc.translate([10, 30])
        pc.end_group()

        small_bearing_pos = [[10, 15], [10, 20]]
        for j in range(2):
            pc.begin_group("small_bearing_unit" + str(i) + "_" + str(j))
            pc.rect([-2.25, -0.75], [2.25, 0.75], stroke='none', fill='gray', object_type='texture')
            pc.circle([2.25, 0], 0.75, stroke='none', fill='gray', object_type='texture')
            pc.circle([-2.25, 0], 0.75, stroke='none', fill='gray', object_type='texture')
            pc.circle([2.25, 0], 0.3, fill='none', object_type='texture')
            pc.circle([-2.25, 0], 0.3, fill='none', object_type='texture')
            pc.circle([0, 0], 1.8, stroke='none', fill='gray', object_type='texture')
            pc.circle([0, 0], 1.2, stroke='none', fill='black', object_type='texture')
            pc.circle([0, 0], 0.5, fill='gray', object_type='texture')
            pc.circle([20, 0], 0.5, fill='gray', object_type='texture')
            pc.translate(small_bearing_pos[j])
            pc.end_group()
        pc.translate([100 + i * 50, 30])
        pc.end_group()

        pc.begin_group("latitude_gearbox_plate" + str(i), svg_group=True)
        pc.rect([0, 0], [20, 24], fill='lightgray')
        pc.begin_group("small_bearing_unit" + str(i))
        pc.rect([-2.25, -0.75], [2.25, 0.75], stroke='none', fill='gray', object_type='texture')
        pc.circle([2.25, 0], 0.75, stroke='none', fill='gray', object_type='texture')
        pc.circle([-2.25, 0], 0.75, stroke='none', fill='gray', object_type='texture')
        pc.circle([2.25, 0], 0.3, fill='none', object_type='texture')
        pc.circle([-2.25, 0], 0.3, fill='none', object_type='texture')
        pc.circle([0, 0], 1.8, stroke='none', fill='gray', object_type='texture')
        pc.circle([0, 0], 1.2, stroke='none', fill='black', object_type='texture')
        pc.circle([0, 0], 0.5, fill='gray', object_type='texture')
        pc.translate([10, 10])
        pc.end_group()
        pc.translate([100 + i * 50, 70])
        pc.end_group()

        for j in range(2):
            pc.begin_group("latitude_bearing" + str(i) + "_" + str(j), svg_group=True)
            pc.rect([-2.5, 0], [2.5, 2.5], fill='black', stroke='darkgray')
            pc.circle([0, 2.5], 2.5, fill='lightgray')
            pc.circle([0, 2.5], 2.2, fill='black', object_type='texture', stroke='none')
            pc.circle([0, 2.5], 1.5, fill='darkgray', object_type='texture', stroke='none')
            pc.circle([0, 2.5], 1, fill='white', object_type='texture')
            pc.glue(['rect0'], 0, 1, width=2, root='active')
            pc.translate([30, 250])
            pc.end_group()

        pc.begin_group("latitude_bearing_side" + str(i), svg_group=True)
        pc.rect([-(1.25 * math.pi + 2.5), -1.6], [1.25 * math.pi + 2.5, 1.6], fill='lightgray')
        pc.glue(['rect0'], 0, 1, root='active', max_length=1.5, angle0=math.pi/3, angle1=math.pi/3)
        pc.glue(['rect0'], 2, 3, root='active', max_length=1.5, angle0=math.pi/3, angle1=math.pi/3)
        pc.begin_group()
        pc.rect([0, -1.6], [2.5, 1.6], fill='lightgray')
        pc.circle([1.3, 0], 0.3, fill='lightgray', object_type='texture')
        pc.adjust_points(['rect0'], 0, 3, ['latitude_bearing_side' + str(i), 'rect0'], 1, 2)
        pc.end_group()
        pc.begin_group()
        pc.rect([0, -1.6], [2.5, 1.6], fill='lightgray')
        pc.circle([1.3, 0], 0.3, fill='lightgray', object_type='texture')
        pc.adjust_points(['rect0'], 0, 3, ['latitude_bearing_side' + str(i), 'rect0'], 3, 0)
        pc.end_group()
        pc.end_group()

    for i in range(2):
        pc.begin_group("latitude_final_gear" + str(i), svg_group=True)
        pc.circle([0, 0], 8.25, fill='brown')
        pc.circle([0, 0], 1, fill='white', object_type='texture')
        pc.end_group()
    pc.begin_group("latitude_final_gear_side", svg_group=True)
    pc.rect([0, 0], [16.5 * math.pi, 2], fill='brown')
    for i in range(64):
        pc.polygon([[16.5 * math.pi / 64 * i, 0], [16.5 * math.pi / 64 * i, 2]], fill='none', object_type='texture')
    pc.glue(['rect0'], 0, 1, max_length=2, root='active', angle0=math.pi/3, angle1=math.pi/3)
    pc.glue(['rect0'], 2, 3, max_length=2, root='active', angle0=math.pi/3, angle1=math.pi/3)
    pc.glue(['rect0'], 1, 2, root='active', angle0=math.pi/2, angle1=math.pi/2, width=2)
    pc.end_group()


    for i in range(2):
        pc.begin_group("nisshu_final_gear" + str(i), svg_group=True)
        pc.circle([0, 0], 10.2, fill='dimgray')
        pc.circle([0, 0], 8, fill='white', object_type='texture')
        pc.translate([30 + 30 * i, 30])
        pc.end_group()

    pc.begin_group("nisshu_final_gear_side", svg_group=True)
    pc.rect([0, 0], [20.4 * math.pi, 1.5], fill='dimgray')
    for i in range(100):
        pc.polygon([[20.4 * math.pi / 100 * i, 0], [20.4 * math.pi / 100 * i, 1.5]], fill='none', object_type='texture')
    pc.glue(['rect0'], 0, 1, max_length=2, root='active', angle0=math.pi/3, angle1=math.pi/3)
    pc.glue(['rect0'], 2, 3, max_length=2, root='active', angle0=math.pi/3, angle1=math.pi/3)
    pc.glue(['rect0'], 1, 2, root='active', angle0=math.pi/2, angle1=math.pi/2, width=2)
    pc.end_group()

    pc.begin_group("nisshu_gearbox", svg_group=True)
    for i in range(2):
        pc.begin_group()
        pc.polygon([[0, 0], [9, 0], [16, 13.5], [16, 16.5], [9, 30], [0, 30], [7, 16.5], [7, 13.5]], loop=True, fill='black', stroke='darkgray')
        pc.rect([0, 30], [9, 39], fill='black', stroke='darkgray')
        pc.translate([0, 39 * i])
        pc.end_group()
    pc.glue(['group0', 'polygon0'], 0, 1, root='active')
    pc.end_group()

    for i in range(2):
        sign = 1 if i == 0 else -1
        pc.begin_group("nisshu_gearbox_plate" + str(i), svg_group=True)
        pc.polygon([[0, 0], [sign * 10, 0], [sign * 17, 13.5], [sign * 7, 13.5]], loop=True, fill='black', stroke='darkgray')
        pc.translate([10 + i * 30, 100])
        pc.end_group()

        pc.begin_group("nisshu_gearbox_support_pipe" + str(i), svg_group=True)
        for j in range(4):
            pc.rect([j * 3, 0], [(j + 1) * 3, 8], fill='black', stroke='darkgray')
        pc.glue(['rect0'], 3, 0, root='active', width=2)
        pc.end_group()

    pc.begin_group("nisshu_motor_mount", svg_group=True)
    pc.rect([0, 0], [9, 2], fill='black', stroke='darkgray')
    pc.rect([0, 2], [9, 11], fill='black', stroke='darkgray')
    pc.rect([0, 11], [9, 13], fill='black', stroke='darkgray')
    pc.rect([1.5, 3.5], [7.5, 9.5], fill='white', object_type='texture')
    pc.end_group()

    for i in range(2):
        pc.begin_group("motor" + str(i), svg_group=True)
        pc.rect([0, 0], [6, -6], fill='lightgray', stroke='black')
        pc.circle([3, -3], 2.5, fill='darkgray', stroke='none', object_type='texture')
        for j in range(4):
            pc.begin_group("side_surface" + str(j))
            pc.rect([j * 6, 0], [(j + 1) * 6, 10], fill='black', stroke='darkgray')
            pc.rect([j * 6, 0], [(j + 1) * 6, 1], fill='lightgray', stroke='none')
            pc.rect([j * 6, 9.5], [(j + 1) * 6, 10], fill='lightgray', stroke='none')
            pc.end_group()
            pc.glue(['side_surface' + str(j), 'rect0'], 2, 3, root='active')
        pc.glue(['rect0'], 0, 1, root='active')
        pc.glue(['rect0'], 1, 2, root='active')
        pc.glue(['rect0'], 3, 0, root='active')
        pc.glue(['side_surface0', 'rect0'], 3, 0, root='active')
        pc.translate([100, 80])
        pc.end_group()

    pc.begin_group("shiitake_base_polygon", svg_group=True)
    pentagon_side = math.sqrt(10**2 + 20**2 + 2 * 10 * 20 * math.cos(math.pi / 5))
    r = pentagon_side / 2.0 / math.sin(math.pi / 5)
    half_angle = math.asin(10 / r)
    vertex_list = []
    for i in range(5):
        vertex_list.append(np.array([r * math.cos(i * 2 * math.pi / 5 - half_angle),
                                     r * math.sin(i * 2 * math.pi / 5 - half_angle)]))
        vertex_list.append(np.array([r * math.cos(i * 2 * math.pi / 5 + half_angle),
                                     r * math.sin(i * 2 * math.pi / 5 + half_angle)]))
    pc.polygon(vertex_list, fill='lightgray', loop=True)
    pc.rect([-21.5, -6], [21.5, -4], fill='white', object_type='texture')
    pc.rect([-21.5, 6], [21.5, 4], fill='white', object_type='texture')
    pc.rect([6, -21.5], [4, 21.5], fill='white', object_type='texture')
    pc.rect([-6, -21.5], [-4, 21.5], fill='white', object_type='texture')
    pc.circle([0, 0], 20, fill='white', object_type='texture')
    pc.translate([170, 120])
    pc.end_group()

    pc.begin_group("kago_outer_plate_top", svg_group=True)
    for i in range(4):
        pc.begin_group()
        pc.rect([-8, -21.5], [8, -19], fill='lightgray')
        pc.rotate(i * math.pi / 2)
        pc.end_group()
    for i in range(4):
        pc.begin_group()
        pc.rect([-10, -22], [10, -18], fill='lightgray')
        pc.rotate(i * math.pi / 2 + math.pi / 4)
        pc.end_group()
    pc.translate([150, 270])
    pc.end_group()

    pc.begin_group("kago_outer_plate_back", svg_group=True)
    for i in range(4):
        pc.begin_group()
        pc.rect([-10, -22], [10, -18], fill='lightgray')
        pc.rotate(i * math.pi / 2 + math.pi / 4)
        pc.end_group()
    for i in range(4):
        pc.begin_group()
        pc.rect([-8, -21.5], [8, -19], fill='lightgray')
        pc.rotate(i * math.pi / 2)
        pc.end_group()
    pc.translate([100, 270])
    pc.end_group()


    for i in range(4):
        pc.begin_group("shiitake_base_bar" + str(i), svg_group=True)
        pc.rect([0, -21.5], [2, 21.5], fill='lightgray')
        pc.rect([0, -21.5], [-2, 21.5], fill='lightgray')
        pc.rect([0, -6], [2, -10], fill='white', object_type='texture')
        pc.rect([0, 6], [2, 10], fill='white', object_type='texture')
        sign = -1 if i % 2 else 1
        pc.rect([0, -4], [sign * 2, -6], fill='white', object_type='texture')
        pc.rect([0, 4], [sign * 2, 6], fill='white', object_type='texture')
        pc.translate([170 + i * 6, 200])
        pc.end_group()

        pc.begin_group("kago_base_angle" + str(i), svg_group=True)
        pc.rect([0, -21.5], [2, 21.5], fill='lightgray')
        pc.rect([2, -21.5], [4, 21.5], fill='lightgray')
        pc.rect([0, -21.5], [-2, 21.5], fill='lightgray')
        pc.rect([-2, -21.5], [-4, 21.5], fill='lightgray')
        pc.rect([-4, -4], [-2, -6], fill='white', object_type='texture')
        pc.rect([-4, 4], [-2, 6], fill='white', object_type='texture')
        pc.translate([170 + i * 10, 250])
        pc.end_group()

        pc.begin_group("kago_angle" + str(i), svg_group=True)
        pc.rect([0, 0], [2, 18], fill='lightgray')
        pc.rect([2, 0], [4, 18], fill='lightgray')
        pc.rect([0, 0], [-2, 18], fill='lightgray')
        pc.rect([-2, 0], [-4, 18], fill='lightgray')
        pc.rect([0, 0], [-2, -4], fill='lightgray')
        pc.rect([0, 0], [2, -4], fill='lightgray')
        pc.translate([10 + i * 10, 100])
        pc.end_group()

    for i in range(2):
        pc.begin_group("kago_channel" + str(i), svg_group=True)
        pc.polygon([[-6, -6], [-4.3, -6], [6, 4.3], [6, 6], [4.3, 6], [-6, -4.3]],
                   fill='lightgray', loop=True)
        pc.begin_group("side_plate0")
        pc.rect([-7, 0], [7, 2.5], fill='lightgray')
        pc.adjust_points(['rect0'], 0, 1,
                         ['kago_channel' + str(i), 'polygon0'], 2, 1)
        pc.end_group()
        pc.begin_group("side_plate1")
        pc.rect([-7, 0], [7, 2.5], fill='lightgray')
        pc.adjust_points(['rect0'], 0, 1,
                         ['kago_channel' + str(i), 'polygon0'], 5, 4)
        pc.end_group()
        pc.circle([-3.75, -3.75], 0.7, fill='white', object_type='texture')
        pc.circle([3.75, 3.75], 0.7, fill='white', object_type='texture')
        pc.translate([50 + 20 * i, 150])
        pc.end_group()

    pc.begin_group("kago_base_connector", svg_group=True)
    pc.rect([-6, -6], [6, 6], fill='lightgray')
    for i in range(4):
        pc.begin_group()
        pc.rect([-6, 6], [6, 8], fill='lightgray')
        pc.rotate(i * math.pi / 2)
        pc.end_group()
    pc.rect([-4, -4], [4, 4], fill='white', object_type='texture')
    pc.end_group()

    for i in range(4):
        pc.begin_group("zungiri" + str(i), svg_group=True)
        pc.rect([0, 0], [5, 36], fill='darkgray')
        for j in np.arange(0, 36, 0.2):
            pc.polygon([[0, j], [5, j]], fill='none', object_type='texture')
        pc.translate([150 + i * 10, 150])
        pc.end_group()


    for i in range(2):
        pc.begin_group("nisshu_center_pipe" + str(i), svg_group=True)
        pc.rect([0, 0], [3, 50], fill='darkslategray')
        pc.rect([3, 0], [6, 50], fill='darkslategray')
        pc.rect([6, 0], [9, 50], fill='darkslategray')
        pc.rect([9, 0], [12, 50], fill='darkslategray')
        pc.glue(['rect0'], 3, 0, root='active', width=2)
        pc.translate([10 + i * 20, 10])
        pc.end_group()

        pc.begin_group("nisshu_square_pipe" + str(i), svg_group=True)
        pc.rect([0, 0], [3, 30], fill='darkslategray')
        pc.rect([3, 0], [6, 30], fill='darkslategray')
        pc.rect([6, 0], [9, 30], fill='darkslategray')
        pc.rect([9, 0], [12, 30], fill='darkslategray')
        pc.glue(['rect0'], 3, 0, root='active', width=2)
        pc.translate([120 + i * 20, 10])
        pc.end_group()

        pc.begin_group("nisshu_channel" + str(i), svg_group=True)
        pc.rect([0, 0], [3, 116], fill='darkslategray')
        pc.rect([3, 0], [6, 116], fill='darkslategray')
        pc.rect([6, 0], [9, 116], fill='darkslategray')
        pc.translate([230 + i * 20, 10])
        pc.end_group()


    for i in range(8):
        pc.begin_group("nisshu_slant_pipe" + str(i), svg_group=True)
        pc.polygon([[0, 0], [3, 1.2], [3, 14.4 + 1.2], [0, 14.4]], loop=True, fill='darkslategray')
        pc.rect([3, 1.2], [6, 14.4 + 1.2], fill='darkslategray')
        pc.polygon([[6, 1.2], [9, 0], [9, 14.4], [6, 14.4 + 1.2]], loop=True, fill='darkslategray')
        pc.rect([9, 0], [12, 14.4], fill='darkslategray')
        pc.glue(['polygon0'], 3, 0, root='active', width=2)
        pc.translate([10 + i * 20, 60])
        pc.end_group()


        pc.begin_group("nisshu_axis_mount_pipe" + str(i), svg_group=True)
        for j in range(4):
            pc.rect([j * 3, 0], [(j + 1) * 3, 24], fill='black', stroke='darkgray')
            pc.glue(['rect' + str(j)], 0, 1, root='active')
        pc.glue(['rect0'], 3, 0, root='active', width=2)
        pc.translate([120 + i * 20, 60])
        pc.end_group()

    for i in range(2):
        pc.begin_group("nisshu_turntable_inner" + str(i), svg_group=True)
        pc.circle([0, 0], 9, fill='black', stroke='lightgray')
        pc.circle([0, 0], 2, fill='white', object_type='texture')
        for j in range(4):
            pc.begin_group()
            pc.circle([3.75, 3.75], 0.7, fill='white', object_type='texture')
            pc.rotate(j * math.pi / 2)
            pc.end_group()
        pc.end_group()

        pc.begin_group("nisshu_turntable_outer" + str(i), svg_group=True)
        pc.circle([0, 0], 12, fill='lightgray')
        pc.circle([0, 0], 8, fill='white')
        pc.end_group()

        pc.begin_group("nisshu_turntable_axis_outer" + str(i), svg_group=True)
        pc.rect([0, 0], [math.pi * 16, 1.5])
        pc.glue(['rect0'], 0, 1, root='active', max_length=1.5)
        pc.end_group()


        pc.begin_group("nisshu_slip_ring" + str(i), svg_group=True)
        pc.circle([0, 0], 13, fill='white', stroke='lightgray')
        pc.circle([0, 0], 11.5, fill='black', stroke='none', object_type='texture')
        pc.circle([0, 0], 8, fill='white', stroke='none', object_type='texture')
        pc.circle([0, 0], 2, fill='white', object_type='texture')
        for j in range(4):
            pc.begin_group()
            pc.circle([3.75, 3.75], 0.7, fill='white', object_type='texture')
            pc.rotate(j * math.pi / 2)
            pc.end_group()
        pc.end_group()


    pc.begin_group("nisshu_turntable_axis_inner", svg_group=True)
    pc.rect([0, 0], [math.pi * 16, 6])
    pc.glue(['rect0'], 0, 1, root='active', max_length=1.5)
    pc.glue(['rect0'], 2, 3, root='active', max_length=1.5)
    pc.end_group()

    for i in range(4):
        pc.begin_group("nisshu_spacer" + str(i), svg_group=True)
        for j in range(3):
            pc.rect([j * 1.5, 0], [(j + 1) * 1.5, 3], fill='gray')
            pc.glue(['rect' + str(j)], 2, 3, root='active')
        pc.glue(['rect0'], 3, 0, root='active', width=1.5)
        pc.translate([150 + i * 10 , 100])
        pc.end_group()

        pc.begin_group("nisshu_center_connect_plate" + str(i), svg_group=True)
        pc.polygon([[0, -3], [3, -3], [7, -1.5], [7, 1.5], [3, 3], [0, 3]], fill='darkslategray', loop=True)
        pc.end_group()

        pc.begin_group("nisshu_side_connect_plate" + str(i), svg_group=True)
        pc.polygon([[0, -1.5], [1.3, -5], [10, -5], [10, 5], [1.3, 5], [0, 1.5]], fill='darkslategray', loop=True)
        pc.end_group()

    pc.begin_group("latitude_axis0", svg_group=True)
    pc.rect([0, 0], [2 * math.pi, 60], fill='dimgray')
    for i in range(1, 60):
        pc.rect([0, i - 0.25], [2 * math.pi, i + 0.25], fill='none', stroke='black', object_type='texture')
    pc.glue(['rect0'], 3, 0, root='active', width=2)
    pc.end_group()

    pc.begin_group("latitude_axis1", svg_group=True)
    pc.rect([0, 0], [2 * math.pi, 73], fill='dimgray')
    for i in range(1, 73):
        pc.rect([0, i - 0.25], [2 * math.pi, i + 0.25], fill='none', stroke='black', object_type='texture')
    pc.glue(['rect0'], 3, 0, root='active', width=2)
    pc.end_group()

    #fixedstar_projector
    for i in range(32):
        pc.begin_group("fixedstar_side" + str(i), svg_group=True)
        pc.rect([0, 0], [8 * math.pi, 16.3], fill='lightgray')
        pc.glue(['rect0'], 3, 0, root='active')
        for j in range(10):
            pc.polygon([[0, 3 + j * 0.5], [8 * math.pi, 3 + j * 0.5]], fill='none', stroke='gray', object_type='texture')
        pc.polygon([[0, 11.3], [8 * math.pi, 11.3]], fill='none', stroke='gray', object_type='texture')
        pc.glue(['rect0'], 0, 1, max_length=2, angle0=math.pi/3, angle1=math.pi/3, root='active')
        pc.glue(['rect0'], 2, 3, max_length=2, angle0=math.pi/3, angle1=math.pi/3, root='active')
        pc.translate([10 + i * 30, 150])
        pc.end_group()

        pc.begin_group("fixedstar_top" + str(i), svg_group=True)
        pc.circle([0, 0], 4, fill='lightgray')
        pc.circle([0, 0], 1.75, fill='black', object_type='texture', stroke='white')
        pc.translate([10 + i * 10, 220])
        pc.end_group()

        pc.begin_group("fixedstar_bottom" + str(i), svg_group=True)
        pc.circle([0, 0], 4, fill='lightgray')
        pc.translate([10 + i * 10, 230])
        pc.end_group()

        for j in range(3):
            pc.begin_group("fixedstar_mount" + str(i) + "_" + str(j), svg_group=True)
            for k in range(3):
                pc.rect([k * 1.5, 0], [(k + 1) * 1.5, 5], fill='lightgray')
                pc.glue(['rect' + str(k)], 2, 3, root='active', angle0=math.pi/3, angle1=math.pi/3)
            pc.glue(['rect0'], 3, 0, root='active', width=1)
            pc.translate([10 + (i * 3 + j) * 6, 250])
            pc.end_group()

        pc.begin_group("triangle_plate" + str(i), svg_group=True)
        pc.regular_polygon(3, side=10, fill='lightgray')
        for j in range(3):
            pc.begin_group()
            pc.rect([2, -0.75], [6, 0.75], fill='lightgray')
            pc.rect([6, -0.75], [10, 0.75], fill='lightgray')
            pc.begin_group("hoseband")
            pc.rect([-0.5, -2.75],[0.5, 2.75], fill='darkgray')
            pc.polygon([[-0.5, -2.75], [-0.75, -3.75], [0.75, -3.75], [0.5, -2.75]], fill='orange', loop=True)
            pc.polygon([[-0.5, 2.75], [-0.75, 3.75], [0.75, 3.75], [0.5, 2.75]], fill='orange')
            pc.translate([7.5, 0])
            pc.end_group()
            pc.rotate(j * 2 * math.pi / 3)
            pc.end_group()
        pc.translate([10 + i * 20, 200])
        pc.end_group()

    pc.draw()
