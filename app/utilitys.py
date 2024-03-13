import requests, os, json
from django.conf import settings


if settings.DEBUG:
    from dotenv import load_dotenv
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    OTP_AUTHORIZATION_KEY = os.getenv('OTP_AUTHORIZATION_KEY')
else:
    with open('/etc/config.json') as f:
        config = json.load(f)
    
    OTP_AUTHORIZATION_KEY = config.get("OTP_AUTHORIZATION_KEY", None)

def send_otp_to_phone(phone_number, otp_code, message=None):
    url = "https://www.fast2sms.com/dev/bulkV2"
    print(OTP_AUTHORIZATION_KEY)

    payload = f"variables_values={otp_code}&route=otp&numbers={phone_number}"
    headers = {
        'authorization': OTP_AUTHORIZATION_KEY,
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
        }
    
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text