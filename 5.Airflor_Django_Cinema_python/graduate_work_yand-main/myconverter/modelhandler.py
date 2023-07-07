from pathlib import Path
import requests
from typing import Optional
from rest_framework import status
import ffmpeg
import os


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
            response = requests.post(f'{self.model_ur}', object_data, files={'file_path': fd})
            assert  response.status_code == 201, 'not add object_data in function add_one_object_to_table'
            return True
        except Exception as e:
            print(f'except in add_one_object_to_table : {e.args}')
            return False


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

    def vid_resize(self, vid_path, output_path, width, overwrite=False):
        '''
        use ffmpeg to resize the input video to the width given, keeping aspect ratio
        '''
        if not (os.path.isdir(os.path.dirname(output_path))):
            raise ValueError(f'output_path directory does not exists: {os.path.dirname(output_path)}')

        if os.path.isfile(output_path) and not overwrite:
            print(f'{output_path} already exists but overwrite switch is False, nothing done.')
            return None

        input_vid = ffmpeg.input(vid_path)
        vid = (
            input_vid
                .filter('scale', width, -1)
                .output(output_path)
                .overwrite_output()
                .run()
        )
        return output_path

    def resize(self):
        stream = ffmpeg.input("C:\\Yand_final_sprint\\myconverter\\mysite\\files\\тест.mp4")
        stream = stream.filter('fps', fps=5, round = 'up').filter('scale', w=128, h=128)
        stream = ffmpeg.output(stream, "C:\\Yand_final_sprint\\myconverter\\mysite\\files\\NEW_MOVIE.mp4")
        ffmpeg.run(stream)




    #6
    def convert_video(self, vid_path, output_path, width, overwrite = False):
        # return  self.vid_resize('C:\\Yand_final_sprint\\myconverter\\mysite\\files\\тест.mp4', output_path = 'C:\\Yand_final_sprint\\myconverter\\mysite\\files\\NEW_MOVIE.mp4', width = 250)

        return  self.vid_resize(f'{vid_path}', output_path = f'{output_path}', width = width)


if __name__ == '__main__':
    # model = ModelHandler('http://127.0.0.1:8000/filmwork/')
    # print(model.resize())

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

    # model.create_object_for_converted_video(converted_file_path, convert_model, film_to_convert_id)
    # print(f' eto fileupload : {os.listdir(".")[0]}')

    # II Вариант без докера
    # {
    #     "id": "9a3986b7-74bb-48df-923b-6b130796d216",
    #     "title": "test2",
    #     "certificate": "test2",
    #     "file_path": "http://127.0.0.1:8000/film_works/%D1%82%D0%B5%D1%81%D1%82_9nvnUYc.mp4"
    # }
    # II Вариант без докера
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
    # 0 базовые параметры
    model = ModelHandler(f'{api_base_url}filmwork/')
    convert_model = ModelHandler(f'{api_base_url}fileupload/')
    # 1 Cоздаю объект в модели FilmWork
    file_path = 'C:\\Yand_final_sprint\\myconverter\\mysite\\files\\тест.mp4'
    # file_path = 'C:\\Yand_final_sprint\\myconverter\\converter\\тест.mp4'
    # file_path = 'C:\\Yand_final_sprint\\myconverter\\mysite\\files\\тест.mp4'
    file_path = 'C:\\Yand_final_sprint\\myconverter\\converter\\тест.mp4'
    object_data = {"title": "test2", "certificate": "test2"}

    fd = open(file_path.encode('utf-8'), 'rb')
    response = requests.post('http://127.0.0.1:8000/filmwork/', object_data, files={'file_path': fd})
    object_id = response.json().get('id')
    print(f' eto object_id : {object_id}')
    # object_id = model.add_one_object_to_table(object_data, file_path)

    # 2 получаею путь до файла в докере из модели filmwork
    file_path_to_convert, film_to_convert_id = model.get_file_from_existing_object_by_id(object_id)
    print(f' eto  file_path_to_convert, film_to_convert_id : {file_path_to_convert, film_to_convert_id}')

    # 3 отправляю полученный путь на конвертацию и получаю имя сконвертированного файла в докер волюме
    converted_file_path = model.resize(file_path_to_convert)
    # 3 отправляю полученный путь на конвертацию и получаю имя сконвертированного файла в докер волюме - не работает вне докера поэтому закоментировано сейчас
    # converted_file_path = model.resize_no_docker(file_path_to_convert)

    # 4 заливаю видео в модели fileupload
    model.create_object_for_converted_video(converted_file_path, convert_model, film_to_convert_id)
    print(f' eto fileupload : {os.listdir(".")[0]}')
    model.create_object_for_converted_video_no_docker(file_path_to_convert, convert_model, object_id)
    print(f' eto fileupload : {os.listdir(".")}')