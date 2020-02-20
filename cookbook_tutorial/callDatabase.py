#!/usr/bin/env python
# coding: utf-8

import sqlite3, sys

from PyQt5.QtWidgets import QApplication, QDialog

from sqlite3 import Error

from database import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super(MyForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonCreateDB.clicked.connect(self.create_database)
        self.ui.pushButtonCreateTable.clicked.connect(self.create_table)
        self.ui.pushButtonAddColumn.clicked.connect(self.add_columns)
        self.ui.pushButtonInsertRow.clicked.connect(self.insert_rows)

        self.show()

    def create_database(self):
        try:
            conn = sqlite3.connect(self.ui.lineEditDBName.text() + ".db")
            self.ui.labelResponse.setText("Database is created")
        except Error as e:
            self.ui.labelResponse.setText("Some error has occurred")
        finally:
            conn.close()

    def insert_rows(self):
        sql_statement = "INSERT INTO " + self.ui.lineEditTableName.text() + "','" + self.ui.lineEditPassword.text() + "')"
        try:
            conn = sqlite3.connect(self.ui.lineEditDBName.text() + ".db")
            with conn:
                cur = conn.cursor()
                cur.execute(sql_statement)
                self.ui.labelResponse.setText("Row successfully inserted")
        except Error as e:
            self.ui.labelResponse.setText("Error in inserting row")
        finally:
            conn.close()

    def add_columns(self):
        global table_definition
        if table_definition == "":
            table_definition = (
                "CREATE TABLE IF NOT EXISTS "
                + self.ui.lineEditTableName.text()
                + " ("
                + self.ui.lineEditColumnName.text()
                + " "
                + self.ui.comboBoxDataType.itemText(
                    self.ui.comboBoxDataType.currentIndex()
                )
            )
        else:
            table_definition += (
                ","
                + self.ui.lineEditColumnName.text()
                + " "
                + self.ui.comboBoxDataType.itemText(
                    self.ui.comboBoxDataType.currentIndex()
                )
            )

        self.ui.lineEditColumnName.setText("")
        self.ui.lineEditColumnName.setFocus()

    def create_table(self):
        global table_definition
        try:
            conn = sqlite3.connect(self.ui.lineEditDBName.text() + ".db")
            self.ui.labelResponse.setText("Database is connected")
            c = conn.cursor()
            table_definition += ");"
            c.execute(table_definition)
            self.ui.labelResponse.setText("Table is successfully created")
        except Error as e:
            self.ui.labelResponse.setText("Error in creating table")
        finally:
            conn.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
