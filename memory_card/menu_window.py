from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])

menu_win = QWidget()
menu_win.resize(400, 300)

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


hbtn = QHBoxLayout()
hbtn.addWidget(btn_back)
hbtn.addWidget(btn_add_q)
hbtn.addWidget(btn_clear)


vline = QVBoxLayout()
vline.addLayout(layout_form)
vline.addLayout(hbtn)


menu_win.setLayout(vline)
# menu_win.show()
