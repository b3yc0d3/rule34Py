from rule34Py import rule34Py

client = rule34Py()

TAGS = ["neko", "sort:score", "-video"]

results = client.search(tags=TAGS)

from pathlib import Path
import requests

DOWNLOAD_LIMIT = 3

for result in results[0:DOWNLOAD_LIMIT]:
    print(f"Downloading post {result.id} ({result.image}).")
    with open(Path(result.image).name, "wb") as fp_output:
        resp = requests.get(result.image)
        resp.raise_for_status()
        fp_output.write(resp.content)
