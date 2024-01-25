import requests
from flask import Flask, request, jsonify
import json
import logging
# from get_webhook_data import main
# app = Flask(__name__)

# Define your webhook endpoint
# from flask import Flask, request, jsonify

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger instance
logger = logging.getLogger(__name__)

        

@app.route("/alamon", methods=['POST'])
def webhook():
    # global last_data
    payload = request.get_data(as_text=True)
    logger.info("Received payload for Evo webhook: %s", payload)
    return payload



    # data = request.get_json()
    # # main(data)
    # return jsonify({"status": "Data posted", "data": data})
    # try:
    #         print("Data has changed:")
    #         print(json.dumps(data))

    #         # You can access specific values from the data
    #         for each_data in data:
    #             key_value = each_data.get("user")
    #             print("Value of 'user':", key_value)

    # except Exception as e:
    #     print("Error:", e)

    # return jsonify({"status": "Data posted"})
    # data_endpoint = "/data"

# last_data = None

# def main(data):
#     print("Data")
#     print("Data has changed:")
#     print(json.dumps(data))
#     key_values = []
#     # data = webhook()
#     for each_data in data:
#         key_value = each_data.get("user")
#         key_values.append(key_value)
#         print("Value of 'user':", key_value)
#     print(key_values)
#     return key_values


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
