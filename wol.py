#################################
#	WOL TOOLS
#Licence 3 Informatique Université d'Artois
#année 2019-2020
#Auteur : Bourdon Antoine-Alexis
#
#Ah oui le principe ... dans le teminal : guest@slinux2 > python3 wol.py 00:00:00:00:00:00 192.168.X.X
#Si le WOL est activé l'ordinateur s'allume
#Version 0.0.0.1 du 18/11/2019

#Importations des librairies de bases très pratiques :
import sys, struct, socket


broadcast = ''
wol_port = 9


#fonction qui gère tout (pour comprendre merci de lire wiki sur le WOL et ensuite la page struct, socket sur le site de python ;) )
def WakeOnLan(adresse):
    # fonction WakeOnLan qui permet d'envoyer le paquet magique. N'inclut pas encore le paramètre mot de passe si activé sur l'ordi à WOL.
    # #args : adresse (str) -> adresse mac de la cible
    # #return : None
    #on sépare les octects de l'adresse.
    add_oct = adresse.split(':')
    if len(add_oct) != 6:#mettre une bonne taille SVP
        print("NON MAIS SERIEUX, METS UNE ADRESSE MAC VALIDE MEC !!!!!!!!")
        print("Erreur : ecrire python3 wol 00:00:00:00:00:00 192.168.X.X")
        return
    hwa = struct.pack('!BBBBBB', int(add_oct[0],16), int(add_oct[1],16),int(add_oct[2],16),int(add_oct[3],16),int(add_oct[4],16),int(add_oct[5],16))
    #petit paquet magique de la mort 
    msg = b'\xff' * 6 + hwa * 16

    #Envoi du paquet magique sur le réseau port 9 (ça peut être 7 mais bon ... même le 1,2,3... fonctionne de nos jours)

    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
    #Ah oui ........ le code ne prend pas en charge l'implémentation d'un mot de passe pour le WOL
    soc.sendto(msg,(broadcast,wol_port))
    soc.close()

#fonction qui vérifie si une adresse IP est valide en IPv4 ou non.
def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.')==3
    except socket.error:
        return False
    return True

def wol(argv):
    #Cette fonction ne sert à rien .............. sauf à vous faire lire 
    #Faut déjà que quelqu'un lit ceci .... bon si personne lit ceci je peux dire nimps :D
    #Alors en ce moment je suis encore fatigué suite au dernier jeudi et vendredi.
    #Pas parce qu'il y avait TUG mais suite à la séquestration (oui ce n'était pas une séquestration XD)
    #Faut vraiment que j'arrête de dire n'importe quoi ....... Sinon vous comment allez vous ? (je vous laisse des lignes pour ecire ;) )
    #
    #
    #
    if ((len(argv)<=2) or (len(argv)>3) or not is_valid_ipv4_address(argv[2])):
        print("Erreur : ecrire python3 wol 00:00:00:00:00:00 192.168.X.X")
        print("00:00:00:00:00:00 correspond à une adresse mac")
        print("192.168.X.X correspond à une adresse de broadcast")
        return
    print ("Ah que coucou !! Je suis bob le WOL TOOL")
    WakeOnLan(argv[1])

##C'est pas très bien ça XD
wol(sys.argv)
