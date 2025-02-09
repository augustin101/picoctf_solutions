import requests, re, time
inp = "picoCTF{(35.028309, 135.753082)(46.469391, 30.740883)(39.758949, -84.191605)(41.015137, 28.979530)(24.466667, 54.366669)(3.140853, 101.693207)_(9.005401, 38.763611)(-3.989038, -79.203560)(52.377956, 4.897070)(41.085651, -73.858467)(57.790001, -152.407227)(31.205753, 29.924526)}"

def find_city(match):
    r = requests.get("https://geocode.xyz/{},{}?json=1".format(match.group(1), match.group(2)))
    j = r.json()
    city = j["city"]
    if "Throttled! See geocode.xyz/pricing" in city :
        print("Sleeping 3s...")
        time.sleep(3)
        return find_city(match)
    if city == "Cankurtaran Mahallesi" : # Manual fix, the letter should be `I` for Istanbul
        city = "Istanbul"
    return city[0]

print(re.sub(r'\(([\d\.-]+), ([\d\.-]+)\)', find_city, inp))