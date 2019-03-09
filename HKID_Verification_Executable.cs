///LastUpdate:1548939259|Powered by Simple Clock. Check it out on https://github.com/knugi0123/SimpleClock///
///Hong Kong ID Card verification///
using System;
using System.Collections.Generic;

namespace HKIDVerification
{
    class HKIDverification
    {
        static void Main()
        {
            verification(Console.ReadLine());
        }

        private static Dictionary<string, string> BasicInfo = new Dictionary<string, string>()
        {
            {"A", "issued between 1949 and 1962."},
            {"B", "issued in the urban office between 1955 and 1960."},
            {"C", "issued at the New Territories Office between 1960 and 1983."},
            {"D", "issued at the Hong Kong Island Office between 1960 and 1983."},
            {"E", "issued at the Kowloon Office between 1955 and 1969."},
            {"F", "issued at the New Territories Office between 1979 and 1983."},
            {"G", "issued at the Kowloon Office between 1967 and 1983."},
            {"H", "issued at the Hong Kong Island Office between 1979 and 1983."},
            {"J", "issued for consulate employee."},
            {"K", "issued for persons who first registered their ID cards from March 28}, 1983 to July 31, 1990."},
            {"L", "An alternate number issued between 1983 and 1999 for the failure of a computer system."},
            {"M", "issued for persons who registered their ID cards for the first time since August , 2011."},
            {"N", "Deprecated. For now, there are only one person with this character."},
            {"P", "issued for persons who first registered their identity cards from August , 1990 to December 27, 2000."},
            {"R", "issued for persons who registered their identity cards for the first time from December 28}, 2000 to July 31, 2011."},
            {"S", "issued for persons registered in Hong Kong from April , 2005." },
	    {"T", "An alternate number issued between 1983 and 1999 for the failure of a computer system."},
            {"V", "issued for persons who was issued a Document of Identity for Visa Purposes before the age of 11."},
            {"W", "issued for foreign workers and foreign domestic helpers."},
            {"WX", "issued for foreign workers and foreign domestic helpers."},
            {"X", "issued for persons who have new registration ID without Chinese name."},
            {"XA", "issued for persons who registered a new ID without Chinese name."},
            {"XB", "issued for persons who registered a new ID without Chinese name."},
            {"XC", "issued for persons who registered a new ID without Chinese name."},
            {"XD", "issued for persons who registered a new ID without Chinese name."},
            {"XE", "issued for persons who registered a new ID without Chinese name."},
            {"XG", "issued for persons who registered a new ID without Chinese name."},
            {"Y", "issued for persons registered in Hong Kong from January 1, 1989 to March 2005."},
            {"Z", "issued for persons registered in Hong Kong from January , 1980 to December 31, 1988."},
            {"default", "not in our database."}
        };

