import requests
import time
import threading
import itertools
import sys

def send_request():
    url = "https://kanal.umk.ac.id/mahasiswa/entrirencanastudi"
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9,id;q=0.8,it-IT;q=0.7,it;q=0.6",
        "cache-control": "max-age=0",
        "content-length": "1270",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": ("SERVER=srvpkanal1; sso_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJOVGcwTTJFMFpqSmtOemt6T1RjM1ltWXhNRGxoWkdNME1qaG1OV016TWpJME5HRmpNekUzT1RBNVl6TXlOVE0xTlRSaFpqSTNNVEV5TURVNU1UZzVNRE01TVdFNFpEUXdZV0l5TTJaa1pXWXlOekpsTVdFME1HWmtOVE5qWVRZMVpqQTFZekU0WldFeFpqaGhabVUzWVRJMU1EQTNaREV5WkRNMk9XVTJOemRKYm5KRGNubEdObGhoWlV4bFV6RkZVbWxXYTFCMVUxRlJNMVZ1YkdWaFRHWjNQVDAiLCJhdWQiOiIyMDIxNTEwMDIiLCJzdWIiOiJkMjU0ZGUyZjg3MGMyODBiNmYxYzM4Zjk1Y2JhODJiNmFmNGYwZTA4IiwiaWF0IjoxNzIyMjA3MDAyfQ.1rO66etC7w6DZ5no-JcQLwYjMdHbYL3pqZPd921LmzI; sso_time=akdEbS9HQlRFVEt2US9lZ3liUXBKTS8xM0tWTVhuVk1kMUFUc05ON2dDV1VvMmc4bmZBVnIwMGlKcDNRVDZNTg; XSRF-TOKEN=eyJpdiI6ImtGa3FCeSsxbG5IeXZ1WmIrWU5qa3c9PSIsInZhbHVlIjoiV3lKSWpUYzFEZXM5MVF1L1V6SktpbG1JZFlObXZxa2FMYVVCQjhqVTBvczhOU0xPVnJOVmN1VnFFVXZ6R2RxR3R4M1M4SkFXQlYxNDVaVzFkcWVGRGp3UHhZamI1UEd6YTY1Nk1iZmJ3cnVKUGltUkdYZ2IvMzRiRDRoblZEYWEiLCJtYWMiOiIxNzQ5YTBmYmE5NTNiNjU0MjE4YjNiYTVmNjE0YjA4YmNmZWI5ZDI0MDIyMWZiOWNmOTI5ZjYyODU4Mzk1NTI1IiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6IlROZDlURWc3NjhTRmZ3YlJ6ZVlrOFE9PSIsInZhbHVlIjoiR3ZXaXJPaTkxMldRTEd4ZjNGN25GbGR1N3I2K25kQVdjUVV1b01XcHo4MVNGRHp1Qm1FTmRZcjBnRjJpL1d5Z0R3Mjl0bkExNDNaZjFxRmxZUGJ6ZnUwNXNLV0RFamw1SGR1SkdMUmkvWFE0UDlNZ2I4eEdqdVlwbytZVUlObzMiLCJtYWMiOiI4ZDEzYzY0OWI4OTk5YWZhZjNkMzY2MDZjNGI2OWRhZDgyOTlhMTQ4YzlmNzUyNzc1ZWJmNjYzZmM5NjZhYWFhIiwidGFnIjoiIn0%3D"),
        "dnt": "1",
        "origin": "https://kanal.umk.ac.id",
        "priority": "u=0, i",
        "referer": "https://kanal.umk.ac.id/mahasiswa/entrirencanastudi",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"127\", \"Chromium\";v=\"127\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
    }
    data = {
        "_token": "4hdHxTtDwsVjtrVjixa1ng2ur2SOaTAhixtYpSzn",
        "makul[]": [
            "NDYzNzA5MzMyNzExMjc0N2JmOTg1NDY4N2I4ZDBhYzhkNGIzN2EyY2QzNjc0MzM3ZWZiZTE3MzFkODAxNGM5OGQxMDhjZmVmYTlhZmJmMmQxYjYyNmExODRiZjgyZjRiMzcyOWYxNjc4ZDk4NWQ0NThhN2I3MTRkMzExOGFhNTUzOHRHV2dzZXdySnJkY0I4OHkyOUcydlRhTU12bWM5NCtCREhDRXFSSzJZPQ",
            "ODMxNTA5OWJmNjM0ZTMyMTU3OTQ1YmZiYWQ2ODQyOTc5NzgyODUxNTczODYzZDcyODA4YjZkODY2YzI5Nzc3NGRkMTc4NDMyZWM0ZmU1OTExZTY0MmJjOTZkNzFhODNlNDE4MmFkZjFmZTNjNDE4ZDYxNmJjYzNlY2NmNTc0MDFoSFhGRjhiVEJIV3JodVR3cWthSmtVRXVuc0lGcVpSV0VNMnpsQlhYMFlvPQ",
            "MjI3MTc2YjEwYTIyYTU5M2IyNDkxYTA2OWQzNDdhZTNjMzJlMzc1MDViOWIzMDI3NjZhZWZkMDQzNGRkYjQzNzZiYjBiZjYwNTBlY2FlZDZjYmQ2MDBiZjQ2YTc4ZjYzNGJmMzRkMjQ1MzFmMzk0NzVhNDBhMjQ5MTk4ZTJmMWZiY0gxMlUzZENhYWQvWnIxc0JXdW05TTJxU25XWXdPUjYzaUEzb2ZHZ2VrPQ",
            "Nzc2MjVjMWYwNTcwYmRiOTNiNjVhOTc0YjA0ZDhhMjZlODU4MzI4NzY5YjA4MTYzOTU3ZDZhZGI2YzgwOTk0MTQwNmY3NTg0MDgyZjU3MDc4MTBhYzk3YTNjNWNlYmE0OTVmMjBiYWY4NDExODk0NzJiODI5ZjlmNjg1ODI2MTNQS2dvNzd6VXpUaDdPNTZpbmg3Y0RldnVQL3o4NllGbGVDcEZUaklzeSswPQ",
            "NTJkOGRjZGUxNzhmYzgxY2VkNDA2OTZkMmFlMjdhY2VhNzk3NmQyYjNjNGNiN2I2YTNhMmE1OTMyMWJkY2RmNWViM2E0MjNlMjZmZjc5NTQ3MTU1NDE1MGZmMDliNTA0ZmE1YjhjMDQ3YmNhNDlmY2IxMjI1NTBjM2U5Mzg5YWFFQy8wS1ZURmZKV202b1VzdkpCbUZ0d3oyeGhGV0lZd0EwWVBsREFFNHQ0PQ"
        ],
        "submit": ""
    }

    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if stop_thread.is_set():
                break
            sys.stdout.write('\rLoading ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\rDone!     ')

    stop_thread = threading.Event()
    loading_thread = threading.Thread(target=animate)
    loading_thread.start()

    try:
        response = requests.post(url, headers=headers, data=data)
        stop_thread.set()
        loading_thread.join()
        print("\nStatus Code:", response.status_code)
        print("Response:", response.text)
    except requests.exceptions.RequestException as e:
        stop_thread.set()
        loading_thread.join()
        print("\nError:", e)
    finally:
        time.sleep(5)
        send_request()

send_request()
