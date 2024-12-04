import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def send_email(to_addr, subject, text, attachments):
    msg = MIMEMultipart()
    msg['From'] = 'vityaanpilogov@yandex.ru'
    msg['To'] = to_addr
    msg['Subject'] = subject

    msg.attach(MIMEText(text, 'plain', 'utf-8'))

    for attachment in attachments:
        part = MIMEBase('application', 'octet-stream')
        with open(attachment, 'rb') as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={attachment}')
        msg.attach(part)

    server = smtplib.SMTP('smtp.yandex.ru', 587)
    server.starttls()
    server.login('vityaanpilogov@yandex.ru', 'PASSWORD')

    server.send_message(msg)
    server.quit()
