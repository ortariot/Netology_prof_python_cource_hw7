import email
import imaplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP_SSL


class EmailClient():
    def __init__(self, smtp, imap, user_login, user_password):
        self.smtp = smtp
        self.imap = imap
        self.login = user_login
        self.password = user_password
        self.transfer_connect()
        self.reciever_connect()

    def transfer_connect(self):
        self.mail_transfer = SMTP_SSL(self.smtp, 465,
                                      context=ssl.create_default_context()
                                      )
        self.mail_transfer.login(self.login, self.password)

    def reciever_connect(self):
        self.mail_reciever = imaplib.IMAP4_SSL(self.imap)
        self.mail_reciever.login(self.login, self.password)

    def transfer_disconnect(self):
        self.mail_transfer.quit()

    def reciever_disconnect(self):
        self.mail_reciever.logout()

    def create_message(self, recipients, subject, message):
        self.msg = MIMEMultipart()
        self.msg['From'] = self.login
        self.msg['To'] = ', '.join(recipients)
        self.msg['Subject'] = subject
        self.msg.attach(MIMEText(message))

    def send_message(self):
        self.mail_transfer.sendmail(self.login, self.msg['To'],
                                    self.msg.as_string()
                                    )

    def recieve_message(self, folder='inbox', header=None):
        self.mail_reciever.select(folder)
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = self.mail_reciever.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = self.mail_reciever.uid('fetch', latest_email_uid,
                                              '(RFC822)'
                                              )
        raw_email = data[0][1].decode('utf-8')
        email_message = email.message_from_string(raw_email)
        return [result, email_message]

    def __dell__(self):
        self.transfer_disconnect()
        self.reciever_disconnect()


if __name__ == '__main__':
    gmail_smtp = "smtp.gmail.com"
    gmail_imap = "imap.gmail.com"
    login = 'login@gmail.com'
    password = 'password'
    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'
    email_box = EmailClient(gmail_smtp, gmail_imap, login, password)
    email_box.create_message(recipients, subject, message)
    email_box.send_message()
    email_box.recieve_message()
