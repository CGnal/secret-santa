import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailSender:
    """
        Email Sender Utility Class
        ...
        Attributes
        ----------
        email_address : str
            Email Address of the sender
        username : str
            Username for login
        password : str
            Password for login
        smtp_address : str
            SMTP address of the SMTP server
        auth_protocol : start
            STMP Authentication protocol can be "TSL" or "SSL"
        Methods
        -------
        send_mail(text, destination)
            Send the mail with a specific text to a specific destination
        """

    def __init__(self, email_address, username, password, smtp_address, auth_protocol="None", port=None):
        self.email_address = email_address
        self.username = username
        self.password = password
        self.smtp_address = smtp_address
        self.auth_protocol = auth_protocol
        self.port = port

    def send_mail(self, text, destination, subject, html=True):
        """
        :param text: The text of the email
        :type text: str
        :param destination: The destination email address
        :type destination: str
        :param subject: The email subject
        :type subject: str
        :param html: if text is with html format. Default True
        :type html: bool
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
