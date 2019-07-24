import requests

def get_params(key_param, value_param):
    params = {}
    if len(key_param) == 1 and key_param[0] == '':
        return None
    for index, _ in enumerate(key_param):
        try:
            params[key_param[index].strip()] = value_param[index].strip()
        except Exception:
            params[key_param[index].strip()] = ''
    if params:
        return params
    return None


def get_header(key_header, value_header):
    headers = {}
    if len(key_header) == 1 and key_header[0] == '':
        return None
    for index, _ in enumerate(key_header):
        try:
            headers[key_header[index].strip()] = value_header[index].strip()
        except Exception:
            headers[key_header[index].strip()] = ''
    if headers:
        return headers
    return None


def get_reponse(resource, body, method, header, param):
    url = 'https://www.googleapis.com/youtube/v3/' + resource + '?'
    actions = {
        'list' : requests.get,
        'insert' : requests.post,
        'update' : requests.put,
        'delete' : requests.delete,
    }
    return actions[method](url, headers=header, json=body, params=param).json()
