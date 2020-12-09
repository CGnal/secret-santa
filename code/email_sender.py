import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailSender:
    def __init__(self, email_address: str, username: str, password: str, smtp_address: str, auth_protocol: str= "None",
                 port=None):
        """

        :param email_address: Email Address of the sender
        :param username: Username for login
        :param password: Password for login
        :param smtp_address: SMTP address of the SMTP server
        :param auth_protocol: STMP Authentication protocol can be "TSL" or "SSL"
        :param port: port. Defult is 465 for protocol SSL, 587 for protocol TLS, 25 otherwise
        """
        self.email_address = email_address
        self.username = username
        self.password = password
        self.smtp_address = smtp_address
        self.auth_protocol = auth_protocol
        self.port = port

    def send_mail(self, text: str, destination: str, subject: str, html: bool =True):
        """
        :param text: The text of the email
        :param destination: The destination email address
        :param subject: The email subject
        :param html: if text is with html format. Default True
        :return:
        """

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self.email_address
        msg['To'] = destination
        if html:
            msg.attach(MIMEText(text, "html"))
        else:
            msg.attach(MIMEText(text, "html"))

        try:
            if self.auth_protocol == "SSL":
                port = 465 if self.port is None else self.port
                server = smtplib.SMTP_SSL(self.smtp_address, port=port)
            elif self.auth_protocol == "TLS":
                port = 587 if self.port is None else self.port
                server = smtplib.SMTP(self.smtp_address, port=port)
                server.starttls()
            elif self.auth_protocol == "None":
                port = 25 if self.port is None else self.port
                server = smtplib.SMTP(self.smtp_address, port=port)
            else:
                raise Exception(f"{self.auth_protocol} not implemented")
            server.ehlo()
            server.login(self.username, self.password)
            print("logged")
            server.sendmail(self.email_address, destination, msg.as_string())
            print("SENT")
            server.close()
        except Exception as e:
            raise e