        static void verification(string id)
        {
            //Check if the value inputted by user is a vaild and if the value consist 8 character, do the following
            if (id.Length == 8)
            {
                //Declare variable
                int letterASCII, converted, productNsum, remainder;
                //Convert character to ASCII code
                letterASCII = (int)id[0];
                //Check if the value inputted by user is a vaild
                if (letterASCII >= 65 && letterASCII <= 90 || letterASCII >= 97 && letterASCII <= 122)
                {
                    //Convert lower case letter to upper case
                    if (letterASCII >= 97 && letterASCII <= 122)
                    {
                        //Set character to upper case with ASCII code
                        letterASCII = letterASCII - 32;
                    }
                    //Convert letter to number for later on calculation by ASCII - 64
                    converted = letterASCII - 64;
                    ///Operation///

                    //Calculate product and sum of user inputted ID Card number
                    productNsum = converted * 8 + Int32.Parse(id[1].ToString()) * 7 + Int32.Parse(id[2].ToString()) * 6 + Int32.Parse(id[3].ToString()) * 5 + Int32.Parse(id[4].ToString()) * 4 + Int32.Parse(id[5].ToString()) * 3 + Int32.Parse(id[6].ToString()) * 2;
                    //Find remainder of calculated product and sum
                    remainder = productNsum % 11;
                    //Default check digit is zero
                    string check = "0";
                    string check_2 = "0";
                    //If remainder is not zero, run the following code
                    if (remainder != 0)
                    {
                        //Check digit is 11 - remainder
                        check = (11 - remainder).ToString();
                        check_2 = check;
                        //If check digit is 10, show "A" as check digit
                        if (check == "10")
                        {
                            check = "A";
                            check_2 = "a";
                        }
                    }
                    //Send back the result to user
                    if (id[7].ToString() == check || id[7].ToString() == check_2)
                    {
                        Console.Write("You provided a vaild Hong Kong ID Card number.");
                        //Set default value for basic information
                        var type = BasicInfo["default"];
						//Check if user input exist in dictionary
                        if (BasicInfo.ContainsKey(id[0].ToString() + id[1].ToString()))
                        {
							//Set basic information value
                            type = BasicInfo[id[0].ToString() + id[1].ToString()];
                        }
                        Console.Write("Category of this ID Card is '" + id[0] + "', which is " + type);
                    }
                    else
                    {
                        Console.Write("You provided a incorrect Hong Kong ID Card number.");
                    }

                }
                else
                {
                    Console.Write("Please provide a complete ID Card number.");//In case, user did not provide a complete ID Card number
                }
            }
            //Check if the value inputted by user is a vaild and if the value consist 9 character, do the following
            else if (id.Length == 9)
            {
                //Declare variable
                int letterASCII_1, letterASCII_2, converted_1, converted_2, productNsum, remainder;
                //Convert character to ASCII code
                letterASCII_1 = (int)id[0];
                letterASCII_2 = (int)id[1];
                //Check if the value inputted by user is a vaild
                if ((letterASCII_1 >= 65 && letterASCII_1 <= 90 || letterASCII_1 >= 97 && letterASCII_1 <= 122) && (letterASCII_2 >= 65 && letterASCII_2 <= 90 || letterASCII_2 >= 97 && letterASCII_2 <= 122))
                {
                    //Convert lower case letter to upper case
                    if ((letterASCII_1 >= 97 && letterASCII_1 <= 122) || (letterASCII_2 >= 97 && letterASCII_2 <= 122))
                    {
                        //Set character to upper case with ASCII code
                        letterASCII_1 = letterASCII_1 - 32;
                        letterASCII_2 = letterASCII_2 - 32;
                    }
                    //Convert letter to number for later on calculation by ASCII - 64
                    converted_1 = letterASCII_1 - 64;
                    converted_2 = letterASCII_2 - 64;

                    ///Operation///

                    //Calculate product and sum of user inputted ID Card number
                    productNsum = converted_1 * 9 + converted_2 * 8 + Int32.Parse(id[2].ToString()) * 7 + Int32.Parse(id[3].ToString()) * 6 + Int32.Parse(id[4].ToString()) * 5 + Int32.Parse(id[5].ToString()) * 4 + Int32.Parse(id[6].ToString()) * 3 + Int32.Parse(id[7].ToString()) * 2;
                    //Find remainder of calculated product and sum
                    remainder = productNsum % 10;
                    //Default check digit is zero
                    string check = "0";
                    string check_2 = "0"; //In case the user enter a lower case HKID Card number
                    //If remainder is not zero, run the following code
                    if (remainder != 0)
                    {
                        //Check digit is 11 - remainder
                        check = (11 - remainder).ToString();
                        check_2 = check;
                        //If check digit is 10, show "A" as check digit
                        if (check == "10")
                        {
                            check = "A";
                            check_2 = "a";
                        }
                    }
                    //Send back the result to user
                    if (id[8].ToString() == check || id[8].ToString() == check_2)
                    {
                        Console.Write("You provided a vaild Hong Kong ID Card number.");
                        //Set default value for basic information
                        var type = BasicInfo["default"];
						//Check if user input exist in dictionary
                        if (BasicInfo.ContainsKey(id[0].ToString() + id[1].ToString()))
                        {
							//Set basic information value
                            type = BasicInfo[id[0].ToString() + id[1].ToString()];
                        }
                        Console.Write("Category of this ID Card is '" + id[0] + id[1] + "', which is " + type);
                    }
                    else
                    {
                        Console.Write("You provided a incorrect Hong Kong ID Card number.");
                    }

                }
                else
                {
                    Console.Write("Please provide a complete ID Card number.");//In case, user did not provide a complete ID Card number
                }
            }
            else
            {
                Console.Write("Please provide a complete ID Card number.");//In case, user did not provide a complete ID Card number
            }
        }
    }
}

