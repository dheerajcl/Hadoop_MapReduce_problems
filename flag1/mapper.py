#!/usr/bin/env python3
import sys

positive_words = set(
    ["excellent", "outstanding", "reliable", "impressive", "durable", "user-friendly", "high-quality", "affordable", "satisfied", "superb"]
    )
negative_words = set(
    ["disappointing", "poor", "unreliable", "defective", "complicated", "expensive", "frustrating", "cheap", "unusable", "awful"]
    )

for line in sys.stdin:
    line = line.strip()
    
    try:
        review_id, product_id, review_text = line.split("|")
    except ValueError:
        continue
    
    review_text = review_text.lower()
    review_text = review_text.replace(".", "").replace(",", "")
    
    no_of_positive = sum(1 for word in review_text.split() if word in positive_words)
    no_of_negative = sum(1 for word in review_text.split() if word in negative_words)
    
    if no_of_positive > no_of_negative:
        sentiment = "Positive"
    elif no_of_negative > no_of_positive:
        sentiment = "Negative"
    else:
        continue

    print(f"{product_id}\t{sentiment}")
