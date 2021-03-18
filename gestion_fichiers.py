import json
import csv

def find_building_number(building_name): 
	with open("Data/Buildings_numbers.json", "r") as f : 
		data= json.load(f)
	upper_data= {k.upper():v for k,v in data.items()}
	#gestion de la casse
	building_number=upper_data[building_name.upper()]
	return building_number

