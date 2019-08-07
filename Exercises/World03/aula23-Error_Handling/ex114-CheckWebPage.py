import webbrowser as browser
import urllib.request as url


try:
    page = url.urlopen("http://ttt.com.br")
except Exception as erro:
    erro.
    print(f'Connection error! {erro.__class__}')
else:
    browser.open_new_tab("http://pudim.com.br")
