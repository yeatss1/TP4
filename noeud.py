import numpy as np

class Noeud():
    def __init__(self, valeur, enfants = None):
        self.valeur = valeur #par exemple ”mul”, ”x”, ”sin”, 2, 3.14. La valeur peut être de type str s’il s’agit d’une 
        # variable ou d’une opération, ou de type int ou float s’il s’agit d’une constante
        self.enfants = enfants # liste des noeuds enfants
        if self.enfants is None :
            self.enfants = []

    def ajouter_enfant(self, nouvel_enfant):
        self.enfants.append(nouvel_enfant)

    def affichage_polonais(self):
        liste = [self.valeur]
        for enfant in self.enfants : 
            liste.append(enfant.valeur)
        print(liste)
        return liste

    def evaluer(self, dico): # {[y] : 1} return exp(3)
        liste = self.affichage_polonais()
        i = 0
        somme, sous, mul = 0,0,0
        while i < len(liste):
            if liste[i] == '+' :
                if liste[i+1] in dico :
                    somme = liste[i-1] + dico[liste[i+1]] 
                elif liste[i-1] in dico :
                    somme = liste[i+1] + dico[liste[i-1]] 
                else : 
                    somme = liste[i+1] + liste[i-1]
            if liste[i] == '-' :
                if liste[i+1] in dico :
                    sous = liste[i-1] - dico[liste[i+1]] 
                elif liste[i-1] in dico :
                    sous = liste[i+1] - dico[liste[i-1]] 
                else : 
                    sous = liste[i+1] - liste[i-1]
            if liste[i] == '*' :
                if liste[i+1] in dico :
                    mul = liste[i-1] * dico[liste[i+1]] 
                elif liste[i-1] in dico :
                    mul = liste[i+1] * dico[liste[i-1]] 
                else : 
                    mul = liste[i+1] * liste[i-1]
            i+=1 
        val = somme + sous + mul
        return (np.exp(val))

    def tracer(self, liste_variables):
        i = 0
        while i < len(liste_variables):