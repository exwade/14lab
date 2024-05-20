import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


class CurrencyConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Currency Converter')

        # Создаем виджеты
        self.label1 = QLabel('Enter amount in USD:')
        self.usd_input = QLineEdit()
        self.convert_button = QPushButton('Convert')
        self.result_label = QLabel('')

        # Создаем макет
        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.usd_input)
        vbox.addWidget(self.convert_button)
        vbox.addWidget(self.result_label)

        self.setLayout(vbox)

        # Подключаем обработчик событий
        self.convert_button.clicked.connect(self.convert)

        self.show()

    def convert(self):
        try:
            # Получаем введенное значение
            usd_amount = float(self.usd_input.text())

            # Предположим, что курс обмена 1 USD = 90 RUB
            rub_amount = usd_amount * 90

            # Отображаем результат
            self.result_label.setText(f'{usd_amount} USD = {rub_amount} RUB')
        except ValueError:
            # Если введено не число, показываем сообщение об ошибке
            self.result_label.setText('Please enter a valid number')


app = QApplication(sys.argv)
converter = CurrencyConverter()
sys.exit(app.exec_())
