#!/usr/bin/env python3
import sys

active_key = None
collected_values = []

for record in sys.stdin:
    key, value = record.strip().split('\t', 1)

    if key == active_key:
        collected_values.append(value)
    else:
        if active_key is not None:
            print(f"{active_key}\t{sorted(collected_values)}")
        active_key = key
        collected_values = [value]

if active_key is not None:
    print(f"{active_key}\t{sorted(collected_values)}")
