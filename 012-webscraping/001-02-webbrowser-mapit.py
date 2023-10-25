import webbrowser, sys, pyperclip

cli_args = sys.argv

print(cli_args)

address = ''

# ['.\\001-02-webbrowser-mapit.py', 'Av', 'Mal', 'Hermes', 'da', 'Fonseca', '286', 'Bessa']
if len(cli_args) > 1:
    address = ' '.join(cli_args[1:])
    print(' '.join(cli_args[1:]))
else:
    address = pyperclip.paste()
    print(address)

openned = webbrowser.open('https://www.google.com/maps/place/' + address)

tambau = 'Rua Tambau 345 Ramos RJ'
webbrowser.open('https://www.google.com/maps/place/' + tambau)


# https://www.google.com/maps/place/Av Mal Hermes da Fonseca 286 Bessa
