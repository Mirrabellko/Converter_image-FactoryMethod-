from __future__ import annotations
from abc import ABC, abstractmethod

from PIL import Image


class IConverterCreator(ABC):
    """
    Интерфейс для фабрики конвертеров.
    """
    @abstractmethod
    def create_converter() ->IImageConverter: pass


class IImageConverter(ABC):
    """
    Интерфейс для конкретного конвертера, принимает в себя пути к файлам
    """

    @abstractmethod
    def convert(): pass


class PngToJpgConverter(IImageConverter):
    """
    Конвертер Png в Jpg, возвращает объект типа JpgProduct
    """

    def __init__(self, path: str) -> None:
        super().__init__()
        self.path = path
        

    def convert(self):
        image = Image.open(self.path)
        name = self.path[:-4]
        print(f"Я сохраняю файл с именем {name}")
        image.save(f'{name}.jpg', format='jpg')


class JpgToPngConverter(IImageConverter):
    """
    Конвертер Jpg в Png, возвращает объект типа PngProduct
    """

    def __init__(self, path: str) -> None:
        super().__init__()
        self.path = path
        

    def convert(self):
        image = Image.open(self.path)
        name = self.path[:-4]
        print(f"Я сохраняю файл с именем {name}")
        image.save(f'{name}.png', format='png')



class Application(IConverterCreator):

    TOPNG = 'jpg'
    TOJPG = 'png'

    def __init__(self) -> None:

        self.path = None
        self.type = None

        
    def start_app(self):

        print("Welcome to EasyConverter!")
        print("You can convert JPG to PNG or PNG to JPG")
        self.path = input("Please enter path to the image: ")
        print(f"Путь был записан: {self.path}")

    def create_converter(self):
        print(f"Это тип {self.path[-3:]}")

        if self.path[-3:] == self.TOPNG:

            print("Определилось jpg")
            self.type = self.TOPNG
            
            creator = JpgToPngConverter(self.path).convert()
            
        if self.path[-3:] == self.TOJPG:

            print("Определилось png")
            self.type = self.TOJPG
            
            creator = JpgToPngConverter(self.path).convert()
        
        return f"Your image was convertered to {self.type}"
    

if __name__ == "__main__":

    app = Application()
    app.start_app()
    product = app.create_converter()
    

# BRAIN_HEALTH_419329DF.jpg