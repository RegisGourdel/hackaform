###############################################################################
#
#                             2017 (C) ReggioG
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

random.seed()

def fill(form, controlName, val):
	""" Fills up a control """
	control = form.find_control(controlName)
	control.readonly = False
	control.disabled = False
	control.value = val


def pickAnswer(probas):
	""" Based on given probabilities this function pick a random answer. """
	sumProba = sum(float(x) for x in probas)
	r = random.random()
	for i in range(len(probas)):
		r = r - float(probas[i]) / sumProba
		if r <= 0:
			return i


def fill_basic_control(form, controlName, params):
	i = pickAnswer([x[1] for x in params])
	ans = params[i][0]
	other = (len(params[i]) == 3) and params[i][2]
	if not(other):
		fill(form, controlName, ans)
	else:
		fill(form, controlName, "__other_option__")
		fill(form, controlName + ".other_option_response", ans)


def fill_check_box_control(form, controlName, params, other):
	n, i = len(params), 0
	if other:
		n -= 1
	for c in form.controls:
		if c.name == controlName:
			c.readonly = False
			c.disabled = False
			r = random.random()
			if i < n and r <= params[i][1]:
				c.value = params[i][0]
			elif i == n and other and r < params[i][1]:
				c.value = "__other_option__"
				fill(form, controlName + ".other_option_response", params[i][0])
			i += 1


def fill_date_control(form, controlName, params):
	i = pickAnswer([x[3] for x in params])
	fill(form, controlName + "_day", params[i][0])
	fill(form, controlName + "_month", params[i][1])
	fill(form, controlName + "_year", params[i][2])

def fill_hour_control(form, controlName, params):
	i = pickAnswer([x[2] for x in params])
	fill(form, controlName + "_hour", params[i][0])
	fill(form, controlName + "_minute", params[i][1])


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
	
	# Radio-select question:
	# Change the list below. For each possible answer you have to specify :
	# First element must be the name of the option, as written in the form.
	# Second element is proportionnal to the probability of the answer.
	# Third element is False if the answer belongs to the list of predefined options and True if it is an other answer.
	params = [ ["Option 1", 1.0, False], ["Option 2", 2.0, False], ["Option 3", 3.0, False], ["Option 4", 4.0, True] ]
	# Change the name of the question that you read using scan.py
	fill_basic_control(form, "entry.1718133627", params)


	# Check-box question:
	# Change the list below. For each possible answer you have to specify :
	# First element must be the name of the option, as written in the form.
	# Second element is proportionnal to the probability of the answer.
	params = [ ["Option 1", 0.1], ["Option 2", 0.5], ["Option 3", 0.9], ["Option 4", 0.5] ]
	# Change the name of the question that you read using scan.py
	# You have to give informations about every option in the form.
	# Last argument is True if you want to give a non-predefined answer, which will be the last item of parms, and False if you don't.
	fill_check_box_control(form, "entry.1215049635", params, True)
	
	
	# List question:
	# It works like the radio-select question without the possibility of additional answers.
	params = [ ["Option 2", 1.0], ["Option 1", 2.0], ["Option 5", 3.0] ]
	fill_basic_control(form, "entry.997826028", params)
	
	
	# Enumerate question:
	# Works like the previous one.
	params = [ ["1", 1.0], ["2", 2.0], ["3", 3.0], ["4", 4.0], ["5", 5.0] ]
	fill_basic_control(form, "entry.743831183", params)
	
	
	# Grid question:
	# Works like the previous one, line by line.
	params = [ ["Option 1", 1.0], ["Colonne 2", 2.0], ["Colonne 3", 3.0] ]
	fill_basic_control(form, "entry.1035037726", params)
	params = [ ["Option 1", 5.0], ["Colonne 2", 2.0], ["Colonne 3", 1.0] ]
	fill_basic_control(form, "entry.1820175584", params)
	
	
	# Date question
	params = [  ["01", "01", "2017", 1.0],
				["15", "02", "2017", 1.0],
				["20", "03", "2017", 1.0] ]
	fill_date_control(form, "entry.711404992", params)
	
	
	# Hour question
	params = [  ["01", "01", 1.0],
				["15", "34", 1.0],
				["20", "55", 1.0] ]
	fill_hour_control(form, "entry.157377019", params)


def hack_form(url, times = 1):
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
		print "run script as\n'python number_of_times_you_want_to_spam'\n" %(__file__)
		exit()

	times = int(sys.argv[1])
	hack_form(url, times)
