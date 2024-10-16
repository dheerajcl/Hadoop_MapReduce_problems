#!/usr/bin/env python3
import sys

endpoint_prices = {
    'user/profile': 100,
    'user/settings': 200,
    'order/history': 300,
    'order/checkout': 400,
    'product/details': 500,
    'product/search': 600,
    'cart/add': 700,
    'cart/remove': 800,
    'payment/submit': 900,
    'support/ticket': 1000
}

for record in sys.stdin:
    if not record:
        continue

    key, raw_values = record.strip().split("\t", 1)
    clean_values = raw_values[1:-1]

    client_list = []
    server_capacity = {}

    for item in clean_values.split("\", \""):
        item = item.strip("\"")

        predicted, details = item.split("  ")
        predicted = int(predicted.strip("'"))
        info_parts = details[2:-1].split(",")

        client_name = info_parts[0].strip(" ").strip("'")
        endpoint = info_parts[1].strip(" ").strip("'")
        available_servers = int(float(info_parts[2].strip(" ").strip("'"))) if len(info_parts) == 3 else 0
        available_servers = 3 - available_servers

        if endpoint not in server_capacity:
            server_capacity[endpoint] = available_servers

        if client_name not in client_list:
            client_list.append(client_name)
            if server_capacity[endpoint] > 0:
                server_capacity[endpoint] -= 1
                expected_status = 200
                print(f'{client_name}\t{predicted==expected_status} {endpoint_prices[endpoint]} {key}')
            else:
                expected_status = 500
                print(f'{client_name}\t{predicted==expected_status} 0 {key}')
