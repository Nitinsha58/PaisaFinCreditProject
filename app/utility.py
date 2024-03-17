import requests, os, json
from django.conf import settings

def send_otp_to_phone(phone_number, otp_code, message=None):
    url = "https://www.fast2sms.com/dev/bulkV2"

    payload = f"variables_values={otp_code}&route=otp&numbers={phone_number}"
    headers = {
        'authorization': settings.OTP_AUTHORIZATION_KEY,
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
        }
    
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text