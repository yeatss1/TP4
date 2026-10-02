from noeud import Noeud

n1 = Noeud("exp")

n2 = Noeud(2)
nplus = Noeud('+')
ny = Noeud('y')

n1.ajouter_enfant(n2)
n1.ajouter_enfant(nplus)
n1.ajouter_enfant(ny)

n1.affichage_polonais()

print(n1.evaluer({'y' : 1}))