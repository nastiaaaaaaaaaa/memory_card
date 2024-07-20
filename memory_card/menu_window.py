from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import * 

app = QApplication([])

menu_win = QWidget()
menu_win.resize(400, 300)

txt_Question = QLineEdit('')        #Створює текстові поля
txt_Answer = QLineEdit('')
txt_Wrong1 = QLineEdit('')
txt_Wrong2 = QLineEdit('')
txt_Wrong3 = QLineEdit('')

layout_form = QFormLayout()

layout_form.addRow('Питання', txt_Question)
layout_form.addRow('Правильна відповідь:', txt_Answer)      #Ставить в правильному порядку текст і текстове поле
layout_form.addRow('Неправильний варіант №1:', txt_Wrong1)
layout_form.addRow('Неправильний варіант №2', txt_Wrong2)
layout_form.addRow('Неправильний варіант №3', txt_Wrong3)

btn_back = QPushButton('Назад')             #Додає кнопки повертання назад, додавання питання, очищення
btn_add_q = QPushButton('Додати питання')   
btn_clear = QPushButton('Очистити')

hbtn = QHBoxLayout()        #Вирівнює кнопки по горизонталі
hbtn.addWidget(btn_back)
hbtn.addWidget(btn_add_q)
hbtn.addWidget(btn_clear)

vline = QVBoxLayout()           #Вирівнює все по вертикалі
vline.addLayout(layout_form)
vline.addLayout(hbtn)

menu_win.setLayout(vline)
