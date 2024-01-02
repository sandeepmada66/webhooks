# # import requests
# import json
# # from flask import Flask, request

# # app = Flask(__name__)

# # # Replace this URL with your desired webhook endpoint
# # webhook_url = "https://webhook.site/0040f40c-37d4-41ed-95fa-0c113a4117d0"

# # # Initialize the last_data variable to keep track of changes
# # last_data = None


# # @app.route('/webhook', methods=['POST'])
# # def webhook():
# #     global last_data
# #     data = request.get_json()

# #     try:
# #         # Check if there is a change in the data
# #         if data != last_data:
# #             last_data = data

# #             # Perform the desired action with the updated data
# #             # print("Data has changed:")
# #             # print(json.dumps(data, indent=2))

# #             # # Make a request to the webhook endpoint
# #             response = requests.get(webhook_url)

# #             # Attempt to parse the response as JSON
# #             try:
# #                 response_data = response.json()
# #                 print("Response from webhook endpoint:")
# #                 print(json.dumps(response_data, indent=2))
# #             except json.JSONDecodeError:
# #                 # Handle the case where the response is not valid JSON
# #                 print("Response from webhook endpoint is not valid JSON.")

# #     except Exception as e:
# #         print("Error:", e)

# #     return "Webhook received successfully"


# # if __name__ == '__main__':
# #     # Start the Flask app to receive webhook notifications
# #     app.run(port=5000)
import requests
from flask import Flask, request, jsonify

# app = Flask(__name__)

# # Replace this URL with your desired webhook endpoint
# webhook_url = "https://webhook.site/0040f40c-37d4-41ed-95fa-0c113a4117d0"

# # Initialize the last_data variable to keep track of changes
# last_data = None

# @app.route('/webhook', methods=['POST'])
# def webhook():
#     global last_data
#     data = request.get_json()

#     try:
#         # Check if there is a change in the data
#         if data != last_data:
#             last_data = data

#             # Perform the desired action with the updated data
#             # You can uncomment the following lines if you want to print the data
#             print("Data has changed:")
#             print(json.dumps(data, indent=2))

#             # Make a request to the webhook endpoint with the updated data
#             response = requests.post(webhook_url, params=data)

#             # Check the status code of the response
#             if response.status_code == 200:
#                 print("Request to webhook endpoint successful")
#             else:
#                 print("Request to webhook endpoint failed with status code:", response.status_code)

#     except Exception as e:
#         print("Error:", e)

#     return "Webhook received successfully"

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, request, jsonify
import json
app = Flask(__name__)

# Define your webhook endpoint
from flask import Flask, request, jsonify

app = Flask(__name__)
webhook_endpoint = "/webhook"
data_endpoint = "/data"

last_data = None

@app.route(webhook_endpoint, methods=['POST'])
def webhook():
    global last_data
    data = request.get_json()

    try:
        # Check if there is a change in the data
        if data != last_data:
            last_data = data
            print("Data has changed:")
            print(json.dumps(data, indent=2))

            # You can access specific values from the data
            key_value = data.get("user")
            print("Value of 'user':", key_value)

            return jsonify({"status": "success"})

    except Exception as e:
        print("Error:", e)

    return jsonify({"status": "failed"})

@app.route(data_endpoint, methods=['GET'])
def get_data():
    global last_data
    return jsonify(last_data)

# if __name__ == '__main__':
#     app.run(debug=True)


if __name__ == '__main__':
    
    app.run(debug=True, port=5000)
