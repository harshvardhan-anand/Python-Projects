import smtplib
from cred import email, password

def send_email():
    session = smtplib.SMTP('smtp.gmail.com', 587)

    session.starttls()

    session.login(email, password)

    with open('log.txt', 'r', encoding='utf-8') as file:
        message = file.read()

    session.sendmail(email, email, message)

    print('\n Email Sent')

    session.quit()