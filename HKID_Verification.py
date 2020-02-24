###LastUpdate:1582562573|Powered by Simple Clock. Check it out on https://github.com/knugi0123/SimpleClock###
###Hong Kong ID Card verification###

#Library
BasicInfo = {
	"A": "issued between 1949 and 1962.",
	"B": "issued in the urban office between 1955 and 1960.",
	"C": "issued at the New Territories Office between 1960 and 1983.",
	"D": "issued at the Hong Kong Island Office between 1960 and 1983.",
	"E": "issued at the Kowloon Office between 1955 and 1969.",
	"F": "issued at the New Territories Office between 1979 and 1983.",
	"G": "issued at the Kowloon Office between 1967 and 1983.",
	"H": "issued at the Hong Kong Island Office between 1979 and 1983.",
	"J": "issued for consulate employee.",
	"K": "issued for persons who first registered their ID cards from March 28, 1983 to July 31, 1990.",
	"L": "An alternate number issued between 1983 and 1999 for the failure of a computer system.",
	"M": "issued for persons who registered their ID cards for the first time since August 1, 2011.",
	"N": "Deprecated. For now, there are only one person with this character.",
	"P": "issued for persons who first registered their identity cards from August 1, 1990 to December 27, 2000.",
	"R": "issued for persons who registered their identity cards for the first time from December 28, 2000 to July 31, 2011.",
	"S": "issued for persons registered in Hong Kong from April 1, 2005.",
	"T": "An alternate number issued between 1983 and 1999 for the failure of a computer system.",
	"V": "issued for persons who was issued a Document of Identity for Visa Purposes before the age of 11.",
	"W": "issued for foreign workers and foreign domestic helpers.",
	"WX": "issued for foreign workers and foreign domestic helpers.",
	"X": "issued for persons who have new registration ID without Chinese name.",
	"XA": "issued for persons who registered a new ID without Chinese name.",
	"XB": "issued for persons who registered a new ID without Chinese name.",
	"XC": "issued for persons who registered a new ID without Chinese name.",
	"XD": "issued for persons who registered a new ID without Chinese name.",
	"XE": "issued for persons who registered a new ID without Chinese name.",
	"XG": "issued for persons who registered a new ID without Chinese name.",
	"Y": "issued for persons registered in Hong Kong from January 1, 1989 to March 2005.",
	"Z": "issued for persons registered in Hong Kong from January 1, 1980 to December 31, 1988.",
	"default": "not in our database."	
}

class InvalidLetterError(Exception):
	pass

class InvalidNumberError(Exception):
	pass

def PreOperation(id):
	lenght = len(id)
	if lenght == 8:
		id = "0" + id
		divisor = 11
	elif lenght == 9:
		divisor = 10
	else:
		raise InvalidNumberError("Number of characters of HKID should be either 8 or 9.")

	#Convert character to ASCII code
	letterASCII_1 = ord(id[0])
	letterASCII_2 = ord(id[1])
	if (letterASCII_1 >= 65 and letterASCII_1 <= 90 or letterASCII_1 >= 97 and letterASCII_1 <= 122 or letterASCII_1 == 48) and (letterASCII_2 >= 65 and letterASCII_2 <= 90 or letterASCII_2 >= 97 and letterASCII_2 <= 122):
		#Convert lower case letter to upper case
		if (letterASCII_1 >= 97 and letterASCII_1 <= 122) or (letterASCII_2 >= 97 and letterASCII_2 <= 122):
			#Set character to upper case with ASCII code
			letterASCII_1 = letterASCII_1 - 32
			letterASCII_2 = letterASCII_2 - 32
			
		#Convert letter to number for later on calculation by ASCII - 64
		if lenght == 8:
			converted_1 = 0
		elif lenght == 9:
			converted_1 = letterASCII_1 - 64
		converted_2 = letterASCII_2 - 64
		return [converted_1, converted_2], divisor, id
	else:
		raise InvalidLetterError("First character of HKID should be contain A-Z only.")

def CalCheck(remainder):
	#Default check digit is zero
	check = 0
	check_2 = 0 #In case the user enter a lower case HKID Card number
	#If remainder is not zero, run the following code
	if remainder != 0:
		#Check digit is 11 - remainder
		check = 11 - remainder
		check_2 = check
		#If check digit is 10, show "A" as check digit
		if check == 10:
			check = "A"
			check_2 = "a"
	return [check, check_2]

def HKIDverification(id):
	#Check if the value inputted by user is a vaild and if the value consist 8 character, do the following
	converted, divisor, id = PreOperation(id)

	#Calculate product and sum of user inputted ID Card number
	productNsum = converted[0] * 9 + converted[1] * 8 + int(id[2]) * 7 + int(id[3]) * 6 + int(id[4]) * 5 + int(id[5]) * 4 + int(id[6]) * 3 + int(id[7]) * 2

	#Find remainder of calculated product and sum
	remainder = productNsum % divisor
	
	check = CalCheck(remainder)
	if id[-1] == str(check[0]) or id[-1] == check[1]:
		return True
	else:
		return False

	#For CSharp and JavaScript only 
	"""
	type = BasicInfo["default"];
	if(id[0] + id[1]) in BasicInfo:
		type = BasicInfo[id[0] + id[1]];
	"""

if __name__ == "__main__":
	from getpass import getpass

	id = str(getpass('Please provide your Hong Kong ID Card number including letter and digit in bracket such as "L5555550" (For security reason, value you typed will not be displayed):'))
	
	try:
		valid = HKIDverification(id)
	except:
		print("Please provide a ID Card number with correct format.")#In case, user did not provide a complete ID Card number
	else:
		if valid:
			print("You provided a vaild Hong Kong ID Card number.")
			if len(id) == 8:
				print("Category of this ID Card is '" + id[0] + "', which is " + BasicInfo.setdefault(id[0], BasicInfo["default"]))
			elif len(id) == 9:
				print("Category of this ID Card is '" + id[0] + id[1] + "', which is " + BasicInfo.setdefault(id[0] + id[1], BasicInfo["default"]))
		else:
			print("You provided an incorrect Hong Kong ID Card number.")
