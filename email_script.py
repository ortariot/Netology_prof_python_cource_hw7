# Мы устроились на новую работу. Бывший сотрудник начал разрабатывать модуль для работы с почтой, но не успел доделать его. Код рабочий. Нужно только провести рефакторинг кода.

# Создать класс для работы с почтой;
# Создать методы для отправки и получения писем;
# Убрать "захардкоженный" код. Все значения должны определяться как аттрибуты класса, либо аргументы методов;
# Переменные должны быть названы по стандарту PEP8;
# Весь остальной код должен соответствовать стандарту PEP8;
# Класс должен инициализироваться в конструкции.
# if __name__ == '__main__'



import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


#send message
class EmailClient(email):
    def __init__(self, smtp, imap, user_login, user_password):
        self.smmtp = smtp
        self.imap = imap
        self.login = user_login
        self.password = user_password

    def create_message(self, recipients, subject, message):
        self.msg = MIMEMultipart()
        self.msg['From'] = self.login
        self.msg['To'] = ', '.join(recipients)
        self.msg['Subject'] = subject
        self.msg.attach(MIMEText(message))

    def send_message(self):
        ms = smtplib.SMTP(self.smmtp, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()
        ms.login(self.login, self.password)
        ms.sendmail(self.login, ms, self.msg.as_string())
        ms.quit()

    def recieve_message(self, header):
        mail = imaplib.IMAP4_SSL(self.imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        self.message_from_string(raw_email)
        mail.logout()


if __name__ == '__main__':
    gmail_smtp = "smtp.gmail.com"
    gmail_imap = "imap.gmail.com"
    login = 'login@gmail.com'
    password = 'qwerty'
    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'
    email_box = EmailClient(gmail_smtp, gmail_imap, login, password)
    email_box.create_message(recipients, subject, message)
    email_box.send_message()
    email_box.recieve_message(header=None)

    