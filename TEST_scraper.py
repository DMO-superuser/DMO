import mechanize

username = ""
password = ""
login_post_url = "https://fetlife.com/users/sign_in"
internal_url = "https://naturalgasintel.com/ext/resources/Data-Feed/Daily-GPI/2018/12/20181221td.txt"

browser = mechanize.Browser()
browser.open(login_post_url)
browser.select_form(nr = 1)
browser.form['Kriz'] = username
browser.form['Prodeo123'] = password
browser.submit()

response = browser.open(internal_url)
print (response.read())
