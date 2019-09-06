from http.cookies import SimpleCookie
from urllib.parse import urljoin

import requests

BASE_DOMAIN = 'https://mybook.ru/api/'
BASE_API_DOMAIN = 'https://mybook.ru/api/'


def auth(email, password):
    path = 'auth/'
    url = urljoin(BASE_API_DOMAIN, path)

    res = requests.post(url, json={'email': email, 'password': password})
    res.raise_for_status()

    set_cookie = res.headers['Set-Cookie']

    session_cookie = SimpleCookie()
    session_cookie.load(set_cookie)

    parsed_session_cookie = {k: v.value for k, v in session_cookie.items()}

    session = parsed_session_cookie['session']

    return session


def get_books(token, page=None):
    path = 'bookuserlist/'
    url = urljoin(BASE_DOMAIN, page) if page else urljoin(BASE_API_DOMAIN, path)

    headers = {'Accept': 'application/json; version=5', 'Cookie': f'session={token};'}

    res = requests.get(url, headers=headers, params={'limit': 10})
    res.raise_for_status()

    data = res.json()

    return data['objects'], data['meta']
