import mechanize

username = "Kriz"
password = "Prodeo123"
login_post_url = "https://fetlife.com/users/sign_in"
internal_url = "https://naturalgasintel.com/ext/resources/Data-Feed/Daily-GPI/2018/12/20181221td.txt"

browser = mechanize.Browser()
browser.open(login_post_url)
browser.select_form(nr = 0)
browser.form['username'] = USERNAME
browser.form['password'] = PASSWORD
browser.submit()
