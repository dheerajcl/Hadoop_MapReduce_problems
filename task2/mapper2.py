#!/usr/bin/env python3
import sys

for entry in sys.stdin:

    key, raw_values = entry.strip().split("\t", 1)
    pro_values = raw_values[1:-1]
    split_values = pro_values.split(",")

    if len(split_values) < 2:
        continue

    det_info = split_values[1].strip()[1:-1].split(" ")
    print(det_info[2] + "\t", end="")
    del det_info[2]

    print(split_values[0] + " ", det_info, key)
