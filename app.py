from flask import Flask, request, jsonify
import json
from flask_cors import CORS
from kafka import KafkaConsumer, KafkaProducer

app = Flask(__name__)
TOPIC_NAME = "INFERENCE"
KAFKA_SERVER = "localhost:9092"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    api_version=(0, 11, 15)
)


@app.route('/kafka/pushToConsumers', methods=['GET'])
def kafkaProducer():
    email = {
        "email_template": "user_registration",
        "msg": "Hello",
        "recipient_list": ["koptseff.mikhail@yandex.ru"],
    }
    email = json.dumps(email)
    email = str.encode(email)
    producer.send(TOPIC_NAME, email)
    producer.flush()
    return jsonify({
        "message": "You will receive an email in a short while with the plot",
        "status": "Pass"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
