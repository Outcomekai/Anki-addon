from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt.qt import *
from aqt.qt import QTimer, QWidget, QProgressBar, QVBoxLayout
import time
import sys
from aqt import gui_hooks

# Anki가 시작 후 몇 분 지났는 지 알려줌.
class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def elapsed_time(self):
        return time.time() - self.start_time

timer = Timer()

def show_elapsed_time():
    difference = timer.elapsed_time()
    showInfo(f"시작 후 지난 시간: {difference / 60:.2f} 분")

action = QAction("시작 후 지난 시간", mw)
mw.form.menuTools.addAction(action)
qconnect(action.triggered, show_elapsed_time)

#경험치 % 알려주게끔.
class experience:
    def __init__(self):
        self.card = None

    def card_current_count(self):
        self.card = mw.col.sched.counts()[1] + mw.col.sched.counts()[2]
        return self.card

    def all_card_counts(self):
        self.all_card = mw.col.cardCount()
        return self.all_card

    def calculator_experience(self):
        experience = ((self.all_card - self.card) / self.all_card)  * 100
        return experience

Experience = experience()

def calculate():
    experience = Experience.calculator_experience()
    showInfo(f"경험치: {experience:.2f} % 입니다.",)

def on_profile_event():
    timer.start()
    Experience.card_current_count()
    Experience.all_card_counts()

gui_hooks.profile_did_open.append(on_profile_event)

action2 = QAction("경험치 계산", mw)
mw.form.menuTools.addAction(action2)
qconnect(action2.triggered, calculate)
















































