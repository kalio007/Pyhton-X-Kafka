from fastapi import FastAPI, HTTPException
from kafka import KafkaProducer
import json

app = FastAPI()

# kafka sever setup
KAFKA_BOOTSTRAP_SERVERS = 'localhost:9092'
KAFKA_TOPIC = 'new_signup'
# producer setup
kafka_producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
@app.post("/signup")
async def signup(data: dict):
    try:
        username = data.get('username')
        email = data.get('email')

        # payload
        event_data = {
            'username': username,
            'email': email,
            'event_type': 'user_signup'
        }
        kafka_producer.send(KAFKA_TOPIC, value=event_data)
        # producer.send('fizzbuzz', {'foo': 'bar'}) 
        return {"message": "User signed up successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))