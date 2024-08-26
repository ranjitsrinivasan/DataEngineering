from kafka import KafkaProducer
import json
from data import get_sample_data
import time

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(bootstrap_servers=['192.168.1.7:9092'])

if __name__ == "__main__":
    while 1 ==1:
        sample_data = get_sample_data()
        print(sample_data)
        #producer.send("SampleData", json_serializer(sample_data))
        producer.send("SampleDataWith2Partition", json_serializer(sample_data)) 
        time.sleep(5)
