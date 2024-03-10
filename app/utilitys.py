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

def send_otp_to_phone(request, phone_number, otp_code, message=None):
    # send otp code to user
    pass

def verify_otp():
    # verify otp code
    pass

# Service Route Success Response:
# {
#     "return": true,
#     "request_id": "lwdtp7cjyqxvfe9",
#     "message": [
#         "Message sent successfully"
#     ]
# }