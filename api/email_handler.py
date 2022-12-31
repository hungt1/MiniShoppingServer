import ssl
import smtplib
import email

import yaml

with open('./api/config.yml') as f:
    config = yaml.safe_load(f)

USERNAME = config['EMAIL']
PASSWORD = config['PASSWORD']

def send(reply_email, to):
    reply_email['Message-ID'] = email.utils.make_msgid()
    reply_email['To'] = to
    reply_email['From'] = USERNAME
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as conn:
        print('Processing ... ', end='')
        conn.login(USERNAME, PASSWORD)
        conn.sendmail(USERNAME, reply_email['To'], reply_email.as_string())
        conn.quit()
        print('Done')