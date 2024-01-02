# import smtplib
# import getpass
 
# HOST = "smtp-mail.outlook.com"
# PORT = 465
 
# FROM_EMAIL = "ganesh.bollem@tapinnov.com"
# TO_EMAIL = "sandeep.mada@tapinnov.com"
# # PASSWORD = getpass.getpass(prompt="Fuz44826")
# PASSWORD = input("Vanetha407@")
 
# BODY = "This is the body of the email."
# SUBJECT = "This is the subject of the email."
 
# MESSAGE = "Subject: {}\n\n{}".format(SUBJECT, BODY)
# print('Hi the process is running')
# try:
    
#     smtp = smtplib.SMTP_SSL(HOST, PORT)
#     smtp.ehlo()  # Use STARTTLS for encryption

#     status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
#     print(f"[*] Logging in: {status_code} {response}")

#     smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
#     smtp.quit()
# except Exception as e:
#     print('Error: ',e)

import smtplib
import getpass
 
HOST = "smtp-mail.outlook.com"
PORT = 587
 
FROM_EMAIL = "sandeep.mada@tapinnov.com"
TO_EMAIL = "ganesh.bollem@tapinnov.com"
# PASSWORD = getpass.getpass("Enter password: ")
PASSWORD = "Fuz44826"
 
BODY = "This is the body of the email."
SUBJECT = "This is the subject of the email."
 
MESSAGE = "Subject: {}\n\n{}".format(SUBJECT, BODY)
print('The process is running')
try:
    smtp = smtplib.SMTP(HOST, PORT)
    
    status_code, response = smtp.ehlo()
    print(f"[*] Echoing the server: {status_code} {response}")
    
    status_code, response = smtp.starttls()
    print(f"[*] Starting TLS connection: {status_code} {response}")
    
    status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
    print(f"[*] Logging in: {status_code} {response}")
    
    smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
    smtp.quit()
except Exception as e:
  print("Connection failed:", e)