import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailSender:
    def __init__(self):
        self.host = smtplib.SMTP_SSL("smtp.yandex.ru", 465)
        self.login = "info@growheads.ru"
        self.password = "fgrmopbjpxiricmw"
        self.templates_dict = {
            "user_registration": {
                "Subject": "Confirm your email",
                "From": "G&H <{}>".format(self.login),
            }
        }

    def send_email(self, email_template=None, msg=None, recipient_list=None):
        email_template = self.templates_dict[email_template]
        message = MIMEMultipart('alternative')
        message["Subject"] = email_template["Subject"]
        message["From"] = email_template["From"]
        message.add_header('Content-Type', 'text/html')
        html = MIMEText(msg, 'html')
        message.attach(html)
        self.host.login(self.login, self.password)
        self.host.sendmail(from_addr=message["From"], to_addrs=recipient_list, msg=message.as_string())
        self.host.quit()
