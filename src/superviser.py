import time
import urllib.error
import urllib.request

URL = "http://localhost:8001/health"
INTERVALLE = 10
echecs = 0

while True:
    try:
        with urllib.request.urlopen(URL, timeout=3) as reponse:
            code = reponse.status
    except (urllib.error.URLError, TimeoutError):
        code = None

    heure = time.strftime("%H:%M:%S")

    if code == 200:
        if echecs:
            print(heure, f"RÉTABLI après {echecs} échec(s)")
        echecs = 0
        print(heure, "OK")
    else:
        echecs += 1
        print(heure, f"ALERTE : /health a répondu {code} (échec n° {echecs})")

    time.sleep(INTERVALLE)