from confluent_kafka import Consumer
import pandas as pd

c = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'mygroup'})
c.subscribe(['mytopic'])

data = []

for i in range(1000):
    msg = c.poll(1.0)
    if msg is not None:
        data.append(msg.value())

df = pd.DataFrame(data)
print(df.describe())

# Output:
#                0
# count  1000.000000
# mean     49.530000
# std      28.867707
# min       1.000000
# 25%      25.000000
# 50%      50.000000
# 75%      74.000000
# max     100.000000
