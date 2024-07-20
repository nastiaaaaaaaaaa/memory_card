from PyQt5.QtCore import Qt      
from PyQt5.QtWidgets import *  

app = QApplication([])

menu_win = QWidget()
menu_win.resize(400, 300)
menu_win.setWindowTitle("Меню")

txt_Question = QLineEdit('')
txt_Answer = QLineEdit('')
txt_Wrong1 = QLineEdit('')
txt_Wrong2 = QLineEdit('')
txt_Wrong3 = QLineEdit('')

layout_form = QFormLayout()

layout_form.addRow('Питання:', txt_Question)
layout_form.addRow('Правильна відповідь:', txt_Answer)
layout_form.addRow('Неправильний варіант №1:', txt_Wrong1)
layout_form.addRow('Неправильний варіант №2', txt_Wrong2)
layout_form.addRow('Неправильний варіант №3:', txt_Wrong3)

btn_back = QPushButton('Назад')
btn_add_q = QPushButton('Додати питання')
btn_clear = QPushButton('Очистити')

# Add statistics label
lbl_statistics = QLabel('')

hbtn = QHBoxLayout()         
hbtn.addWidget(btn_back)
hbtn.addWidget(btn_add_q)
hbtn.addWidget(btn_clear)

# Статистика
lbl_statistics = QLabel('Статистика:\nПравильних відповідей: 0\nЗагальна кількість спроб: 0') # надпис статистики

# Макет для основного вікна
vline = QVBoxLayout()
vline.addLayout(layout_form)
vline.addLayout(hbtn)
vline.addWidget(lbl_statistics) # додаємо його на макет

menu_win.setLayout(vline)

menu_win.setLayout(vline)
