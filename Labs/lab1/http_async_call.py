import grequests

def make_request():
    urls = [
        "https://webhook.site/aea677c7-e4e0-4f7b-a813-02ebafe3f62d",
        "https://webhook.site/aea677c7-e4e0-4f7b-a813-02ebafe3f62d",
        "https://webhook.site/aea677c7-e4e0-4f7b-a813-02ebafe3f62d"
    ]

    rs = (grequests.get(u) for u in urls)
    responses = grequests.map(rs)

    for response in responses:
        print(response.headers['Date'])

if __name__ == "__main__":
    make_request()