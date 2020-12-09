from twill.commands import go, showforms, formclear, fv, submit

go('https://www.fetlife.com')
go('./widgets')
showforms()

formclear('1')
fv('1', 'name', 'Kriz')
fv('1', 'password', 'Prodeo123')
fv('1', 'confirm', 'yes')
showforms()

submit('0')
