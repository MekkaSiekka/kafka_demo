
from kafka import KafkaConsumer

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('sample',
                         bootstrap_servers=['localhost:9092'])
for message in consumer:
    transaction = message.value.decode('utf-8')
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`

    # print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
    #                                       message.offset, message.key,
    #                                       message.value))
    print(transaction)  #item_id, type, price, amount
    print()