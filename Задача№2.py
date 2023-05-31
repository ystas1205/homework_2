import requests


class YaUploader:
    def __init__(self, token):
        self.token = token

    def upload(self, disk_file_path, filename):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": disk_file_path}
        response = requests.get(upload_url, headers=headers, params=params)
        response_data = response.json()
        url_to_upload = response_data["href"]
        result = requests.put(url_to_upload, open(filename, 'rb'))


if __name__ == '__main__':
    TOKEN = 'y0_AgAAAAA0uLDFAADLWwAAAADj_cM7nWORvH_UQ0ixyd_abR4z_XeQ9AQ'
    uploader = YaUploader(token=TOKEN)
    uploader.upload("test/test.json", "test.json")
