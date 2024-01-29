from flask import Flask, request
import logging
from webhook_email import send_email


app = Flask(__name__)

# Configure logger for the "evo" webhook
alamon_logger = logging.getLogger("alamon")
alamon_logger.setLevel(logging.INFO)
alamon_logger.addHandler(logging.StreamHandler())


@app.route("/alamon", methods=["POST"])
def alamon_webhook():
    payload = request.json
    # send_email(payload)
    alamon_logger.info("Received payload for Alamon webhook: %s", payload)
   
    return payload


# app.run()
@app.route("/hello",methods=["GET"])
def hello_alamon():
    alamon_logger.info("Hello. Welcome to Alamon")
    print("hello")
    return "Success"
# app.run()



