class LogMixin:
    """
    Миксин для логирования информации о создаваемом объекте.
    """
    def __init__(self, *args, **kwargs):
        print(f"Создан объект класса {self.__class__.__name__} с атрибутами: {kwargs}")
