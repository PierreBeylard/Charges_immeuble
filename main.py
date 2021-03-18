# -*-coding:Latin-1 -*

from calcul_charges import *
from graphique import *
from gestion_fichiers import *
import csv
import json

building_name = input("Merci d'entrer le nom de l'immeuble (Rempart, Servandoni, Chenes Lieges, Portal, Chartrons,Begles ou Cauderan) ")
building_number= find_building_number(building_name)

#si rempart : 

print("merci d'entrer les informations concernant l'electricite ")
over ="non"
while over != "oui": 
	n=1
	elec_invoice_date = input("Merci d'entrer la date de facture au format dd/mm/yyyy ")
	elec_invoice_amount= input("Merci d'entrer le montant de ce releve ")
	over=input("merci de dire si vous avez entrer toutes les factures d'electricite format reponse (oui ou non)") 
	#Invoice(elec_invoice_amount, elec_invoice_date)
	n+=1


print("merci d'entrer les informations concernant la taxe d'ordure menagere")
year_waste_taxe=("merci d'entrer l annee concernee par cette taxe (format YYYY) ")
nb_waste_taxe= input("merci d'entrer combien de taxes ont ete recues: ")
if nb_waste_taxe == 1 : 
	waste_taxe =input("merci d'entrer le montant de la taxe d ordure menagere")
elif nb_waste_taxe==2: 
	waste_taxe21=input("merci d'entrer le montant de la premiere taxe ")
	waste_taxe22=input("merci d'entrer le montant de la deuxieme taxe ")
elif nb_waste_taxe==3 :
	waste_taxe31=input("merci d'entrer le montant de la premiere taxe ")
	waste_taxe32=input("merci d'entrer le montant de la deuxieme taxe ")
	waste_taxe33=input("merci d'entrer le montant de la troisieme taxe ")

print("merci d'entrer les informations concernant le nettoyage des communs")
year_building_cleaning=input("merci d'entrer l annee concernee par cette facture (format YYYY) ")
amount_building_cleaning=input("merci d'entrer le montant ")

print("merci d entrer les informations concernant les factures d'eau ")
overeau ="non"
while overau != "oui": 
	n=1
	water_invoice_date = input("Merci d'entrer la date de facture au format dd/mm/yyyy ")
	water_invoice_amount= input("Merci d'entrer le montant de ce releve ")
	water_consumption= input("Merci d'entrer le volume d'eau consomme indique sur le releve ")
	over=input("merci de dire si vous avez entrer toutes les factures d'electricite format reponse (oui ou non)") 
	#Invoice(elec_invoice_amount, elec_invoice_date)
	n+=1


print("merci d'entrer les informations concernant les releves de compteurs d'eau")



"""water_meter_reading_value = input("merci d'entrer la valeur releve sur le compteur d'electricite pour l'immeuble Servandoni ")
#add a exception handling if format not correct 
meter_reading_date =input("merci d'entrer la date de ce releve au format dd/mm/yyyy ")"""
os.system("pause")
