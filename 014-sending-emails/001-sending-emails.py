"""
# NOT WORKING
"""

import smtplib

connection = smtplib.SMTP('smtp.gmail.com', 587)

print(type(connection))

connection.ehlo()

# print(connection.ehlo())

connection.starttls()

connection.ehlo()

connection.login('abrahaoallan54@gmail.com', '#$Math397')

connection.sendmail('abrahaoallan54@gmail.com', 'allan8tech@gmail.com', 'Subject: Hello from Python SMTPLib')