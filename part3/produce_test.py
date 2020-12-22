#https://timber.io/blog/hello-world-in-kafka-using-python/

#https://towardsdatascience.com/create-your-first-etl-pipeline-in-apache-spark-and-python-ec3d12e2c169

'''
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties
in/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic sample
bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic sample
'''

from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
# Asynchronous by default
future = producer.send('sample2', b'raw_bytes')

# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    # Decide what to do if produce request failed...
    log.exception()
    pass

# Successful result returns assigned partition and offset
print (record_metadata.topic)
print (record_metadata.partition)
print (record_metadata.offset)

