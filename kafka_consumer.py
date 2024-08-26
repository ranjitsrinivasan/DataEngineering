from kafka import KafkaConsumer
import json

if __name__ == "__main__":
    consumer = KafkaConsumer("SampleDataWith2Partition",
    bootstrap_servers = '192.168.1.7:9092',
    auto_offset_reset = "earliest",
    group_id="consumer-group-a" )

    print("strating the consumer")

    for msg in consumer:
        print("Sample Data= {}".format(json.loads(msg.value)))