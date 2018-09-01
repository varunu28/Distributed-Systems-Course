import requests

def make_request():
    url = "https://webhook.site/817fd522-e7fb-4916-a41f-acbc0db04371"
    
    response = requests.get(url)
    print(response.headers['Date'])

def main():
    for i in range(3):
        make_request()

if __name__ == "__main__":
    main()