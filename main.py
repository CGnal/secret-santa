import getpass
import pandas as pd

from code.person import get_conditions
from code.solver import solver, saver
from code.text import testo
from code.email_sender import EmailSender

people_dft = pd.read_excel("code/people.xlsx", index_col=0)
people_list, invalid_links = get_conditions(people_dft)
match = solver(people_list, invalid_links)
saver(match)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    sender = input("Type the email of the sender: ")
    username = input("Type your username and press enter: ")
    password = getpass.getpass(prompt="Type your password and press enter: ")
    addres_smtp = input("Type the address of the SMTP server and press enter: ")
    auth_protocol = input("It can be TLS or SSL: ")
    email = EmailSender(sender, username, password, addres_smtp, auth_protocol)

    completa = {}
    for k, v in match.items():
        completa["sender"] = k.name
        completa["receivername"] = v.name
        completa["receiversurname"] = v.surname
        completa["address"] = v.address
        completa["number"] = v.number
        if k.gender == "f":
            completa["gender"] = "a"
        else:
            completa["gender"] = "o"
        email.send_mail(testo % completa, k.email, "Secret Santa")
