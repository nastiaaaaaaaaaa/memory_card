from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

main_win = QWidget()
main_win.resize(600, 500)
main_win.move(300, 300)
main_win.setWindowTitle("Питання")

#  
# Створюємо потрібні віджети (Кнопки - таймер - надпис)
# ----------------------------------------------------------
btn_Menu = QPushButton('Меню')               # кнопка повернення до основного вікна
btn_Sleep = QPushButton('Відпочити')         # кнопка прибирає вікно та повертає його після закінчення таймера
btn_OK = QPushButton('Відповісти')           # кнопка відповіді
box_Minutes = QSpinBox()                     # введення кількості хвилин
box_Minutes.setValue(3)
lb_Question = QLabel('')                     # текст питання

# ----------------------------------------------------------
#  Створюємо панель  - із варіантами відповідей - групуємо
# ----------------------------------------------------------
RadioGroupBox = QGroupBox("Варіанти відповідей:")    # Створення панелі-рамки для блоку 
RadioGroup = QButtonGroup()                         # Організація в групу віджетів (кнопок)

rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

                                    #Розміщуємо варіанти відповідей у стовпці всередині групи
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()     # вертикальні будуть усередині горизонтального
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)   #Дві відповіді в перший стовпець
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)   #Дві відповіді у другий стовпець
layout_ans3.addWidget(rbtn_4)

                                        #Тепер перемикачі прив'язані до однієї горизонтальної направляючої лінії
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

# ----------------------------------------------------------
# Створюємо панель із результатом тесту:
# ----------------------------------------------------------
AnsGroupBox = QGroupBox("Результат тесту:")
lb_Result = QLabel('')                          # Напис "правильно"/"неправильно"
lb_Correct = QLabel('')                         # Текст правильної відповіді

                                # Розміщуємо 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()                    # Можна приховати віджет.

# ----------------------------------------------------------
# Розміщуємо всі віджети у вікні:
# ----------------------------------------------------------
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

# розмінюємо на 1 шій лінії (кнопки меню,сну,і надпис)
layout_line1.addWidget(btn_Menu)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(QLabel("хвилин"))

# розмінюємо на 2 шій лінії надпис - питання
layout_line2.addWidget(lb_Question,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

# розмінюємо на 3  тій лінії Рамки
layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)

# розмінюємо на 4 тій лінії кнопку відповісти
layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK,stretch=2)
layout_line4.addStretch(1)

# 4 горизонтальні на 1 вертикальну
layout_cards = QVBoxLayout()
layout_cards.addLayout(layout_line1,stretch=1)
layout_cards.addLayout(layout_line2,stretch=2)
layout_cards.addLayout(layout_line3,stretch=8)

layout_cards.addStretch(1)
layout_cards.addLayout(layout_line4,stretch=1)
layout_cards.addStretch(1)
layout_cards.setSpacing(5) # прогалини між вмістом

main_win.setLayout(layout_cards) # передаємо на головне вікно основний макет
