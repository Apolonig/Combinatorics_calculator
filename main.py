import sys
import math

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QDialog

from other_windows.start_ui import Ui_Dialog_start
from other_windows.oder import Ui_Dialog_oder
from other_windows.Choose_everything_el import Ui_Dialog_choose
from other_windows.Repeat import Ui_Dialog_repeat
from other_windows.Repeat_right import Ui_Dialog_repeat_right
from other_windows.Repeat_left_1 import Ui_Dialog_repeat_left_1
from other_windows.Permutations_ui import Ui_Dialog_permutations
from other_windows.Permutations_repetitions_ui import Ui_Dialog_Permutations_repetitions
from other_windows.Placements_ui import Ui_Dialog_placement
from other_windows.Placements_repetitions_ui import Ui_Dialog_placements_repetitions
from other_windows.Combination_ui import Ui_Dialog_Combination
from other_windows.Combination_repetitions_ui import Ui_Dialog_combination_repetitions
from other_windows.Pre_permutations_repetitions import Ui_Dialog_pre_permutation


class Start(QDialog):
    def __init__(self):
        super(Start, self).__init__()
        self.ui = Ui_Dialog_start()
        self.ui.setupUi(self)

        self.ui.next_step_button.clicked.connect(self.start)

    def answer_permutations(self):
        n = self.ui.nn.text()
        return math.factorial(int(n))

    def answer_placements_repetitions(self):
        n = self.ui.nn.text()
        m = self.ui.mm.text()
        return int(n) ** int(m)

    def answer_placements(self):
        n = self.ui.nn.text()
        m = self.ui.mm.text()
        return math.factorial(int(n)) // math.factorial(int(n) - int(m))

    def answer_combination(self):
        n = self.ui.nn.text()
        m = self.ui.mm.text()
        return math.factorial(int(n)) // (math.factorial(int(m)) * math.factorial(int(n) - int(m)))

    def answer_combination_repetitions(self):
        n = self.ui.nn.text()
        m = self.ui.mm.text()
        return math.factorial(int(n) + int(m) - 1) // (math.factorial(int(m)) * math.factorial(int(n) - 1))

    def start(self):
        oder = Oder()
        widget.addWidget(oder)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Oder(QDialog):
    def __init__(self):
        super(Oder, self).__init__()
        self.ui = Ui_Dialog_oder()
        self.ui.setupUi(self)

        self.ui.oder_yes.clicked.connect(self.start_chooser)
        self.ui.oder_no.clicked.connect(self.start_repeat_left)

    def start_chooser(self):
        choose = Choose_everything_el()
        widget.addWidget(choose)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def start_repeat_left(self):
        repeat = Repeat_left()
        widget.addWidget(repeat)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Repeat_left(QDialog):
    def __init__(self):
        super(Repeat_left, self).__init__()
        self.ui = Ui_Dialog_repeat()
        self.ui.setupUi(self)

        self.ui.repeat_yes.clicked.connect(self.start_combination_repetitions)
        self.ui.repeat_no.clicked.connect(self.start_combination)

    def start_combination(self):
        combination = Combination()
        widget.addWidget(combination)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def start_combination_repetitions(self):
        combination_repetitions = Combination_repetitions()
        widget.addWidget(combination_repetitions)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Choose_everything_el(QDialog):
    def __init__(self):
        super(Choose_everything_el, self).__init__()
        self.ui = Ui_Dialog_choose()
        self.ui.setupUi(self)
        self.ui.choose_everything_el_yes.clicked.connect(
            self.start_repeat_right)
        self.ui.choose_everything_el_no.clicked.connect(self.start_left_1)

    def start_repeat_right(self):
        repeat_right = Repeat_right()
        widget.addWidget(repeat_right)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def start_left_1(self):
        start_left_1 = Repeat_left_1()
        widget.addWidget(start_left_1)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Repeat_right(QDialog):
    def __init__(self):
        super(Repeat_right, self).__init__()
        self.ui = Ui_Dialog_repeat_right()
        self.ui.setupUi(self)

        self.ui.repeat_right_yes.clicked.connect(self.start_pre_permutation)
        self.ui.repeat_right_no.clicked.connect(self.start_permutations)

    def start_pre_permutation(self):
        start_pre_permutation = Pre_permutation()
        widget.addWidget(start_pre_permutation)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def start_permutations(self):
        start_permutations = Permutations()
        widget.addWidget(start_permutations)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Repeat_left_1(QDialog):
    def __init__(self):
        super(Repeat_left_1, self).__init__()
        self.ui = Ui_Dialog_repeat_left_1()
        self.ui.setupUi(self)

        self.ui.repeat_left_1_yes.clicked.connect(
            self.start_placements_repetitions)
        self.ui.repeat_left_1_no.clicked.connect(self.start_placements)

    def start_placements(self):
        combination = Placements()
        widget.addWidget(combination)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def start_placements_repetitions(self):
        combination_repetitions = Placements_repetitions()
        widget.addWidget(combination_repetitions)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Pre_permutation(QDialog):
    def __init__(self):
        super(Pre_permutation, self).__init__()
        self.uii = Ui_Dialog_pre_permutation()
        self.uii.setupUi(self)

        self.uii.counting_button.clicked.connect(
            self.start_permutations_repetitions)

    def start_permutations_repetitions(self):
        m1_text = self.uii.m1.text().strip()
        n_text = self.uii.nn.text().strip()
        m2_text = self.uii.m2.text().strip()
        m3_text = self.uii.m3.text().strip()
        m4_text = self.uii.m4.text().strip()
        m5_text = self.uii.m5.text().strip()
        m6_text = self.uii.m6.text().strip()
        m7_text = self.uii.m7.text().strip()
        m8_text = self.uii.m8.text().strip()
        m9_text = self.uii.m9.text().strip()
        m10_text = self.uii.m10.text().strip()

        # if m1_text:
        #     try:
        #         m1 = int(m1_text)
        #         answer = math.factorial(m1)

        #         permutations_repetitions = Permutations_repetitions(answer)
        #         widget.addWidget(permutations_repetitions)
        #         widget.setCurrentIndex(widget.currentIndex() + 1)

        #     except ValueError:
        #         print("Неверный ввод для m1. Пожалуйста, введите целое число.")
        # else:
        #     print("Пожалуйста, введите значение для m1.")
        m1 = int(m1_text)
        m2 = int(m2_text)
        m3 = int(m3_text)
        m4 = int(m4_text)
        m5 = int(m5_text)
        m6 = int(m6_text)
        m7 = int(m7_text)
        m8 = int(m8_text)
        m9 = int(m9_text)
        m10 = int(m10_text)
        n = int(n_text)
        answer = math.factorial(n) // (math.factorial(m1) * math.factorial(m2) * math.factorial(m3) * math.factorial(m4) * math.factorial(
            m5) * math.factorial(m6) * math.factorial(m7) * math.factorial(m8) * math.factorial(m9) * math.factorial(m10))

        permutations_repetitions = Permutations_repetitions(answer)
        widget.addWidget(permutations_repetitions)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Permutations_repetitions(QDialog):
    def __init__(self, answer):
        super(Permutations_repetitions, self).__init__()
        self.ui = Ui_Dialog_Permutations_repetitions()
        self.ui.setupUi(self)

        self.ui.Permutations_repetitions_answer.setText(str(answer))


