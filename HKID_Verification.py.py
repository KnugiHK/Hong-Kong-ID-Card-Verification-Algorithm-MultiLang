#Hong Kong ID Card verification

import getpass

#Library
convertion =	{
  "A": 1,
  "B": 2,
  "C": 3,
  "D": 4,
  "E": 5,
  "F": 6,
  "G": 7,
  "H": 8,
  "I": 9,
  "J": 10,
  "K": 11,
  "L": 12,
  "M": 13,
  "N": 14,
  "O": 15,
  "P": 16,
  "Q": 17,
  "R": 18,
  "S": 19,
  "T": 20,
  "U": 21,
  "V": 22,
  "W": 23,
  "X": 24,
  "Y": 25,
  "Z": 26
}

#Pre-Operation
id = getpass.getpass('Please provide your Hong Kong ID Card number including letter and digit in bracket. (For security reason, value you typed will not be displayed):')
if len(id) == 8:
	letter = convertion[id[0].upper()]
	
	#Operation
	productNsum = letter * 8 + int(id[1]) * 7 + int(id[2]) * 6 + int(id[3]) * 5 + int(id[4]) * 4 + int(id[5]) * 3 + int(id[6]) * 2
	remainder = productNsum % 11

	if remainder == 10:
		check = "A"
	elif remainder == 0:
		check = "0"
	else:
		check = 11 - remainder

	if int(id[7]) == check:
		print("You provided a vaild Hong Kong ID Card id.")
		if id[0] == 
	else:
		print("You provided a incorrect Hong Kong ID Card id.")
else:
	print("Please provide a complete ID Card number.")

