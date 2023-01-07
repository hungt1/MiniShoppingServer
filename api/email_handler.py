import ssl
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import yaml

with open('./api/config.yml') as f:
    config = yaml.safe_load(f)

USERNAME = config['EMAIL']
PASSWORD = config['PASSWORD']

def send(body, to):
    reply_email = MIMEMultipart()
    reply_email['Subject'] = 'Cảm ơn bạn đã đặt hàng'
    reply_email['Message-ID'] = email.utils.make_msgid()
    reply_email['To'] = to
    reply_email['From'] = USERNAME
    reply_email.attach(MIMEText(body, 'html'))
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as conn:
        print('Processing ... ', end='')
        conn.login(USERNAME, PASSWORD)
        conn.sendmail(USERNAME, reply_email['To'], reply_email.as_string())
        conn.quit()
        print('Done')