from confluent_kafka import Producer, Consumer

p = Producer({'bootstrap.servers': 'localhost:9092'})
p.produce('mytopic', 'my message')

c = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'mygroup'})
c.subscribe(['mytopic'])
msg = c.poll(1.0)

print(msg.value())

# Output:
# 'my message'
