from twill.commands import go, showforms, formclear, fv, submit

go('http://localhost:8080/')
go('./widgets')
showforms()

formclear('1')
fv('1', 'name', 'test')
fv('1', 'password', 'testpass')
fv('1', 'confirm', 'yes')
showforms()

submit('0')
