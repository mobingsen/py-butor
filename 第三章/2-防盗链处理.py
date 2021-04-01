import requests

url = "https://www.pearvideo.com/video_1725312"
contId = url.split("_")[1]

videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.05820282175266778"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    "Referer": url
}

resp = requests.get(videoStatusUrl, headers=headers)
dict = resp.json()
srcUrl = dict['videoInfo']['videos']['srcUrl']
systemTime = dict['systemTime']
srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")

with open("a.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)
