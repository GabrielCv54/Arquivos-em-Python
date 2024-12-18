import requests
url_playstation = (
    "https://upload.wikimedia.org/wikipedia/commons/0/00/PlayStation_logo.svg"
)

response= requests.get(url_playstation)
with open('logo_ps.jpg','wb') as img:
    img.write(response.content)
    