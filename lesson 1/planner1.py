import requests


class planner:
    r = requests.get('https://planner.thumbtack.net/accounts/login')
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.text)
