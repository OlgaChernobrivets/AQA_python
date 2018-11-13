import requests

name = str(input("Input name, please: "))
print("Hello, ", name)

r = requests.get('https://planner-sandbox.dev.thumbtack.net/')
print(r.status_code)
print(r.headers['content-type'])
