from script import *
import getpass

first = True

while first:

    bank = input("Connaissez-vous votre identifiant de banque Budgea ? o/n : ")
    first = False
    ok_bank = True
    while ok_bank:
        if bank == "n":
            get_banks()
            log = True
            ok_bank = False

        elif bank == "o":
            log = True
            ok_bank = False

        else:
            print("Entrer 'o' ou 'n'")
            ok_bank = False
            first = True
            log = False

        while log:
            bank_id = input("Entrez votre identifiant de banque : ")
            login = getpass.getpass("Veuillez entrer votre identifiant : ")
            password = getpass.getpass("Veuillez entrer votre mot de passe : ")
            request_api(bank_id, login, password)
            print('FERMETURE')
            log = False
