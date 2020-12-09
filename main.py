import argparse
import getpass

import pandas as pd

from santacode.email_sender import EmailSender, build_email
from santacode.person import get_conditions
from santacode.solver import solver, saver


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--sender', help='Email of the sender', default=None)

    parser.add_argument('--username', help='username for the mail server', default=None)

    parser.add_argument('--password', help='password for the mail server', default=None)

    parser.add_argument('--smtp-server', help='address of the SMTP server', default=None)

    parser.add_argument('--protocol', help='protocol for the SMTP server', default=None)

    parser.add_argument('--input-file', help='Name of the Excel input file', default="santacode/people.xlsx")

    return parser.parse_args()


if __name__ == '__main__':

    args = parse_args()

    sender = input("Type the email of the sender: ") if args.sender is None else args.sender
    username = input("Type your username and press enter: ") if args.username is None else args.username
    password = getpass.getpass(prompt="Type your password and press enter: ") if args.password is None \
        else args.password
    addres_smtp = input("Type the address of the SMTP server and press enter: ") if args.smtp_server is None \
        else args.smtp_server
    auth_protocol = input("Protocol: it can be TLS, SSL or None: ") if args.protocol is None else args.protocol

    email = EmailSender(sender, username, password, addres_smtp, auth_protocol)

    people_dft = pd.read_excel(args.input_file, index_col=0)
    people_list, invalid_links = get_conditions(people_dft)
    match = solver(people_list, invalid_links)
    saver(match)

    for _from, _to in match.items():
        email.send_mail(build_email(_from, _to), _from.email, "Secret Santa")
