import webbrowser as browser
# try:
#     # page_to_open = browser.open_new_tab("http://pudim.com.br")
#     page_to_open = browser.
#     open_new_tab("http://pudim.com.br")
# except ConnectionRefusedError:
#     print('No connection.')
# except ConnectionError:
#     print('Error on try connecting.')
# else:
#     print('Passed')

import urllib.request as url
try:
    print(url.urlopen("http://pudim.com.br"))
except url.URLError as erro:
    print('Connection error!')
    print(erro.__class__)
else:
    print(browser.open_new_tab("http://.com.br"))
