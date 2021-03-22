# Autofill Google Form

import requests
import datetime
import time
import sys

# URLnya, pake formResponse
url = 'https://docs.google.com/forms/d/e/1FAIpQLSd1_vuM_rXwzL7bjp9YA343s3SKzwyIokQTo4SAHrvRGbCYsA/formResponse'


def get_values():

    values_list = []
    now = datetime.datetime.now()
    hour_minute = now.strftime("%H:%M")

    subjects_time = {
        "08:01": ["Materi Jam ke-1 (08.00 - 08.50)"],
        "09:01": ["Materi Jam ke-2 (09:00 - 09.50)"],
        "15:43": ["Materi Jam ke-3 (10.00 - 10.50)"],
    }

    date = str(now).split('-')

    for i in subjects_time[hour_minute]:
        values = {
            # NIM
            "entry.726004286": str(sys.argv[1]),
            # Nama
            "entry.959984559": str(sys.argv[2]),
            # Date
            "entry.393130259_year": date[0],
            "entry.393130259_month": date[1],
            "entry.393130259_day": date[2][0:2],
            # Kelas
            "entry.1906449228": "Kelas B2",
            # Subject
            "entry.362957536": i[0:],
            # inform Consent
            "entry.1687389616": "Dengan ini saya menyatakan diri bahwa mengikuti kuliah sesi yang bersesuaian berdasarkan jadwal yang sudah ditentukan / I hereby declare that i attend the appropriate lecture sessions based on a predetermined schedule",
        }
        values_list.append(values)
    return values_list


def send_absen(url, data):
    for d in data:
        try:
            requests.post(url, data=d)
            print("Form Tersubmit.")
            time.sleep(10)
        except:
            print("Error!")


final_data = get_values()

send_absen(url, final_data)
