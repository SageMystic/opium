import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QButtonGroup, QPushButton, QLabel

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        # Создаем объекты QRadioButton
        radio_btn1 = QRadioButton('Option 1')
        radio_btn2 = QRadioButton('Option 2')
        radio_btn3 = QRadioButton('Option 3')

        # Создаем объект QButtonGroup
        button_group = QButtonGroup(self)

        # Добавляем кнопки в группу
        button_group.addButton(radio_btn1)
        button_group.addButton(radio_btn2)
        button_group.addButton(radio_btn3)

        # Добавляем кнопки в вертикальный layout
        vbox.addWidget(radio_btn1)
        vbox.addWidget(radio_btn2)
        vbox.addWidget(radio_btn3)

        # Метка для отображения выбранной опции
        self.selected_option_label = QLabel('Выбрана опция: Нет')

        # Подключаем слот (функцию-обработчик) к событию изменения состояния кнопки
        button_group.buttonToggled.connect(self.on_radio_button_toggled)

        # Кнопка для вывода выбранной опции
        show_option_button = QPushButton('Show Selected Option')
        show_option_button.clicked.connect(self.show_selected_option)

        vbox.addWidget(self.selected_option_label)
        vbox.addWidget(show_option_button)

        # Устанавливаем вертикальный layout для основного виджета
        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('QRadioButton Example')
        self.show()

    def on_radio_button_toggled(self, button):
        # Этот метод будет вызываться при изменении состояния любой из кнопок
        if button.isChecked():
            self.selected_option_label.setText(f'Выбрана опция: {button.text()}')

    def show_selected_option(self):
        # Метод для вывода выбранной опции
        selected_button = self.findChild(QRadioButton, lambda x: x.isChecked())
        if selected_button:
            self.selected_option_label.setText(f'Выбрана опция: {selected_button.text()}')
        else:
            self.selected_option_label.setText('Выбрана опция: Нет')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    sys.exit(app.exec_())

import csv
import json

def find_unusual_houses(file_path):
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            inside = int(row['inside'])
            outside = int(row['outside'])
            if inside != outside:
                difference = abs(inside - outside)
                yield {'address': row['address'], 'difference': difference}

def save_unusual_houses(unusual_houses, file_path):
    with open(file_path, 'w', newline='') as file:
        json.dump(list(unusual_houses), file, ensure_ascii=False, indent=4)

def main():
    file_path = 'houses.csv'
    save_unusual_houses(find_unusual_houses(file_path), 'unusual.json')

if __name__ == '__main__':
    main()

