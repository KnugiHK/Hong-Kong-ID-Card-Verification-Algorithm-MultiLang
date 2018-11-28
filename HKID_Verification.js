//Hong Kong ID Card verification
function HKIDverification(){
	//Library
	convertion = {
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
	};

	// Pre-Operation
	var id = document.getElementById("hkid").value;
	var productNsum, remainder, check;
	if(id.length == 8){
		letter = convertion[id[0].toUpperCase()];
		
		//Operation
		var productNsum = letter * 8 + parseInt(id[1]) * 7 + parseInt(id[2]) * 6 + parseInt(id[3]) * 5 + parseInt(id[4]) * 4 + parseInt(id[5]) * 3 + parseInt(id[6]) * 2;
		var remainder = productNsum % 11;

		if(remainder == 10){
			check = "A"
		}else if(remainder == 0){
			check = "0"
		}else{
			check = 11 - remainder
		}
			
		if(parseInt(id[7]) == check){
			alert("You provided a vaild Hong Kong ID Card number.")
		}else{
			alert("You provided a incorrect Hong Kong ID Card number.")
		}		
	}else{
		alert("Please provide a complete ID Card number.")
	}	
}
