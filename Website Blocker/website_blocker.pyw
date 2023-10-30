# the needed libraries
import time
from datetime import datetime as dt

# the host path
host_temp = r"C:\Users\MUSAH IBRAHIM ALI\PycharmProjects\Mega Course\Website Blocker\Host File\hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = [
    "www.facebook.com", 
    "facebook.com", 
    "www.xnxx.com", 
    "xnxx.com", 
    "www.xvideos.com", 
    "xvideos.com"
]

work_start_time = dt(dt.now().year, dt.now().month, dt.now().day, 8)
work_end_time = dt(dt.now().year, dt.now().month, dt.now().day, 16)
current_time = dt.now()
space = "           "
new_line = "\n"

while True:
    if work_start_time < current_time < work_end_time:
        with open(host_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + space + website + new_line)
        # print("working hours....")
    else:
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        # print("Fun time fella....")
    time.sleep(5)
