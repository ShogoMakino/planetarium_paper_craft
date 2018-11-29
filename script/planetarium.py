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
    {'name': 'n11', 'n': 6, 'circle': True, 'glue': [[1, 2], [2, 3], [3, 4]],
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
angle = {58: 7, 177: 6, 68: 6, 58: 4, 24: 4}

if __name__ == '__main__':
    pc = PaperCraft("planetarium.svg")
    pc.glue_width = 3
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
            pc.circle([0.0, 0.0], 4, fill='white', object_type='texture')
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
        pc.rect([0, 0], [5, 30], fill='lightgray')
        pc.rect([5, 0], [15, 30], fill='lightgray')
        pc.rect([15, 0], [20, 30], fill='lightgray')
        pc.translate([100 + i * 25, 50])
        pc.end_group()

        pc.begin_group("latitude_gearbox_plate" + str(i), svg_group=True)
        pc.polygon([[0, 0], [20, 0], [20, 30], [15, 30],
                    [15, 15], [5, 15], [5, 30], [0, 30]],
                   fill='lightgray', loop=True)
        pc.translate([150 + i * 25, 50])
        pc.end_group()

    pc.begin_group("latitude_motor", svg_group=True)
    pc.rect([0, 0], [6, -6], fill='black', stroke='darkgray')
    pc.rect([0, 0], [6, 10], fill='black', stroke='darkgray')
    pc.rect([6, 0], [12, 10], fill='black', stroke='darkgray')
    pc.rect([12, 0], [18, 10], fill='black', stroke='darkgray')
    pc.rect([18, 0], [24, 10], fill='black', stroke='darkgray')
    pc.glue(['rect0'], 0, 1, root='active')
    pc.glue(['rect0'], 1, 2, root='active')
    pc.glue(['rect0'], 3, 0, root='active')
    pc.glue(['rect1'], 3, 0, root='active')
    pc.translate([100, 30])
    pc.end_group()

    pc.draw()
