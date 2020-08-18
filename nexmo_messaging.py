import nexmo

client = nexmo.Client(key='2e2955ad', secret='uV0maJ5LHjRO1TKF')

responseData = client.send_message(
    {
        "from": "Vetrichelvan",
        "to": "919677758721",
        "text": "Hello this is vetri from nexmo.",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")