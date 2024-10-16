#!/usr/bin/env python3
import sys
import json

for line in sys.stdin:
    line = line.strip().rstrip(',')
    
    if line in ['[', ']'] or not line:
        continue

    try:
        record = json.loads(line)
        total_rev = 0
        total_cogs = 0
        has_sales_data = False

        for category in record.get('categories', []):
            if category in record.get('sales_data', {}):
                sales_info = record['sales_data'][category]
                if 'revenue' in sales_info and 'cogs' in sales_info:
                    total_rev += sales_info['revenue']
                    total_cogs += sales_info['cogs']
                    has_sales_data = True

        if has_sales_data:
            profit_or_loss = "profit" if (total_rev - total_cogs) > 0 else "loss"
            print(f"{record['city']}\t{profit_or_loss}")

    except json.JSONDecodeError as e:
        sys.stderr.write(f"JSON decode error: {e}\n")
    except Exception as e:
        sys.stderr.write(f"Processing error: {e}\n")
