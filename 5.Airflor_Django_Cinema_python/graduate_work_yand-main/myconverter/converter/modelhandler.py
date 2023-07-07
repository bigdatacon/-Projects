from pathlib import Path
import requests
from typing import Optional
from rest_framework import status
import ffmpeg
import os
import time
import argparse
import uuid


class ModelHandler:
    def __init__(self, model_url: str):
        self.model_url = model_url

    #0
    def get_model_object(self):
        """
        Ensure we can get model objects
        """
        response = requests.get(f"{self.model_url}")
        return response.json()

    #1
    def get_model_object_by_id(self, object_id : str):
        """
        Ensure we can get object by id from table
        """
        response = requests.get(f"{self.model_url}{object_id}")
        return response.json()

    #2
    def add_one_object_to_table(self, object_data: dict, file_path : Optional[str]= None):
        try:
            fd = open(file_path.encode('utf-8'), 'rb')
            response = requests.post(f'{self.model_url}', object_data, files={'file_path': fd})
            assert  response.status_code == 201, 'not add object_data in function add_one_object_to_table'
            return response.json().get('id')
        except Exception as e:
            print(f'except in add_one_object_to_table : {e.args}')
            return False

    def add_one_object_to_table_no_docker(self, object_data: dict, file_path : Optional[str]= None):
        object_data = {"resolution": "convert_video", "codec_name": "convert_videotest", 'display_aspect_ratio': 5,
                       'fps': 1,
                       'film': film_to_convert_id}

        try:
            response = requests.post("http://127.0.0.1:8000/fileupload/", object_data,
                                     files={'file_path': file_path})
            print(f' in fileupload response.status_code, response.json() : {response.status_code, response.json()}')
        except Exception as e:
            print(f'exception in create_object_for_converted_video, CAUSE : {e.args}')


    #3
    def delet_one_object_to_table(self, object_id: dict):
        try:
            response = requests.delete(f"{self.model_url}{object_id}")
            return True
        except Exception as e:
            print(f'except in delet_one_object_to_table : {e.args}')
            return False

    #4
    def add_many_object_to_table(self, object_title: Optional[str] =None, object_certificate : Optional[str] =None,  path : Optional[str]=None):
        """
        Ensure we can create many new objects in model by loading many files from path.
        """
        try:
            files = []
            for p in Path(path).rglob('*'):

                file_path = str(p.parent) + p.name
                response = requests.post(f"{self.model_url}",
                                         {'title': f"{object_title}", 'certificate': f"{object_certificate}"},
                                         files={'file_path': file_path})
            return True
        except Exception as e:
            print(f'except in add_many_object_to_table : {e.args}')
            return False

    #5
    def update_object_by_id(self, object_id : str,  object_data : dict = None,  file_path : Optional[str] = None):
        """
        Ensure we can update object by id.
        """
        try:
            if file_path:
                fd = open(file_path.encode('utf-8'), 'rb')
                response = requests.put(f"{self.model_url}{object_id}",
                                         object_data,
                                         files={'file_path': fd})
                return True
            else:
                response = requests.put(f"{self.model_url}{object_id}",
                                         object_data)

                return True

        except Exception as e:
            print(f'except in update_object_by_id : {e.args}')
            return False
        pass


    # def resize(self, output_file_name: str):
    #     stream =  ffmpeg.input(os.path.join("/usr", "src", "app", "тест.mp4"))
    #     stream = stream.filter('fps', fps=5, round = 'up').filter('scale', w=128, h=128)
    #     stream = ffmpeg.output(stream, f"{output_file_name}.mp4")
    #     ffmpeg.run(stream)

    def get_file_from_existing_object_by_id(self, object_id):
        object_data = self.get_model_object_by_id(object_id)
        file_path = object_data.get('file_path')
        file_id = object_data.get('id')
        return file_path, file_id

    def resize(self, input_file_path: str):
        file_path = input_file_path.split('/')[-1]
        output_file_path =  f"{uuid.uuid4()}"
        resp = requests.get(input_file_path)
        open(os.path.join("/usr", "src", "app", file_path), "wb").write(resp.content)
        stream =  ffmpeg.input(os.path.join("/usr", "src", "app", file_path))
        stream = stream.filter('fps', fps=5, round = 'up').filter('scale', w=128, h=128)
        stream = ffmpeg.output(stream, f"{output_file_path}.mp4")
        ffmpeg.run(stream)
        return f"{output_file_path}.mp4"

    def resize_no_docker(self, input_file_path: str):
        print(f' eto input_file_path : {input_file_path}')
        file_path = input_file_path.split('/')[-1]
        print(f'eto file_path : {file_path}')
        output_file_path =  f"{uuid.uuid4()}"
        resp = requests.get(input_file_path)
        print(f'eto resp.json() : {resp}')

        stream =  ffmpeg.input(input_file_path)
        stream = stream.filter('fps', fps=5, round = 'up').filter('scale', w=128, h=128)
        stream = ffmpeg.output(stream, f"{output_file_path}.mp4")
        ffmpeg.run(stream)
        return f"{output_file_path}.mp4"

    def create_object_for_converted_video(self, convert_video_path:str, convert_model, file_id):
        object_data = {"resolution": "convert_video", "codec_name": "convert_videotest", 'display_aspect_ratio': 5, 'fps': 1, 'film': file_id}
        file_path_new_2 = os.path.join("/usr", "src", "app", convert_video_path)

        try:
            convert_model.add_one_object_to_table(object_data, file_path_new_2)
            return True
        except Exception as e:
            print(f'exception in create_object_for_converted_video, CAUSE : {e.args}')
            return False

    def create_object_for_converted_video_no_docker(self, convert_video_path:str, convert_model, file_id):
        object_data = {"resolution": "convert_video", "codec_name": "convert_videotest", 'display_aspect_ratio': 5, 'fps': 1, 'film': file_id}
        try:
            convert_model.add_one_object_to_table_no_docker(object_data, convert_video_path)
            return True
        except Exception as e:
            print(f'exception in create_object_for_converted_video, CAUSE : {e.args}')
            return False


