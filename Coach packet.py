# Import Important Libriries

import requests
import pandas as pd
import time
import random
import os

""" Data Extraction from API"""

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,de;q=0.8',
    'Connection': 'keep-alive',
    'Origin': 'https://www.coachpacket.com',
    'Referer': 'https://www.coachpacket.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'auth': 'eyJraWQiOiJKdWZEbEZ4Q1BZVllXUHdJOVwvQlhISnhsdHpiNlRNbDJUTnFaRmNEbFlYUT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJmZTIzOGFhOS1lNDBjLTQwMjgtOWU5My0xMWIzMGM5YWVlNzMiLCJldmVudF9pZCI6ImY2OTJjYTQ1LTExMWQtNGNjMS05MWQ2LWQ2NWI4NjI0ZGIwNiIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2ODg3Mzg4NjgsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX0JRa2V5RXljZSIsImV4cCI6MTY4ODc1MTc1OCwiaWF0IjoxNjg4NzQ4MTU4LCJqdGkiOiJlN2Y3ZjBhMS0xNmY5LTRmMWYtYjBjNS04MzkxZmE1Y2ZiNjUiLCJjbGllbnRfaWQiOiI3Z3ZvMTZhdGJ1MGZodmE5cTY2OTA0ZHRwYiIsInVzZXJuYW1lIjoiZmUyMzhhYTktZTQwYy00MDI4LTllOTMtMTFiMzBjOWFlZTczIn0.O243sY0IN3AQBeoMnXh2lmVihoPF6aIAP1TG3evfLsuGmQ9NG4lgIdpxbrG1MF0hCHixQgVLiR7o5HlYExwdg3GD1flQz28z8G1p2lmwvhXozpM6erTR4mXFRAirLxnEpA9DD1sq2rt8qncy5OXHp5fNyegxoB_pWVPPfBWCG4jvpfbiWVj7mIMi6B4vnGrdHPNN1W-CloIfsDsBAj5XtxfLhhJFjd65ujNyYhVvMmJdtGIfqCW0O5QojFlgR1QzYNpwWAlr_mtqVODO04DXrnAsDqafkB6KXtOGwjHqbuxv8GAetQWcsk0F6tEVkNPSLCd4iCXoA4OznpuRVcZ15A',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sport': '8',
}

params = {
    'club': '',
    'college_program_id': '5298',
    'first': '',
    'gradyears[]': [
        '2025',
        '2026',
        '2027',
    ],
    'is_evaluated': 'false',
    'is_evaluated_event': 'false',
    'is_event': 'true',
    'last': '',
    'note': '',

    'page_length': '100',
    'ranks': '[]',
    'sort_by': 'last',
    'sort_order': 'ASC',
    'tournament_id': '0',
}


first_name = []
last_name = []
grad_year = []
email = []
cell_phone = []
address = []
state = []
city = []
zip_code = []
club_name = []
pos1= []
scholarship = []
event_name = []

for i in range(1, 116):
    params['page'] = str(i)



    response = requests.get('https://coachpacket.com/api/v1/athletes', params=params, headers=headers)

    print(f"Processing page {i} - Response Status: {response.status_code}")

    if response.status_code == 401:
        print("Access denied. Your authentication has expired. Please generate a new API key from the website.")

    result_json = response.json()
    result_cards = result_json['athletes']

    for result in result_cards:
        try:
            first_name.append(result['first'])
        except KeyError:
            first_name.append("Not Found")

        try:
            last_name.append(result['last'])
        except KeyError:
            last_name.append("Not Found")

        try:
            grad_year.append(result['gradyear'])
        except KeyError:
            grad_year.append("Not Found")

        try:
            email.append(result['email'])
        except KeyError:
            email.append("Not Found")

        try:
            cell_phone.append(result['phonec'])
        except KeyError:
            cell_phone.append("Not Found")

        try:
            address.append(result['haddress1'])
        except KeyError:
            address.append("Not Found")

        try:
            state.append(result['hstate'])
        except KeyError:
            state.append("Not Found")

        try:
            city.append(result['hcity'])
        except KeyError:
            city.append("Not Found")

        try:
            zip_code.append(result['hzip'])
        except KeyError:
            zip_code.append("Not Found")

        try:
            club_name.append(result['club_name'])
        except KeyError:
            club_name.append("Not Found")

        try:
            pos1.append(result['position1_abbrev'])
        except KeyError:
            pos1.append("Not Found")

        try:
            scholarship_status = result['scholarship_status']
            if scholarship_status == 'U':
                scholarship.append("Uncommitted")
            elif scholarship_status == 'C':
                scholarship.append("Committed")
            else:
                scholarship.append("Unknown")
        except KeyError:
            scholarship.append("Not Found")

        try:
            event_name.append(result['attending'][0]['event_name'])
        except (KeyError, IndexError):
            event_name.append("Not Found")

""" Download the data into an Excel File from Colab"""

df = pd.DataFrame(zip(first_name, last_name, grad_year, email, cell_phone, address, city, state, zip_code,club_name, pos1, scholarship, event_name),
                  columns= ['Frist Name', 'Last Name', 'Grad Year', 'E-mail','Cell Phone', 'Address', 'City', 'State', 'Zip Code', 'Club Name', 'Pos 1', 'Scholarship', 'Event Name'])


file_path = '/content/2023 Nexus Championship.xlsx'

df.to_excel(file_path, index=False)

from google.colab import files
files.download(file_path)

df
