
import time

amazon_store = {
    "electronis": ["laptop", "charger", "mobile phone"],
    "clothing": ["shirt", "pants"],
    "books": ["Fredirech", "tom"]
}

for category, products in amazon_store.items():
    print(f" {category} section: ")
    time.sleep(3)
    for product in products:
        print(f" : {product}")
        time.sleep(2)