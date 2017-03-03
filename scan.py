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

import mechanize

def new_browser():

	""" Returns a new mechanize browser instance """
	browser = mechanize.Browser()
	browser.set_handle_robots(False)
	browser.set_handle_refresh(False)
	return browser

if __name__ == "__main__":
	browser = new_browser()
	browser.open(url)
	
	browser.form = list(browser.forms())[0]
	
	print "Form name:", browser.form.name, "\n"
	print browser.form
