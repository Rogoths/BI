from script import Bi_connec
import getpass

first = True

while first:
    login = getpass.getpass("Veuillez entrer votre identifiant : ")
    password = getpass.getpass("Veuillez entrer votre mot de passe : ")
    id = Bi_connec(login, password)
    update(id)
    first = False
