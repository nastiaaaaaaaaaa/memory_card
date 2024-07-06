from menu_window import *
from main_window import *

from random import choice, shuffle
from time import sleep

class Question():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3)#конструктор
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3

        self.actual = True
        self.attemts = 0
        self.correct = 0


    def got_right(self):
        self.attemts +=1
        self.correct +=1

    def got_wrong(self):
        self.attemts


q1 = Question("Банан", "banana", "banan", "anana", "banaa")#запитання та відповідь
q2 = Question("Хмара", "cloud", "loud", "clou", "clod")
q3 = Question("Кольори", "color", "color", "colr", "clor")
q4 = Question("Подушка", "pillow", "pilow", "illow", "pllow")

#списки з перемикачів кнопок та питань
radio_list =[rbtn_1, rbtn_2, rbtn_3, rbtn_4]
questions = [q1, q2, q3, q4]

def new_question():
    global cur_question
    cur_question = choice(questions) #обирає рандомне запитання
    
    lb_Question.setText(cur_question.question)
    lb_Correct.setText(cur_question.answer)

    shuffle(radio_list)

radio_list[0].setText(cur_question.answer1)
radio_list[1].setText(cur_question.answer2)
radio_list[2].setText(cur_question.answer3)
radio_list[3].setText(cur_question.answer)
#________________________________
#функція для перевірки відповідей
#________________________________
def check_results():
    for ans_btn in radio_list:
        if ans_btn.isChecked():
            if ans_btn.text() == lb_Correct.text():
                cur_question.got_right()
                lb_Result.setText("Правильно")
    else:
        cur_question.got_wrong()
        lb_Result.setText("Неправильно")
#__________________________________
#функція-оброки  кнопки "Відпочити"
#__________________________________
def rest():
    main_wind.hide()
    n = box_Minutes.value () * 60
    sleep(n)
    main_wind.show()
#__________________________
# функція для кнопки панелі
#__________________________
def show_menu():
    main_wind.hide()
    main_wind.show()

def back_menu():
    main_wind.hide()
    main_wind.show()

def clear():
    txt_Question.clear()
    txt_Answer.clear()
    txt_Wrong1.clear()
    txt_Wrong2.clear()
    txt_Wrong3.clear()

def add_question():
    newq = Question(txt_Question.text(), txt_Answer.text(), txt_Wrong1.text(), txt_Wrong2.text(), txt_Wrong3.text(),)
    questions.apped(newq)
    clear()

#функція зміни(запитаннь та надписів на кнопках)
def switch_screen():
    if btn_OK.text() == 'Відповісти':
        RadiogroupBox.hide()
        AnsGroupBox.show()
        btn_OK.setText('Наступне запитання')
    else:
        RadiogroupBox.show()
        AnsGroupBox.hide()
        btn_OK.setText('Відповісти')
                                            # скинути вибрану радіо-кнопку
        Radiogroup.setExclusive(False) # зняли обмеження, щоб можна було скинути вибір радіокнопки
        rbtn_1.setChecked(False)
        rbtn_2.setChecked(False)
        rbtn_3.setChecked(False)
        rbtn_4.setChecked(False)
        Radiogroup.setExclusive(True) # повернули обмеження, тепер лише одна радіокнопка може бути вибрана

new_question()

main_wind.show()
app.exec_()
