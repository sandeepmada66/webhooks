import smtplib
import getpass
def send_email(body):
    HOST = "smtp.office365.com"
    PORT = 587
    
    FROM_EMAIL = 'sandeep.mada@tapinnov.com'
    TO_EMAIL = 'sandeep.mada@tapinnov.com'
    # PASSWORD = getpass.getpass("Enter password: ")
    PASSWORD = "Fuz44826"
    
    BODY = body
    SUBJECT = 'Payload'
    
    MESSAGE = "Subject: {}\n\n{}".format(SUBJECT, BODY)
    print('The email is sending')
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
# from_email = 'sandeep.mada@tapinnov.com'
# to_email = 'sandeep.mada@tapinnov.com'
# subject = 'Empty data in Incentive File Received'
# body = '''Hi,
                
# I hope this message finds you well.
# The data in the file is empty.

# Thank you
#                 '''
# send_mail(from_email,to_email,subject,body)