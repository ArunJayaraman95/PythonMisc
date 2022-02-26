import os
import smtplib
import time

address = os.environ.get('MAIN_EMAIL')
password = os.environ.get('MAIN_EMAIL_PASSWORD')
school = os.environ.get('SCHOOL_EMAIL')


test = "test"

# Function to send emails
def sendEmail(subjectx, bodyx, email_address = address):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(address, password)

        msg = f'Subject: {subjectx} \n\n\n{bodyx}'

        # (sender, receiver, message)
        if email_address != "test":
            smtp.sendmail(address, email_address, msg)
        print("Email Sent to " + email_address)

long = """ I'm faster than fast.

Quicker than quick.

I am lightning!
"""


scriptList = long.split()


# print(scriptList)
# print("\n\n")

# for word in scriptList:
  # sendEmail("Cars", word, school)
  # time.sleep(3)


sendEmail("August 3rd Test", "How is your day going?!", test)
sendEmail("School Email Test", "Wassup Arun, \n How are you today!", test)