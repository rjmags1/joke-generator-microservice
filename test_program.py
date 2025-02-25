import requests

def fetch_joke():
    url = "http://localhost:8008/getRandomJoke"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            joke = response.json()
            print(f"Setup: {joke['setup']}")
            print(f"Punchline: {joke['punchline']}")
        else:
            print(f"Error: Received status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    fetch_joke()
