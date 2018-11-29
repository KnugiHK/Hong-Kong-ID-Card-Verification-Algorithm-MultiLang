###Hong Kong ID Card verification###

#When using console "import getpass"

def HKIDverification(id):

	###Pre-Operation###
	
	"""When using console assign the following:
	id = "str(getpass.getpass('Please provide your Hong Kong ID Card number including letter and digit in bracket such as "L5555550" (For security reason, value you typed will not be displayed):'))" """
	#Check if the value inputted by user is a vaild
	if ord(id[0]) >= 65 & ord(id[0]) <= 90:
		if len(id) == 8:
			#Convert lower case letter to upper case
			letter = id[0].upper()
			#Convert letter to number for later on calculation by ASCII - 64
			convert = ord(letter) - 64
			
			###Operation###
			
			#Calculate product and sum of user inputted ID Card number
			productNsum = convert * 8 + int(id[1]) * 7 + int(id[2]) * 6 + int(id[3]) * 5 + int(id[4]) * 4 + int(id[5]) * 3 + int(id[6]) * 2
			#Find remainder of calculated product and sum
			remainder = productNsum % 11
			#Default check digit is zero
			check = 0
			#If remainder is not zero, run the following code
			if remainder != 0:
				#Check digit is 11 - remainder
				check = 11 - remainder
				#If check digit is 10, show "A" as check digit
				if check == 10:
					check = "A"
			#Send back the result to user
			if id[7] == str(check):
				print("You provided a vaild Hong Kong ID Card number.")
			else:
				print("You provided a incorrect Hong Kong ID Card number.")
		else:
			print("Please provide a complete ID Card number.")#In case, user did not provide a complete ID Card number
	else:
		print("Please provide a complete ID Card number.")#In case, user did not provide a complete ID Card number
HKIDverification(input())