import requests
from json import loads
from datetime import datetime


def get_params():
    params = {}
    param = input("Input param (ex : q=avengers) : ")
    while param:
        if param.count('=') == 1:
            param = param.split('=')
            params[param[0].strip()] = param[1].strip()
            param = input('> ')
        else:
            param = input('Wrong (ex : q=avengers) > ')
    return params


def write_to_file(content, file_type):
    file_name = datetime.now().strftime('%d-%m-%y_%H:%M') + '.' + file_type
    with open(file_name, 'w') as write_file:
        write_file.write(content)
    print('Your report/ouput have been written to {}'.format(file_name))


def get_file_type(reponse):
    return reponse.headers['Content-Type'].split(';')[0].split('/')[-1]


def get_url():
    url = input("Input your URL (defauls : https://www.googleapis.com/youtube/v3) : ")
    if not url:
        return 'https://www.googleapis.com/youtube/v3'
    try:
        requests.get(url)
        return url
    except Exception:
        print("Wrong URL, type agian")
        return get_url()


def get_resource():
    resource = input("Input resource of API (if any) : ")
    return resource


def get_method():
    method = input("Input your method [GET, POST, PUT, DELETE, PATCH, HEAD] (default : GET) : ")
    if not method:
        return 'GET'
    while method not in ('GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD'):
        method = input("Wrong Input : ")
    return method


def get_headers():
    headers = {}
    header = input("Input header (ex : Content-Type:application/json) : ")
    while header:
        if header.count(':') == 1:
            header = header.split(':')
            headers[header[0].strip()] = header[1].strip()
            header = input('> ')
        else:
            header = input('Wrong (ex : q=avengers) > ')
    if headers:
        return headers
    return None


def get_reponse(url):
    actions = {
        'GET' : requests.get,
        'POST' : requests.post,
        'PUT' : requests.put,
        'DELETE' : requests.delete,
        'PATCH' : requests.patch,
        'HEAD' : requests.head
    }
    return actions[get_method()](url, json=get_body(), headers=get_headers(),
                                 params=get_params())


def get_body():
    def check_body(body):
        if not body:
            return True
        try:
            loads(body)
            return True
        except Exception:
            return False
    
    body = input('Body (require json type): ')
    while not check_body(body):
        body = input('Wrong data, please input the right json type: ')
    if body:
        return body
    return None


def main():
    url = get_url().rstrip('/') + '/' + get_resource() + "?"
    print("Request URL : {}".format(url))
    reponse = get_reponse(url)
    write_to_file(reponse.content.decode(), get_file_type(reponse))
    print(reponse)


if __name__ == '__main__':
    main()