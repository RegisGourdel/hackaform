# HackAForm

A python script that enables you to bias a open google form poll.

Instructions for setup
------------

- Clone the project

        git clone https://github.com/ReggioG/hackaform.git
        cd hackaform

- Install the project's runtime requirements

	pip install -r requirements.txt

- Figure out what are the questions you want to answer and what their reference numbers are :
	
	python scan.py

- Change the bias.py file accordingly.

- Run the script with arguments

	python bias.py times
	``times`` : number of times you want to spam the form

**That was it, happy hacking!**

About
-----------

* What can it bias ? (1)
  
  - Single page Google forms
  - The following controls :
    - text
    - textarea
    - select
    - radio
    - checkbox
    - list
    - date
    - hour
    - grid
    - enumerations

* What can it not bias?
  
  - Multi page forms
  - Forms that require login

* Credits to kushagra14056 for his "Google Form Spammer" which helped a lot.

Issues
------------

Please report any bugs or requests that you have using the GitHub issue tracker!

License
------------

                               Licensed under WTFPL
                   Do What the Fuck You Want to Public License
                              http://www.wtfpl.net/

                   Author is nor liable for misuse; Use carefully!

                               2017 (C) | ReggioG
