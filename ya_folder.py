import requests

with open('token.txt', 'r') as file:
    token = file.read()


def ya_create_folder(token, name):
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {token}'}
    params = {"path": name, "overwrite": "true"}
    req = requests.put(url, headers=headers, params=params)
    return req.status_code


if __name__ == '__main__':
    print(ya_create_folder('token', "New_folder"))
