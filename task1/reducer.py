#!/usr/bin/env python3
import sys
import json

city_stats = {}

for line in sys.stdin:
    line = line.strip()
    if line:
        try:
            city, result = line.split("\t")
            if city not in city_stats:
                city_stats[city] = {"profit": 0, "loss": 0}
            
            if result == "profit":
                city_stats[city]["profit"] += 1
            else:
                city_stats[city]["loss"] += 1

        except ValueError:
            sys.stderr.write(f"Error splitting line: {line}\n")
        except Exception as e:
            sys.stderr.write(f"Processing error: {e}\n")

for city, counts in city_stats.items():
    output = {
        "city": city,
        "profit_stores": counts["profit"],
        "loss_stores": counts["loss"]
    }
    print(json.dumps(output))
