# Password Strength Calculator

password_strength.py calculates the strength of the given password using the following rules:

Requirements:
-------------
Minimum 5 characters in length (maximum 20)
Contains 3/4 of the following items:
- Uppercase Letters
- Lowercase Letters
- Numbers
- Special Symbols   **$#@!%**

Strengths:
------------
Number of Characters	+(n*4)	
Uppercase Letters		+((len-n)*2)	
Lowercase Letters		+((len-n)*2)	
Numbers	    	        +(n*4)	
Special Symbols		    +(n*6)
Requirements		    +(n*2)	

Weaknesses:
-----------
Letters Only		            -n	
Numbers Only		            -n	
Consecutive Uppercase Letters	-(n*2)	
Consecutive Lowercase Letters	-(n*2)	
Consecutive Numbers		        -(n*2)

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
