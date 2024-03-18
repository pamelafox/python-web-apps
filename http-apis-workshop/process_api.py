import urllib3

# POST,
# Set Headers: Authorization: Token
resp = urllib3.request("GET",
    "https://api.zippopotam.us/us/94530") # path parameter
result = resp.json()
lat = result["places"][0]["latitude"]
lng = result["places"][0]["longitude"]

resp2 = urllib3.request("GET",
    f"https://api.sunrisesunset.io/json?lat={lat}&lng={lng}&timezone=PST&date=today")
result2 = resp2.json()
sunset = result2["results"]["sunset"]
print(f"Sunset for {lat},{lng} is {sunset}")
