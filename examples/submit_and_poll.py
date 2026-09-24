import os
import time
import requests

API_KEY = os.environ["MUAPI_API_KEY"]
BASE = "https://api.muapi.ai/api/v1"
headers = {"x-api-key": API_KEY, "Content-Type": "application/json"}
payload = {'prompt': 'A close-up video of a young woman smiling gently in the rain, with raindrops glistening on her face and eyelashes. The camera focuses on the delicate details of her expression and the shimmering water droplets, while soft light softly reflects off her skin, emphasizing the rainy atmosphere.', 'image_url': 'https://example.com/replace-with-your-file'}

response = requests.post(f"{BASE}/wan2.2-image-to-video", headers=headers, json=payload, timeout=60)
response.raise_for_status()
request_id = response.json()["request_id"]
print("request_id:", request_id)

while True:
    result = requests.get(f"{BASE}/predictions/{request_id}/result", headers=headers, timeout=60)
    result.raise_for_status()
    data = result.json()
    status = data.get("status")
    if status in ("completed", "failed"):
        print(data)
        break
    time.sleep(3)
