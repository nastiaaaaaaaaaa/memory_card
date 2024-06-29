from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint

app = QApplication([])

main_wind =  QWidget()
main_wind.resize(600, 500)
main_wind.move(300, 300)
main_wind.setWindowTitle('Memory card')
 
#Створемо потрібні віджети: кнопки - таймери - надписи

btn_Menu = QPushButton("Меню")
btn_Sleep = QPushButton("Відпочити")
box_Minutes = QSpinBox()
box_Minutes.setValue(30)
btn_Ok = QPushButton("Відповісти")

lb_Question = QLabel('')

#________________________________________
#Створюємо панель з варіантами відповідей
#________________________________________

RadioGroupBox = QGroupBox('Варіанти відповідей')#Рамка групи кнопок

RadioGroup =QButtonGroup()#всі кнопки в 1 віджет

rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

#__________________________________________
#Розміщення варіантів відповідей по макетах
#__________________________________________

layout_ans1 = QBoxLayout()
layout_ans2 = QVBoxLayout() # вертикальні в горизонтальні
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1) # Перші 2 відповідей на 1 вертикалінів
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2) # до горизонтальної лінії додаємо вертикальні
layout_ans1.addLayout(layout_ans3)

#_____________________________________
# На блок накладаємо лінії з віджетами
#_____________________________________
RadioGroupBox.setLayout(layout_ans1)

#_____________________________________
# Створюємо панель з результатом тесту
#_____________________________________

AnsGroupBox = QGroupBox('Результат тесту')
lb_Result = QLabel('')# надпис результату
lb_Correct = QLabel('')# правильно чи неправильно
#____________________
# Розміщуємо на рамці 
#____________________

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)

AnsGroupBox.setLayout(layout_res)# додаємо макет до рамки

#__________________________________________
#Розміщення всіх віджетів по у вікні 
#__________________________________________
layout_line1 = QBoxLayout()
layout_line2 = QBoxLayout()
layout_line3 = QBoxLayout()
layout_line4 = QBoxLayout()

# Розміщеємо на 1 ліній(кнопки, меню, сну, надпис)
layout_line1.addWidget(btn_Menu)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(QLabel('хвмлина'))

# Розміщеємо на 2 ліній
layout_line2.addWidget(lb_Question, alignment=(Qt.AlignLeft | Qt.AlignTop))

# Розміщеємо на 3 ліній
layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(RadioGroup)

# Розміщеємо на 4 ліній
layout_line4.addStretch(1)
layout_line4.addWidget(btn_Ok, stretch=2)
layout_line4.addStretch(1)

# Розміщуємо 4 горизонтальні на 1 вертикальну
layout_cards = QVBoxLayout()
layout_cards.addLayout(layout_line1, stretch=1)
layout_cards.addLayout(layout_line2, stretch=2)
layout_cards.addLayout(layout_line3, stretch=8)
layout_cards.addStretch
layout_cards.addLayout(layout_line4, stretch=1)
layout_cards.addStretch(1)
layout_cards.addSpacing(5)# проганили між вмістом

main_wind.setLayout(layout_cards)

main_wind.show()
app.exec_()