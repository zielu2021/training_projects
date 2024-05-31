import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_parms = {
    "token": "",
    "username": "",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_parms)

print(response.text)


