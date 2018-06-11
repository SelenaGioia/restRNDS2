import requests

"""
Example file for calling the API
Uses the "requests" module for HTTP calls
"""

#base_url = 'http://localhost:5000'
base_url = 'http://192.168.43.224:8080'

def list_users():
    url = base_url+'/users'
    r = requests.get(url)
    return r.json()


def one_user(name):
    url = base_url + '/users/' + name
    print (url)
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        return 'fetch one user did not work'

def add_user(name, firstname, lastname):
    user = { 'name': name, 'firstname': firstname, 'lastname': lastname }
    url = base_url + '/users'
    r = requests.get(url)
    return r.json()

def read_userstatusdetails (userstatus):
    url = base_url + '/usersettings/' + userstatus
    r = requests.get(url)

def get_statuses():
    url = base_url+'/statuses'
    r = requests.get(url)
    return r.json()


def update_status(id, newstatus):
    url = base_url + '/statuses/'+ id + "/" + newstatus
    return requests.put(url)


if __name__ == '__main__':
    #all_users = list_users()
    #print(all_users)
    #print(one_user('1'))

    #settings = read_userstatusdetails ('1_1')
    #print (settings)

    statuses= get_statuses()
    #print (statuses)
    update_status('1', '1_4')
    print(one_user('1'))


