import requests
import time

r = requests.get("https://wallpaper.dog/large/10876450.jpg", stream=True)

with open("wppr.png", 'wb') as wp:
    for chunk in r.iter_content(chunk_size=1024):
        if not chunk:
            break

        wp.write(chunk)

time.sleep(1.5)
