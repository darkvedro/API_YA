import requests


class TestYA:

    def test_ya_1(self, url_param, status_code_param):
        """ Проверка работы параметров --url и --status_code """
        response = requests.get(url_param)
        assert response.status_code == status_code_param