if __name__ == '__main__':
    # # I Вариант для докера
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--target-host", type=str, default="127.0.0.1", help="Целевой хост")
    # args = parser.parse_args()
    # api_base_url = f"http://{args.target_host}:8000/"
    # print(f' eto api_base_url : {api_base_url}')
    # #0 базовые параметры
    # time.sleep(5)
    # model = ModelHandler(f'{api_base_url}filmwork/')
    # convert_model = ModelHandler(f'{api_base_url}fileupload/')
    # #1 Cоздаю объект в модели FilmWork
    # object_data = {"title": "test2", "certificate": "test2"}
    # file_path_new_2 = os.path.join("/usr", "src", "app", "тест.mp4")
    # object_id = model.add_one_object_to_table(object_data, file_path_new_2)
    # print(f' eto object_id : {object_id}')
    #
    # #2 получаею путь до файла в докере из модели filmwork
    # file_path_to_convert, film_to_convert_id = model.get_file_from_existing_object_by_id(object_id)
    #
    # #3 отправляю полученный путь на конвертацию и получаю имя сконвертированного файла в докер волюме
    # converted_file_path = model.resize(file_path_to_convert)
    #
    # #4 заливаю видео в модели fileupload
    # model.create_object_for_converted_video(converted_file_path, convert_model, film_to_convert_id)
    # print(f' eto fileupload : {os.listdir(".")[0]}')



#########################################################################################################
    #II Вариант без докера
    {
        "id": "9a3986b7-74bb-48df-923b-6b130796d216",
        "title": "test2",
        "certificate": "test2",
        "file_path": "http://127.0.0.1:8000/film_works/%D1%82%D0%B5%D1%81%D1%82_9nvnUYc.mp4"
    }
    parser = argparse.ArgumentParser()
    parser.add_argument("--target-host", type=str, default="127.0.0.1", help="Целевой хост")
    args = parser.parse_args()
    api_base_url = f"http://{args.target_host}:8000/"
    print(f' eto api_base_url : {api_base_url}')
    #0 базовые параметры
    model = ModelHandler(f'{api_base_url}filmwork/')
    convert_model = ModelHandler(f'{api_base_url}fileupload/')
    #1 Cоздаю объект в модели FilmWork
    # file_path = 'C:\\Yand_final_sprint\\myconverter\\mysite\\files\\тест.mp4'
    file_path = 'C:\\Yand_final_sprint\\myconverter\\converter\\тест.mp4'
    object_data = {"title": "test2", "certificate": "test2"}

    fd = open(file_path.encode('utf-8'), 'rb')
    response = requests.post('http://127.0.0.1:8000/filmwork/', object_data, files={'file_path': fd})
    object_id = response.json().get('id')
    print(f' eto object_id : {object_id}')


    # object_id = model.add_one_object_to_table(object_data, file_path)


    #2 получаею путь до файла в докере из модели filmwork
    file_path_to_convert, film_to_convert_id = model.get_file_from_existing_object_by_id(object_id)
    print(f' eto  file_path_to_convert, film_to_convert_id : {file_path_to_convert, film_to_convert_id}')

    #3 отправляю полученный путь на конвертацию и получаю имя сконвертированного файла в докер волюме - не работает вне докера поэтому закоментировано сейчас
    # converted_file_path = model.resize_no_docker(file_path_to_convert)

    #4 заливаю видео в модели fileupload
    model.create_object_for_converted_video_no_docker(file_path_to_convert, convert_model, object_id)
    print(f' eto fileupload : {os.listdir(".")}')

