import requests

def main():
    url = "https://webhook.site/aea677c7-e4e0-4f7b-a813-02ebafe3f62d"
    
    response1 = requests.get(url)
    response2 = requests.get(url)
    response3 = requests.get(url)
    
    print(response1.headers['Date'])
    print(response2.headers['Date'])
    print(response3.headers['Date'])

if __name__ == "__main__":
    main()