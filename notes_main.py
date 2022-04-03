from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel, QButtonGroup, QTextEdit, QListWidget, QInputDialog, QMessageBox)
import json



app = QApplication([])


notes_win = QWidget()
notes_win.resize(500, 350)
notes_win.setWindowTitle("безмозглые заметки")

list_notes = QListWidget()
list_notes_label = QLabel("список заметок")

button_note_create = QPushButton("создать заметку")
button_note_del = QPushButton("удалить заметку")
button_note_save = QPushButton("сохранить заметку")

field_text = QTextEdit()

col_1 = QVBoxLayout()
col_2 = QVBoxLayout()
layout_notes = QHBoxLayout()

col_1.addWidget(field_text)

col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)

col_2.addWidget(button_note_create)
col_2.addWidget(button_note_del)
col_2.addWidget(button_note_save)

layout_notes.addLayout(col_1)
layout_notes.addLayout(col_2)
notes_win.setLayout(layout_notes)

notes_win.show()


notes = {}
with open("notes_data.json", "w", encoding = "utf-8") as file:
        json.dump(notes, file, sort_keys = True)

def show_note():
        name = list_notes.selectedItems()[0].text()
        field_text.setText(notes[name])

list_notes.itemClicked.connect(show_note)
        
def add_note():
        note_name, result = QInputDialog.getText(notes_win, "добавить", "название заметки")
        if result and note_name != "":
                notes[note_name] = ""
                list_notes.addItem(note_name)
                print(notes)

button_note_create.clicked.connect(add_note)


def save_note():
        if list_notes.selectedItems():
            key = list_notes.selectedItems()[0].text()
            notes[key] = field_text.toPlainText()
            with open("notes_data.json", "w", encoding="utf-8") as file:
                    json.dump(notes, file, sort_keys = True)
            print(notes)
        else:
            message = QMessageBox()
            message.setText("ты че не выбрал заметку э")
            message.exec()

button_note_save.clicked.connect(save_note)

def del_note():
        if list_notes.selectedItems():
            key = list_notes.selectedItems()[0].text()
            del notes[key]
            list_notes.clear()
            field_text.clear()
            list_notes.addItems(notes)
            with open("notes_data.json", "w") as file:
                    json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        else:
            message = QMessageBox()
            message.setText("ты че не выбрал заметку э")
            message.exec()

button_note_del.clicked.connect(del_note)


with open("notes_data.json", "r", encoding = "utf-8") as file:
        notes = json.load(file)
        
list_notes.addItems(notes)


    


app.exec_()