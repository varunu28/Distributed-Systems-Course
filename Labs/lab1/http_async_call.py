import asyncio
import requests

async def make_request():
    url = "https://webhook.site/817fd522-e7fb-4916-a41f-acbc0db04371"
    
    loop = asyncio.get_event_loop()

    responses = [
        loop.run_in_executor(None, requests.get, url)
        for i in range(3)
    ]

    for response in await asyncio.gather(*responses):
        print(response.headers['Date'])

loop = asyncio.get_event_loop()
loop.run_until_complete(make_request())
