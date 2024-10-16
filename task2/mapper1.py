#!/usr/bin/env python3
import sys

for record in sys.stdin:
    str_record = record.strip()
    
    if not str_record:
        continue

    tokens = str_record.split(" ")

    print(tokens[0] + "\t", end="")
    rem_tokens = tokens[1:]

    for token in rem_tokens:
        print(token, end=" ")
    print()
