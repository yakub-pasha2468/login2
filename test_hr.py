from datetime import datetime
import json
import requests


def test_mark_attendance():
    try:
        latest_date = datetime.today().strftime('%Y-%m-%d')
        url = "https://hroneauthapi.hrone.cloud/oauth2/token"
        payload = 'username=9849909905&password=#Moneyheist@789&grant_type=password&loginType=1&' \
                  'companyDomainCode=qentelli'
        headers = {
            'authority': 'hroneauthapi.hrone.cloud',
            'Authorization': 'Bearer',
            'Origin': 'https://app.hrone.cloud',
            'Referer': 'https://app.hrone.cloud/',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        assert response.status_code == 200
        json_resp = json.loads(response.text)
        access_token = json_resp['access_token']
        url = "https://hronewebapi.hrone.cloud/api/timeoffice/mobile/checkin/Attendance/Request"
        headers = {
            'authority': 'hronewebapi.hrone.cloud',
            'domaincode': 'qentelli',
            'Origin': 'https://app.hrone.cloud',
            'Referer': 'https://app.hrone.cloud/',
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        time = ['20:00']
        for t in time:
            payload = "{\n    \"requestType\": \"A\",\n    \"employeeId\": 628,\n    \"latitude\": " \
                      f"\"\",\n    \"longitude\": \"\",\n    \"geoAccuracy\": \"\"," \
                      f"\n    \"geoLocation\": \"\",\n    \"punchTime\": \"{latest_date}T{t}\"," \
                      "\n    \"uploadedPhotoOneName\": \"\",\n    \"uploadedPhotoOnePath\": \"\",\n    \"uploadedPhotoTwoName\": \"\",\n    \"uploadedPhotoTwoPath\": \"\",\n    \"attendanceSource\": \"W\",\n    \"attendanceType\": \"Online\"\n}"
#             response = requests.request("POST", url, headers=headers, data=payload)
#             assert response.status_code == 200
        print(f"Attendance marked at {time} for {latest_date}")
        send_sms(f"Attendance marked at {time} for {latest_date}")
    except Exception as e:
        send_sms('WARNING: ATTENDANCE NOT MARKED')
        assert False


def send_sms(message):
    url = "https://www.fast2sms.com/dev/bulkV2"
    querystring = {"authorization": "F9ZR78D0iBqpEIw2UCszkAfcrKlNdOojvJh5LHeMn3XG6mbQWPOSIok7AWdhj58FJmrEq9XaRexpMLw3",
                   "message": message, "language": "english",
                   "route": "q", "numbers": "9849909905"}
    headers = {
        'cache-control': "no-cache"
    }
    requests.request("GET", url, headers=headers, params=querystring)
