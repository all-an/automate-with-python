"""
# NOT WORKING
"""

import smtplib, ssl

port = 465  # For SSL
# password = input("Type your password and press enter: ")

password = '#$Math397'

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("abrahaoallan54@gmail.com", password)
    # TODO: Send email here
    server.sendmail('abrahaoallan54@gmail.com', 'allan8tech@gmail.com', 'Subject: Hello from Python SMTPLib')