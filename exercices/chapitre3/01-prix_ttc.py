# -*- coding: UTF-8 -*-

# fichier : 01-prix_ttc.py
# auteur : David GILLARD

"""Dans une boucle while, entrer des prix d'achat HT en euros de produits (saisir 0 pour terminer).
Afficher, pour chaque prix, la valeur TTC correspondante pour un taux de TVA de 20%, calculer la 
somme TTC en cours et compter combien de produits valaient au moins 100€. Après la dernière saisie,
afficher la somme finale TTC et le nombre d'achats supérieur à 100€ TTC.
Calcul d'un prix TTC """

prixHT = float(input("Prix HT (o pour terminer) ? "))
somTTC = 0
cptSup1OO = 0
while prixHT > 0:
    prixTTC = prixHT * 1.2
    somTTC += prixTTC
    if prixTTC >= 100:
        cptSup1OO += 1
    print(f"PRIX TTC:  {prixTTC}")
    prixHT = float(input("Prix HT (o pour terminer) ? "))
    print(f"Vous avez acheté pour {somTTC} TTC d'articles.")
    print(f"Dans ceux-ci, {cptSup1OO}, valaient 100 € ou plus.")