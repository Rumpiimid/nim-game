import sys
from os import path
from PyQt5 import QtWidgets

# Добавляем путь к папке с ресурсами
sys.path.insert(0, path.join(path.dirname(path.dirname(__file__)), 'ui'))

from ui.design import Ui_MenuStackedWidget


class Window(QtWidgets.QStackedWidget, Ui_MenuStackedWidget):
    # Переменные для игры
    stones: int = 15
    current_player: int = 1
    number_of_take_stone: int = 1

    def __init__(self):
        super().__init__()  # Запускаем иницмализацию конструктора в родительском классе
        self.setupUi(self)  # То что инициализировали вызываем

        # Привязка кнопок кнопки
        self.ButtonStart.clicked.connect(self.__start_game)

        self.Select1Stone.clicked.connect(lambda: self.__select_stone(1))
        self.Select2Stone.clicked.connect(lambda: self.__select_stone(2))
        self.Select3Stone.clicked.connect(lambda: self.__select_stone(3))

        self.ButtonTakeStone.clicked.connect(self.__take_stone)

        self.__update_ui()

    def __start_game(self):
        self.setCurrentIndex(1)  # переключаемся на страницу Game

    def __select_stone(self, count):
        """Выбор количества взятия камней"""
        self.number_of_take_stone = count

    def __take_stone(self):
        """Метод для обработки взятия камней"""
        count = self.number_of_take_stone
        self.stones -= count

        self.__check_lose_and_win()

        self.current_player = 2 if self.current_player == 1 else 1

        self.__update_ui()

    def __update_ui(self):
        """Обновление текста на экране"""
        self.StoneCount.setText(str(self.stones))
        self.PlayerNumber.setText(str(self.current_player))

    def __check_lose_and_win(self):
        """Проверка на победу/поражение"""
        if self.stones <= 0:
            if self.current_player == 2:
                self.setCurrentIndex(2)  # LoseScreen
            else:
                self.setCurrentIndex(3)  # WinScreen
