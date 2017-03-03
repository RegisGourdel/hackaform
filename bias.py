###############################################################################
#
#                             2015 (C) ReggioG
#
#                           Licensed under WTFPL
#               Do What the Fuck You Want to Public License
#                          http://www.wtfpl.net/
#
#              Author is nor liable for misuse; Use carefully!
#
###############################################################################
#
# You have to change the url below and the fill_form function.
#
###############################################################################

url = 'https://docs.google.com/forms/d/e/1FAIpQLScX5FkvJG9OpqbLpSBOR5ulbi-PY93_84SkG5NMOsOBA6YLQA/viewform'

import random
import string
import sys
import mechanize

def fill(control):
	""" Fills up radio, checkbox and select control with a random option """

	total = len(control.get_items())
	value_to_set = str(control.get_items()[random.randint(1,total - 1)])
	control.value = [value_to_set]

def fill_radio_control(control,parameters):
	n = len(parameters)
	#TODO

def random_text(control, length):
	""" Fills up a text control with a random string of length "length" """

	control.value = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

def new_browser():
	""" Returns a new mechanize browser instance """

	browser = mechanize.Browser()
	browser.set_handle_robots(False)
	browser.set_handle_refresh(False)

	return browser

def fill_form(form):
	""" Fills up the form : the function to be modified"""
	
	control = form.find_control("entry.327270975")
	control.readonly = False
	control.disabled = False
	control.value = "Jean-Truc"
	
	control = form.find_control("entry.1371494928")
	control.readonly = False
	control.disabled = False
	control.value = '1A'
	
	control = form.find_control("entry.755134921")
	control.readonly = False
	control.disabled = False
	control.value = "__other_option__"
	
	control = form.find_control("entry.755134921.other_option_response")
	control.readonly = False
	control.disabled = False
	control.value = "MyAnswer"

	val = "2094587968"
	for control in form.controls:
		if control.name == 'entry.2094587968':
			control.readonly = False
			control.disabled = False
			print(control.value)
			#value_to_set = str(control.get_items()[2])
			control.value = val
			val = "0"


def hcak_form(url, times = 1):
	""" Spams a google form at url "times" number of times """

	browser = new_browser()
	total = times
	while times:

		""" Open form """
		browser.open(url)

		""" The form has no name by default, but luckily for 
			us only one form on the page so simply select the 
			first one.
		"""
		browser.form = list(browser.forms())[0]

		""" Mess it up and submit"""
		fill_form(browser.form)
		browser.submit()

		times -= 1

		print "%d. Filled form" % (total - times)


if __name__ == "__main__":

	if len(sys.argv) < 2:
		print "run script as\n'python %s 'url' (in quotes) number_of_times_you_want_to_spam'\n" %(__file__)
		exit()

	times = int(sys.argv[1])
	hack_form(url, times)

