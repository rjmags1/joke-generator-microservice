from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
import requests

class RandomJokeServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/getRandomJoke":
            joke_url = "https://official-joke-api.appspot.com/random_joke"
            response = requests.get(joke_url)

            if response.status_code == 200:
                joke_data = response.json()
                filtered_joke = {
                    "setup": joke_data.get("setup", "No setup available"),
                    "punchline": joke_data.get("punchline", "No punchline available")
                }
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(filtered_joke).encode("utf-8"))
            else:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b'{"error": "Failed to fetch joke"}')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'{"error": "Not Found"}')

if __name__ == "__main__":
    server_address = ("", 8008)
    server = HTTPServer(server_address, RandomJokeServer)
    print("Serving on port 8008...")
    server.serve_forever()
