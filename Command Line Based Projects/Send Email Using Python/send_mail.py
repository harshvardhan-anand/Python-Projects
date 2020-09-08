import smtplib
from cred import email, password

session = smtplib.SMTP('smtp.gmail.com', 587)

session.starttls()

session.login(email, password)

message = 'This is a python file.'


session.sendmail(email, email, message)

session.quit()