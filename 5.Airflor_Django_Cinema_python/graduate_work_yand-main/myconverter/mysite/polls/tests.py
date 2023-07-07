from django.test import TestCase
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status
from .models import FilmWork, Fileupl
from pathlib import Path
import requests
import os


class ConnectionTests(APITestCase):
    def setUp(self):
        self.path = os.path.join(".", "files")
        self.row_file_path =  os.path.join(".", "files", "тест.mp4")
        self.fd = open(self.row_file_path, 'rb')
        self.url = '/filmwork/'
        self.url_long = "http://127.0.0.1:8000/filmwork/"
        self.test_filmwork  = FilmWork.objects.create(title="test_object", certificate = 'test_sertificate')
        self.test_filmwork_id = self.test_filmwork.id
        self.files = {'file_path': self.fd}

    def test_connection_questions(self):
        """
        Ensure we can get access to the object .
        """
        response = self.client.get('/filmwork/', format= 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_connection_by_id(self):
        """
        Ensure we can get object by id from table
        """
        response = self.client.get(f"{self.url}{self.test_filmwork_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)



    def test_post_delete_data(self):
        response = self.client.post(self.url, {"title": "test", "certificate": "test", "file_path": self.fd})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        id = response.json().get('id')
        response = self.client.delete(f"{self.url}{id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_post_many_files(self):
        """
        Ensure we can create many new objects in model by loading many files from path.
        """
        files = []
        i = 1
        for p in Path(self.path).rglob('*'):
            file_path = os.path.join(str(p.parent), p.name)
            response = self.client.post(self.url,
                                     {'title': f"test_api_{i}", 'certificate': f"test_api_{i}", 'file_path': open(file_path, "rb")})
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            i += 1

    def test_can_update_film(self):
        response = self.client.put(f'{self.url}{self.test_filmwork_id}/', {"title": "test_UPDATE", "certificate": "test", 'file_path': self.fd})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(f'Answer after update : {response.json().get("title")}, send to update : {"test_UPDATE"}')

    def tearDown(self):
        self.fd.close()
        self.test_filmwork.delete()


