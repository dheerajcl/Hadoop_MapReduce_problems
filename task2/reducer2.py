#!/usr/bin/env python3
import sys

current_key = None
accu_values = []

for record in sys.stdin:
    key, value = record.strip().split('\t', 1)

    if key == current_key:
        accu_values.append(value)
    else:
        if current_key is not None:
            accu_values = sorted(accu_values, key=lambda x: int(x.split('r')[-1]))
            print(f"{current_key}\t{[item.split(' r')[0] for item in accu_values]}")
        current_key = key
        accu_values = [value]

if current_key is not None:
    accu_values = sorted(accu_values, key=lambda x: int(x.split('r')[-1]))
    print(f"{current_key}\t{[item.split(' r')[0] for item in accu_values]}")
