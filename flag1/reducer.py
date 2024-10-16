#!/usr/bin/env python3
import sys

current_product = None
positive_reviews = 0
negative_reviews = 0
total_reviews = 0

for line in sys.stdin:
    product_id, sentiment = line.strip().split("\t")

    if current_product and current_product != product_id:
        overall_sentiment = "Positive" if positive_reviews >= negative_reviews else "Negative"
        print(f"{current_product} {overall_sentiment} {positive_reviews}/{total_reviews} {negative_reviews}/{total_reviews}")
        
        positive_reviews = 0
        negative_reviews = 0
        total_reviews = 0

    current_product = product_id
    total_reviews += 1

    if sentiment.lower() == "positive":
        positive_reviews += 1
    elif sentiment.lower() == "negative":
        negative_reviews += 1

if current_product:
    overall_sentiment = "Positive" if positive_reviews >= negative_reviews else "Negative"
    print(f"{current_product} {overall_sentiment} {positive_reviews}/{total_reviews} {negative_reviews}/{total_reviews}")