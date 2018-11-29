//////Hong Kong ID Card verification//////

function HKIDverification(id){
	//////Pre-Operation//////
	
	//Convert user input to string
	id = id.toString();
	//Check if the value inputted by user is a vaild
	if(id[0].charCodeAt() >= 65 && id[0].charCodeAt() <= 90){
		if(id.length == 8){
			//Convert lower case letter to upper case
			letter = id[0].toUpperCase();
			//Convert letter to number for later on calculation by ASCII - 64
			convert = letter.charCodeAt() - 64;
			
			//////Operation//////
			
			//Calculate product and sum of user inputted ID Card number
			productNsum = convert * 8 + parseInt(id[1]) * 7 + parseInt(id[2]) * 6 + parseInt(id[3]) * 5 + parseInt(id[4]) * 4 + parseInt(id[5]) * 3 + parseInt(id[6]) * 2;
			//Find remainder of calculated product and sum
			remainder = productNsum % 11;
			//Default check digit is zero
			check = 0;
			//If remainder is not zero, run the following code
			if (remainder != 0){
				//Check digit is 11 - remainder
				check = 11 - remainder;
				//If check digit is 10, show "A" as check digit
				if(check == 10){
					check = "A";
				}
			}
			//Send back the result to user
			if(id[7] == check.toString()){
				alert("You provided a vaild Hong Kong ID Card number.");
			}else{
				alert("You provided a incorrect Hong Kong ID Card number.");
			}
				
		}else{
			alert("Please provide a complete ID Card number."); //In case, user did not provide a complete ID Card number
		} 
	}else{
		alert("Please provide a complete ID Card number."); //In case, user did not provide a complete ID Card number
	} 
}
