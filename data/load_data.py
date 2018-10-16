import requests 

def main():
    r = requests.get('http://localhost:8000/data/load')
    print (r.status_code)

while(True):
    main()
