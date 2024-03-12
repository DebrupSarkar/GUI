from loginPage import LoginPage
from registerationForm import RegisterationForm

login_page = LoginPage()
if login_page.RETURNVALUE == 'FNR':
    registeration_form = RegisterationForm()
elif login_page.RETURNVALUE == 'LOGIN':
    print('Hi debrup')
