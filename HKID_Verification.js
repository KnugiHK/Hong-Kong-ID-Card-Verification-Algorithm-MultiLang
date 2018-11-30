///LastUpdate:1543580291///
//////Hong Kong ID Card verification//////

function HKIDverification(id){
	///Pre-Operation///
	
	//Check if the value inputted by user is a vaild and if the value consist 8 character, do the following
	if (id.length == 8){
		//Convert character to ASCII code
		letterASCII = id[0].charCodeAt()
		//Check if the value inputted by user is a vaild
		if (letterASCII >= 65 && letterASCII <= 90 || letterASCII >= 97 && letterASCII <= 122){
			//Convert lower case letter to upper case
			if (letterASCII >= 97 && letterASCII <= 122){
				//Set character to upper case with ASCII code
				letterASCII = letterASCII - 32
			}	
			//Convert letter to number for later on calculation by ASCII - 64
			converted = letterASCII - 64
			
			///Operation///
			
			//Calculate product and sum of user inputted ID Card number
			productNsum = converted * 8 + parseInt(id[1]) * 7 + parseInt(id[2]) * 6 + parseInt(id[3]) * 5 + parseInt(id[4]) * 4 + parseInt(id[5]) * 3 + parseInt(id[6]) * 2
			//Find remainder of calculated product and sum
			remainder = productNsum % 11
			//Default check digit is zero
			check = 0
			check_2 = 0
			//If remainder is not zero, run the following code
			if (remainder != 0){
				//Check digit is 11 - remainder
				check = 11 - remainder
				check_2 = check
				//If check digit is 10, show "A" as check digit
				if (check == 10){
					check = "A"
					check_2 = "a"
				}
			}
				
			//Send back the result to user
			if (id[7] == check || id[7] == check_2){
				alert("You provided a vaild Hong Kong ID Card number.")
			}else{
				alert("You provided a incorrect Hong Kong ID Card number.")
			}	
		}else{
			alert("Please provide a complete ID Card number.")//In case, user did not provide a complete ID Card number
		}	
	//Check if the value inputted by user is a vaild and if the value consist 9 character, do the following
	}else if (id.length == 9){
	//Convert character to ASCII code
		letterASCII_1 = id[0].charCodeAt()
		letterASCII_2 = id[1].charCodeAt()
		//Check if the value inputted by user is a vaild
		if ((letterASCII_1 >= 65 && letterASCII_1 <= 90 || letterASCII_1 >= 97 && letterASCII_1 <= 122) && (letterASCII_2 >= 65 && letterASCII_2 <= 90 || letterASCII_2 >= 97 && letterASCII_2 <= 122)){
			//Convert lower case letter to upper case
			if ((letterASCII_1 >= 97 && letterASCII_1 <= 122) || (letterASCII_2 >= 97 && letterASCII_2 <= 122)){
				//Set character to upper case with ASCII code
				letterASCII_1 = letterASCII_1 - 32
				letterASCII_2 = letterASCII_2 - 32
			}
			//Convert letter to number for later on calculation by ASCII - 64
			converted_1 = letterASCII_1 - 64
			converted_2 = letterASCII_2 - 64
			
			///Operation///
			
			//Calculate product and sum of user inputted ID Card number
			productNsum = converted_1 * 9 + converted_2 * 8 + parseInt(id[2]) * 7 + parseInt(id[3]) * 6 + parseInt(id[4]) * 5 + parseInt(id[5]) * 4 + parseInt(id[6]) * 3 + parseInt(id[7]) * 2
			//Find remainder of calculated product and sum
			remainder = productNsum % 10
			//Default check digit is zero
			check = 0
			check_2 = 0
			//If remainder is not zero, run the following code
			if (remainder != 0){
				//Check digit is 11 - remainder
				check = 11 - remainder
				//If check digit is 10, show "A" as check digit
				if (check == 10){
					check = "A"
					check_2 = "a"
				}	
			}
			//Send back the result to user
			if (id[8] == check || id[8] == check_2){
				alert("You provided a vaild Hong Kong ID Card number.")
			}else{
				alert("You provided a incorrect Hong Kong ID Card number.")
			}
		}else{
			alert("Please provide a complete ID Card number.")//In case, user did not provide a complete ID Card number
		}	
	}else{
		alert("Please provide a complete ID Card number.")//In case, user did not provide a complete ID Card number
	}
		
}
