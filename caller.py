import requests

"""
Example file for calling the API
Uses the "requests" module for HTTP calls
"""

base_url = 'http://localhost:5000'


def list_users():
    url = base_url+'/users'
    r = requests.get(url)
    return r.json()


def one_user(name):
    url = base_url + '/users/' + name
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        return None

def add_user(name, firstname, lastname):
    user = { 'name': name, 'firstname': firstname, 'lastname': lastname }
    url = base_url + '/users'
    r = requests.post(url, json=user)


if __name__ == '__main__':
    all_users = list_users()
    print(all_users)
    print(one_user('1'))

    '''
    print(one_user('AMR'))
    print(one_user('AE'))

    add_user('AE', 'Albert', 'Einstein')

    print(list_users())
    print(one_user('AE'))'''

