import re
def main():
	name_list = {
Tamica Valliere,
Aisha Hoopes,
Shanel Dendy,
Nita Everly,
Kristle Stromberg,
Rodolfo Fenley,
Brooks Mayhew,
Cheree Scheller,
Kayla Allin,
Nicola Fransen,
Euna Ansari,
Alejandrina Grippo,
Delisa Redondo,
Tyrell Mister,
Wilburn Borth,
Lieselotte Horowitz,
Meaghan Cade,
Kaci Acuff,
Valda Dawson,
Margie Poirer}
	f_exp= r'^    (.*) (.*)$'
	r_exp= r'/1, /2"
	for names in name_list:
		print names
		print re.sub(f_exp,r_exp,names)
	
