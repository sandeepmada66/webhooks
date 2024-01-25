import requests
from flask import Flask, request, jsonify
import json
# from get_webhook_data import main
# app = Flask(__name__)

# Define your webhook endpoint
# from flask import Flask, request, jsonify

app = Flask(__name__)
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
        

@app.route("/alamon", methods=['POST'])
def webhook():
    # global last_data
    data = request.get_json()
    # main(data)
    return jsonify({"status": "Data posted", "data": data})
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


if __name__ == '__main__':
    
    app.run()
