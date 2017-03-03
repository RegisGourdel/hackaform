import mechanize

def new_browser():

	""" Returns a new mechanize browser instance """
	browser = mechanize.Browser()
	browser.set_handle_robots(False)
	browser.set_handle_refresh(False)
	return browser

if __name__ == "__main__":
	url = 'https://docs.google.com/forms/d/e/1FAIpQLScX5FkvJG9OpqbLpSBOR5ulbi-PY93_84SkG5NMOsOBA6YLQA/viewform'
	browser = new_browser()
	browser.open(url)
	
	browser.form = list(browser.forms())[0]
	
	print "Form name:", browser.form.name, "\n"
	print browser.form
