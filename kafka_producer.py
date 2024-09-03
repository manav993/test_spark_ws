from kafka import KafkaProducer
import json
import random
import time

# Initialize Kafka Producer
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Produce fake sales data
products = ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Monitor']
while True:
    sales_data = {
        'product': random.choice(products),
        'quantity': random.randint(1, 10),
        'price': round(random.uniform(100, 1000), 2)
    }
    producer.send('sales_topic_electronics', sales_data)
    print(f"Produced: {sales_data}")
    time.sleep(3)
