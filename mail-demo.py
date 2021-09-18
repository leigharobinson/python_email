
import smtplib

from secrets import (MY_EMAIL, MY_PASSWORD)

with smtplib.SMTP('localhost', 1025) as smtp:

    subject = 'Get together soon?'
    body = 'how about a hike and hotpot October 2nd?'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(MY_EMAIL, MY_EMAIL, msg)


# dont name python file "email.py" or it will break
#  https://www.youtube.com/watch?v=JRCJ6RtE3xU
# from secrets import (MY_EMAIL, MY_PASSWORD)
# import smtplib
# from email.message import EmailMessage


# msg = EmailMessage()
# msg['Subject'] = 'Lets Hang Soon!'
# msg['From'] = MY_EMAIL
# msg['To'] = MY_EMAIL
# msg.set_content('How about a hike and some hot pot 🍲')


# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#     smtp.login(MY_EMAIL, MY_PASSWORD)

#     smtp.send_message(msg)
