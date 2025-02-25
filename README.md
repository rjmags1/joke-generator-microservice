# joke-generator-microservice

I just used my global requests package, other dependencies part of python standard lib.

```
pip3 install requests
python3 ./server.py
```

Then navigate to `localhost:8008/getRandomJoke`, or call the `/getRandomJoke` endpoint programmatically with a GET request.

The response is json with 2 properties: `setup` and `punchline`.
