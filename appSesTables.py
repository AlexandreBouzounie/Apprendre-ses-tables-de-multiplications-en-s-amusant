from time import *
from random import *

tempsJeu = 0
print("Comment t'appelles-tu ?")
name = input()
print('Es-tu un garçon ou une fille (Garçon = G, Fille = F) ?')
sexe = input()
while True:
    f1 = randint(1, 9)
    f2 = randint(1, 9)
    m = f1 * f2
    print('%s, combien fait %s fois %s ?' % (name, f1, f2))
    reponse = int(input())
    if reponse == m:
        tempsJeu += 1
        print("Bravo %s, la réponse est bien %s !" % (name, m))
        sleep(1.5)
        print('Encore motivé ?')
        sleep(1.25)
        if tempsJeu >= 10:
            print('Si, %s, tu ne l\'es pas, \"Spoiler !\", tu peux quitter le jeu, car tu as déjà fait %s tours. Entre R pour rester, ou Q pour quitter !' % (name, tempsJeu))
            reponseQuitterJeu = input()
            if reponseQuitterJeu == 'Q':
                break
            else:
                if sexe == 'G':
                    print('Quoi, tu es sûr ? Bon... D\'accord %s. J\'accepte !' % name)
                else:
                    print('Quoi, tu es sûre ? Bon... D\'accord %s. J\'accepte !' % name)
            sleep(3)
        if sexe == 'G':
            if tempsJeu == 1:
                print('Allez, on continue ! %s, tu es si fort ! Tu en es déjà au 1er tour !' % name)
            else:
                print('Allez, on continue ! %s, tu es si fort ! Tu en es déjà au %sème tour !' % (name, tempsJeu))
        else:
            print('Allez, on continue ! %s, tu es si forte ! Tu en es déjà au %sème tour !' % (name, tempsJeu))
        sleep(2)
    else:
        print('Oh non, %s, tu as perdu. %s fois %s fait %s. Passons au calcul suivant :' % (name, m))
        sleep(2.5)
print('Fin du jeu, %s. Merci d\'avoir joué sur les programmes de Donkey Kong Jeux-Vidéos, alias DKJV, cré par Donkey Kong Informatique (DKI). À bientôt sur nos jeux !' % name)
