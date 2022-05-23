from kafka import KafkaConsumer
import json

from email_sender import EmailSender

TOPIC_NAME = "INFERENCE"
KAFKA_SERVER = "localhost:9092"

consumer = KafkaConsumer(
    TOPIC_NAME,
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
)

for email in consumer:
    email_data = email.value
    email_template = email_data["email_template"]
    msg = email_data["msg"]
    recipient_list = email_data["recipient_list"]
    EmailSender().send_email(email_template=email_template, msg=msg, recipient_list=recipient_list)
