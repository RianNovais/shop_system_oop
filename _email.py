import os
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from smtplib import SMTP
import string
from pathlib import Path

# the email class is used to send emails. When the export of a spreadsheet is completed, be it customers, products or sales
# , the user has the option of an email being sent, containing the spreadsheet as an attachment. We used Python's own smtplib,
# and defined variables in a .env file that was loaded via dotenv. As attributes of the Email class we have port, server,
# sending email, and the email password subsequently we have 3 functions, each sending a type of spreadsheet,
# be it customers, sales or products.


load_dotenv()

class Email():
    def __init__(self):
        self.server = os.getenv('SMTP_SERVER')
        self.port = os.getenv('SMTP_PORT')
        self.email_sender = os.getenv('EMAIL_SENDER')
        self.email_passwd = os.getenv('EMAIL_PASSWORD')

    def sendProductSpreadsheetEmail(self, spreadsheetPath):

        #opening the message that will be sent in the email, which is html and editing it with string.template using
        #substitute
        MSG_PATH = Path().absolute() / 'message.html'
        with open(MSG_PATH, 'r', encoding='utf-8') as msg:
            mensagem = msg.read()
            template = string.Template(mensagem)
            textoEmail = template.substitute(type = 'Product')

        # creating the multipart, which will be the parts of our email, such as sender, recipient, and subject
        mime_multipart = MIMEMultipart()
        mime_multipart['from'] = os.getenv(self.email_sender)
        mime_multipart['to'] = 'riannovais3@gmail.com'
        mime_multipart['subject'] = 'Product Spreadsheet'


        #creating a mimetext, passing our formatted text from the html and throwing this mimetext into the MimeMultiPart
        mime_text = MIMEText(textoEmail, 'html', 'utf-8')
        mime_multipart.attach(mime_text)

        #opening the file that we will attach to the email, in this case our spreadsheet with the path passed in the
        #function parameter, we load it with MIMEApplication and then add it to MimeMultiPart
        with open(spreadsheetPath, 'rb') as file:
            planilha = MIMEApplication(file.read(), _subtype="xlsx")
            planilha.add_header('Content-Disposition', 'attachment', filename='planilha.xlsx')
            mime_multipart.attach(planilha)

        #estabilishing the server SMTP connection, passing an server and port, and send email
        with SMTP(self.server, self.port) as server:
            server.ehlo()
            server.starttls()
            server.login(self.email_sender, self.email_passwd)
            server.send_message(mime_multipart)

            print('Email send sucessfully')

    def sendCustomerSpreadsheetEmail(self, spreadsheetPath):

        # abrindo a mensagem e alterando ela via string.Template
        MSG_PATH = Path().absolute() / 'message.html'
        with open(MSG_PATH, 'r', encoding='utf-8') as msg:
            mensagem = msg.read()
            template = string.Template(mensagem)
            textoEmail = template.substitute(type='Customer')

        # criando o multipart
        mime_multipart = MIMEMultipart()
        mime_multipart['from'] = os.getenv(self.email_sender)
        mime_multipart['to'] = 'riannovais3@gmail.com'
        mime_multipart['subject'] = 'Customer'

        # definindo o mime text e jogando no mimemultipart
        mime_text = MIMEText(textoEmail, 'html', 'utf-8')
        mime_multipart.attach(mime_text)

        # abrindo a planilha
        with open(spreadsheetPath, 'rb') as file:
            planilha = MIMEApplication(file.read(), _subtype="xlsx")
            planilha.add_header('Content-Disposition', 'attachment', filename='planilha.xlsx')
            mime_multipart.attach(planilha)

        with SMTP(self.server, self.port) as server:
            server.ehlo()
            server.starttls()
            server.login(self.email_sender, self.email_passwd)
            server.send_message(mime_multipart)

            print('Email send sucessfully')

    def sendSaleSpreadsheetEmail(self, spreadsheetPath):

        # abrindo a mensagem e alterando ela via string.Template
        MSG_PATH = Path().absolute() / 'message.html'
        with open(MSG_PATH, 'r', encoding='utf-8') as msg:
            mensagem = msg.read()
            template = string.Template(mensagem)
            textoEmail = template.substitute(type='Sales')

        # criando o multipart
        mime_multipart = MIMEMultipart()
        mime_multipart['from'] = os.getenv(self.email_sender)
        mime_multipart['to'] = 'riannovais3@gmail.com'
        mime_multipart['subject'] = 'Sales Spreadsheet'

        # definindo o mime text e jogando no mimemultipart
        mime_text = MIMEText(textoEmail, 'html', 'utf-8')
        mime_multipart.attach(mime_text)

        # abrindo a planilha
        with open(spreadsheetPath, 'rb') as file:
            planilha = MIMEApplication(file.read(), _subtype="xlsx")
            planilha.add_header('Content-Disposition', 'attachment', filename='planilha.xlsx')
            mime_multipart.attach(planilha)

        with SMTP(self.server, self.port) as server:
            server.ehlo()
            server.starttls()
            server.login(self.email_sender, self.email_passwd)
            server.send_message(mime_multipart)

            print('Email send sucessfully')
        ...


if __name__ == '__main__':
    ...
    # e = Email()
    # e.sendProductSpreadsheetEmail(r'C:\Users\Rian Novais\Documents\PROJETOS\Pessoal\shop_system_oop\shop_system_oop\spreadsheets\customers.xlsx')


