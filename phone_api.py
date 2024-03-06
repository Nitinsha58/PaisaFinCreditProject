# from twilio.rest import Client

# account_sid = 'ACcf40d8fd98e72e2e84732718c1407e4f'
# auth_token = '1369481a6f7acf4179b1060029485001'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#   from_='+16315273661',
#   body='Hi, Your Verification code for PaisaFinCredit India is: 454523',
#   to='+917982683117'
# )

# print(message.sid)

import requests

url = "https://www.fast2sms.com/dev/bulkV2"

payload = "variables_values=5599&route=otp&numbers=7982683117"
headers = {
    'authorization': "A1gTUmbucRf5s06XnDVNxkQ8hFqle4voIOSiB2rY97wpzPMaWEmSVNKazuGhv1iHU37wORrQtBJLM9dX",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
# Service Route Success Response:
# {
#     "return": true,
#     "request_id": "lwdtp7cjyqxvfe9",
#     "message": [
#         "Message sent successfully"
#     ]
# }