class Permutations(QDialog):
    def __init__(self):
        super(Permutations, self).__init__()
        self.ui = Ui_Dialog_permutations()
        self.ui.setupUi(self)

        answer_per = main_window.answer_permutations()
        self.ui.Permutations_answer.setText(str(answer_per))


class Combination(QDialog):
    def __init__(self):
        super(Combination, self).__init__()
        self.ui = Ui_Dialog_Combination()
        self.ui.setupUi(self)

        answer_com = main_window.answer_combination()
        self.ui.Combination_answer.setText(str(answer_com))


class Combination_repetitions(QDialog):
    def __init__(self):
        super(Combination_repetitions, self).__init__()
        self.ui = Ui_Dialog_combination_repetitions()
        self.ui.setupUi(self)

        answer_com_rep = main_window.answer_combination_repetitions()
        self.ui.Combination_repetitions_answer.setText(str(answer_com_rep))


class Placements(QDialog):
    def __init__(self):
        super(Placements, self).__init__()
        self.ui = Ui_Dialog_placement()
        self.ui.setupUi(self)

        answer_pl = main_window.answer_placements()
        self.ui.Placements_answer.setText(str(answer_pl))


class Placements_repetitions(QDialog):
    def __init__(self):
        super(Placements_repetitions, self).__init__()
        self.ui = Ui_Dialog_placements_repetitions()
        self.ui.setupUi(self)

        answer_pl_rep = main_window.answer_placements_repetitions()
        self.ui.Placements_repetitions_answer.setText(str(answer_pl_rep))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = Start()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(main_window)
    widget.setFixedWidth(750)
    widget.setFixedHeight(620)
    widget.show()

    sys.exit(app.exec())
