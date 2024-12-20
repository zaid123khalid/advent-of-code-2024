import time
from itertools import *
from collections import Counter


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split("\n")
    return lines


def find_regions(regions_map):
    dct = {}
    for y, i in enumerate(regions_map):
        for x, j in enumerate(i):
            try:
                dct[j].append((x, y))
            except:
                dct[j] = [(x, y)]
    return dct


def nearby_plots(plot):
    return [
        (plot[0] + 1, plot[1]),
        (plot[0] - 1, plot[1]),
        (plot[0], plot[1] + 1),
        (plot[0], plot[1] - 1),
    ]


def split_regions(region):
    regions = []
    while region:
        for i in region:
            seen = 0
            for j in regions:
                if i in j:
                    seen += 1
            if seen == 0:
                region_tmp = [i]
                nearby_plots_tmp = nearby_plots(i)
                added = True
                region_tmp_len = len(region_tmp)
                while added:
                    for j in region:
                        if j in nearby_plots_tmp:
                            region_tmp.append(j)
                            nearby_plots_tmp.extend(nearby_plots(j))
                            nearby_plots_tmp = list(set(nearby_plots_tmp))
                    region_tmp = list(set(region_tmp))
                    region_tmp.sort()
                    if len(region_tmp) > region_tmp_len:
                        region_tmp_len = len(region_tmp)
                    else:
                        added = False
                for i in region_tmp:
                    region.remove(i)
                regions.append(region_tmp)
    return regions


def calculate_perimeter(region):
    perimeter = 0
    for i in region:
        for j in nearby_plots(i):
            if j not in region:
                perimeter += 1
    return perimeter


regions_map = read_file("../input.txt")
regions = find_regions(regions_map)

separate_regions = []
for i in regions:
    new_regions = split_regions(regions[i])
    separate_regions.extend(new_regions)

result = 0
for i in separate_regions:
    perimeter = calculate_perimeter(i)
    result += len(i) * perimeter

print("1st part answer: " + str(result))
