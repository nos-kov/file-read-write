import os
import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str, disk_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        
        headers = {

            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)

        }
        files_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": disk_path, "overwrite": "True"}
        response = requests.get(files_url, headers = headers, params = params)
        response_data  = response.json()
        href = response_data["href"]

        response = requests.put(href, data=open(file_path, 'rb'))


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = os.path.join(os.getcwd(), '1.txt')
    disk_path = "2.txt"
    token = "y0_AgAAAAAZXUOIAADLWwAAAADkYcIcFk1UCK-CS0WRr8DMyjMu4obVZ1I"
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, disk_path)
    