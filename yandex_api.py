class Yan_disk:
    url = 'https://cloud-api.yandex.net/v1/'

    def __init__(self, token, folder='Folder'):
        self.token = token
        self.folder = folder
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {token}'}

    def list_files_on_disk(self):
        import requests
        method = 'disk/resources'
        params = {'path': '/', 'fields': '_embedded.items.name'}
        full_url = self.url + method
        list_files = []
        response = requests.get(full_url, headers=self.headers, params=params)
        resp = response.json()
        if response.status_code == 200:
            for i in resp['_embedded']['items']:
                list_files.append(i['name'])
        return list_files

    def creating_folder(self):
        import requests
        method = 'disk/resources'
        params = {'path': self.folder}
        full_url = self.url + method
        response = requests.put(full_url, headers=self.headers, params=params)
        return response.status_code
