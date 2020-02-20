from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

import os
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()
        self.editor = QPlainTextEdit()  # Could also use a QTextEdit and set self.editor.setAcceptRichText(False)

        # Setup the QTextEdit editor configuration
        fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedfont.setPointSize(12)
        self.editor.setFont(fixedfont)

        # self.path holds the path of the currently open file.
        # If none, we haven't got a file open yet (or creating new).
        self.path = None
        self.txt_changed_check = 0

        layout.addWidget(self.editor)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        # file menu & toolbar
        file_toolbar = QToolBar("File")
        file_toolbar.setIconSize(QSize(14, 14))
        self.addToolBar(file_toolbar)

        file_menu = self.menuBar().addMenu("&File")

        new_file_action = QAction(QIcon(os.path.join('images', 'new_file.png')), "New file", self)
        new_file_action.setStatusTip("Create new text file")
        new_file_action.triggered.connect(self.new_file)
        file_menu.addAction(new_file_action)
        file_toolbar.addAction(new_file_action)

        open_file_action = QAction(QIcon(os.path.join('images', 'blue-folder-open-document.png')), "Open file...", self)
        open_file_action.setStatusTip("Open file")
        open_file_action.triggered.connect(self.file_open)
        file_menu.addAction(open_file_action)
        file_toolbar.addAction(open_file_action)

        save_file_action = QAction(QIcon(os.path.join('images', 'disk.png')), "Save", self)
        save_file_action.setStatusTip("Save current page")
        save_file_action.triggered.connect(self.file_save)
        file_menu.addAction(save_file_action)
        file_toolbar.addAction(save_file_action)

        saveas_file_action = QAction(QIcon(os.path.join('images', 'disk--pencil.png')), "Save As...", self)
        saveas_file_action.setStatusTip("Save current page to specified file")
        saveas_file_action.triggered.connect(self.file_saveas)
        file_menu.addAction(saveas_file_action)
        file_toolbar.addAction(saveas_file_action)

        print_action = QAction(QIcon(os.path.join('images', 'printer.png')), "Print...", self)
        print_action.setStatusTip("Print current page")
        print_action.triggered.connect(self.file_print)
        file_menu.addAction(print_action)
        file_toolbar.addAction(print_action)

        # edit menu
        edit_toolbar = QToolBar("Edit")
        edit_toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(edit_toolbar)

        edit_menu = self.menuBar().addMenu("&Edit")

        undo_action = QAction(QIcon(os.path.join('images', 'arrow-curve-180-left.png')), "Undo", self)
        undo_action.setStatusTip("Undo last change")
        undo_action.triggered.connect(self.editor.undo)
        edit_menu.addAction(undo_action)

        redo_action = QAction(QIcon(os.path.join('images', 'arrow-curve.png')), "Redo", self)
        redo_action.setStatusTip("Redo last change")
        redo_action.triggered.connect(self.editor.redo)
        edit_toolbar.addAction(redo_action)
        edit_menu.addAction(redo_action)

        edit_menu.addSeparator()

        cut_action = QAction(QIcon(os.path.join('images', 'scissors.png')), "Cut", self)
        cut_action.setStatusTip("Cut selected text")
        cut_action.triggered.connect(self.editor.cut)
        edit_toolbar.addAction(cut_action)
        edit_menu.addAction(cut_action)

        copy_action = QAction(QIcon(os.path.join('images', 'document-copy.png')), "Copy", self)
        copy_action.setStatusTip("Copy selected text")
        copy_action.triggered.connect(self.editor.copy)
        edit_toolbar.addAction(copy_action)
        edit_menu.addAction(copy_action)

        paste_action = QAction(QIcon(os.path.join('images', 'clipboard-paste-document-text.png')), "Paste", self)
        paste_action.setStatusTip("Paste from clipboard")
        paste_action.triggered.connect(self.editor.paste)
        edit_toolbar.addAction(paste_action)
        edit_menu.addAction(paste_action)

        select_action = QAction(QIcon(os.path.join('images', 'selection-input.png')), "Select all", self)
        select_action.setStatusTip("Select all text")
        select_action.triggered.connect(self.editor.selectAll)
        edit_menu.addAction(select_action)

        clear_action = QAction("Clear", self)
        clear_action.setStatusTip("Clear selelcted text")
        clear_action.triggered.connect(self.editor.clear)
        edit_menu.addAction(clear_action)

        clear_all_action = QAction("Clear All", self)
        clear_all_action.setStatusTip("Clear all text")
        clear_all_action.triggered.connect(self.clear_all)
        edit_menu.addAction(clear_all_action)

        edit_menu.addSeparator()

        wrap_action = QAction(QIcon(os.path.join('images', 'arrow-continue.png')), "Wrap text to window", self)
        wrap_action.setStatusTip("Toggle wrap text to window")
        wrap_action.setCheckable(True)
        wrap_action.setChecked(True)
        wrap_action.triggered.connect(self.edit_toggle_wrap)
        edit_menu.addAction(wrap_action)

        self.editor.textChanged.connect(self.txt_changed)

        self.update_title()

        self.show()

    def dialog_critical(self, s):
        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()

    def file_open(self):
        self.editor.modificationChanged.connect(self.modification_changed)
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text documents (*.txt);All files (*.*)")

        if path:
            try:
                with open(path, 'r') as f:
                    text = f.read()

            except Exception as e:
                self.dialog_critical(str(e))

            else:
                self.path = path
                self.editor.setPlainText(text)
                self.update_title()

    def file_save(self):
        if self.path is None:
            # If we do not have a path, we need to use Save As.
            return self.file_saveas()

        self._save_to_path(self.path)

    def file_saveas(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Text documents (*.txt);All files (*.*)")

        if not path:
            # If dialog is cancelled, will return ''
            return

        self._save_to_path(path)

    def _save_to_path(self, path):
        text = self.editor.toPlainText()
        try:
            with open(path, 'w') as f:
                f.write(text)

        except Exception as e:
            self.dialog_critical(str(e))

        else:
            self.path = path
            self.update_title()
            self.file_save_check = 1

    def file_print(self):
        dlg = QPrintDialog()
        if dlg.exec_():
            self.editor.print_(dlg.printer())

    def update_title(self):
        self.setWindowTitle("%s - No2Pads" % (os.path.basename(self.path) if self.path else "Untitled"))

    def edit_toggle_wrap(self):
        self.editor.setLineWrapMode(1 if self.editor.lineWrapMode() == 0 else 0)

    def clear_all(self):
        self.editor.selectAll()
        self.editor.clear()

    def new_file(self):
        txt_length = self.editor.toPlainText()

        if self.txt_changed_check == 1 and len(txt_length) > 0:
            self.file_saveas()

        self.path = None
        self.clear_all()
        self.update_title()
        self.txt_changed_check = 0

    def txt_changed(self):
        self.txt_changed_check = 1
        print("txt_changed_check: ", self.txt_changed_check)

    def modification_changed(self):
        self.modification_check = 1
        print("modification_check: ", self.modification_check)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("No2Pads")

    window = MainWindow()
    app.exec_()