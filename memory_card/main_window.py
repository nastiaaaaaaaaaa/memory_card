from main_window import *
from menu_window import *

from random import choice, shuffle
from time import sleep
 
wins = [main_win, menu_win]

for win in wins:
    win.setStyleSheet('''
                      color:yellow
                      backround-color:lightblue
                      font-size: 20xp;
                      border: 0.5px solid blue:
                      ''')

lb_Result.setStyleSheet('margin: 20px;')

app = QApplication([])

class Question():
    def __init__(self,question,answer,wrong_answer1,wrong_answer2,wrong_answer3): # конструктор
        self.question = question # питання
        self.answer = answer # відповідь
        self.wrong_answer1 = wrong_answer1 # неправильні відповіді 1 - 3
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        
        self.actual = True # чи актуальне питання
        self.attempts = 0 # спроби
        self.correct = 0 # правильно чи ні

    def got_right(self):
        # змінює статистику, отримавши правильну відповідь
        self.attempts += 1
        self.correct += 1
    
    def got_wrong(self):
        # змінює статистику, отримавши неправильну відповідь
        self.attempts += 1

# питання
q1 = Question('Які зорі мають найвищу температуру', 'сині', 'жовті', 'білі', 'червоні')
q2 = Question('Які зорі мають найнижчу температуру поверхні', 'білі', 'чорні', 'блакитні', 'червоні')
q3 = Question('Які холодні зорі мають колір', 'червоні', 'білі', "жовті", "чорні")
q4 = Question('Який місяць має тільки 28 днів', 'Лютий', 'Березень', 'Квітень', 'всі мають')
q5 = Question('Скільки в Ураїні були президенти', '6', '8', '7', '5')
q6 = Question('Перший президент України', 'Леонід Кравчук', 'Володимер Зеленський', 'Віктор Ющенко', 'Віктор Янукович')
q7 = Question('Найвища гора?', 'Еверест', 'Говерла', 'Лхоцзе', 'Чогорі')


# списки з кнопками та питаннями
radio_list = [rbtn1, rbtn2, rbtn3, rbtn4] # кнопки
questions = [q1, q2, q3, q4, q5, q6, q6, q7] # питання
# задаємо питання

def new_question():
    global current_question
    current_question = choice(questions) # питання

    lb_Question.setText(current_question.question) # беремо питання та правильну відповідь
    lb_Correct.setText(current_question.answer)

    shuffle(radio_list) # перемішуємо кнопки

    radio_list[0].setText(current_question.wrong_answer1) # задаємо кнопкам варіанти відповідей
    radio_list[1].setText(current_question.wrong_answer2)
    radio_list[2].setText(current_question.wrong_answer3)
    radio_list[3].setText(current_question.answer)
new_question()
# перевірка відповіді
def check_result():
    for ans_btn in radio_list: # отримуємо кнопки з списка
        if ans_btn.isChecked(): # якщо кнопку нажали
            if ans_btn.text() == lb_Correct.text(): # перевіряємо якщо текст кнопки правильний
                current_question.got_right()
                lb_Result.setText('Правильно') # правильно
                break
    else:
        current_question.got_wrong()
        lb_Result.setText('Неправильно') # неправильно
# відпочити
def rest(): 
    main_wind.hide() # прячемо головне вікно
    n = box_Minutes.value() # беремо встановлене число
    sleep(n) # відпочинок
    main_wind.show() # показуємо головне вікно

def show_menu(): # показати меню
    menu_wind.show() # показуємо меню
    main_wind.hide() # ховаємо головне вікно

def back_menu(): # показати головне вікно
    menu_wind.hide() # прячемо меню
    main_wind.show() # показуємо головне вікно

def clear(): 
    # очищуємо питання
    txt_Question.clear()
    txt_Answer.clear()
    txt_Wrong1.clear()
    txt_Wrong2.clear()
    txt_Wrong3.clear()

def addQuestion(): # додаємо питання
    newq = Question(txt_Question.text(), txt_Answer.text(), txt_Wrong1.text(), txt_Wrong2.text(), txt_Wrong3.text()) # задаємо варіанти відповіді
    questions.append(newq) # додаємо питання в список
    clear() # очищуємо

def switch_screen():
    if btn_OK.text() == 'Відповісти':
        check_result()
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_OK.setText('Наступне питання')
    else:
        new_question()
        RadioGroupBox.show()
        AnsGroupBox.hide()
        btn_OK.setText('Відповісти')

        RadioGroup.setExclusive(False)
        rbtn1.setChecked(False)
        rbtn2.setChecked(False)
        rbtn3.setChecked(False)
        rbtn4.setChecked(False)

# Підключення виклику функції до кнопок

btn_Menu.clicked.connect(show_menu)
btn_back.clicked.connect(back_menu)
btn_clear.clicked.connect(clear)
btn_Sleep.clicked.connect(rest)
btn_OK.clicked.connect(switch_screen)
btn_add_q.clicked.connect(addQuestion)

main_wind.show()
app.exec_()
