#!/usr/bin/env python3
import sys

previous_client = None
request_count = 0
successful_predictions = 0
total_cost = 0

for record in sys.stdin:
    client, raw_info = record.strip().split("\t")
    prediction_status, cost, key = raw_info.split(" ")

    prediction_success = 1 if prediction_status[0] == 'T' else 0
    cost_value = int(cost)

    if previous_client is None:
        previous_client = client

    if client != previous_client:
        print(f'{previous_client} {successful_predictions}/{request_count} {total_cost}')
        previous_client = client
        request_count = 0
        successful_predictions = 0
        total_cost = 0

    request_count += 1
    successful_predictions += prediction_success
    total_cost += cost_value

if previous_client is not None:
    print(f'{previous_client} {successful_predictions}/{request_count} {total_cost}')
