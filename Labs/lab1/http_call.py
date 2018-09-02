import requests

def main():
    url = "https://webhook.site/817fd522-e7fb-4916-a41f-acbc0db04371"
    
    response1 = requests.get(url)
    response2 = requests.get(url)
    response3 = requests.get(url)
    
    print(response1.headers['Date'])
    print(response2.headers['Date'])
    print(response3.headers['Date'])

if __name__ == "__main__":
    main()