# -*- coding: utf-8 -*-
import sqlite3

class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def select_all(self):
        """ Получаем все строки """
        with self.connection:
            return self.cursor.execute('SELECT * FROM order_info').fetchall()

    def select_single(self, rownum):
        """ Получаем одну строку с номером rownum """
        with self.connection:
            return self.cursor.execute('SELECT * FROM order_info WHERE id = ?', (rownum,)).fetchall()[0]

    def select_single_order(self, id):
        with self.connection:
            return self.cursor.execute('SELECT name, number_chosen, other_info FROM order_info WHERE id = ?', (id,)).fetchall()[0]

    def select_text_result(self, chosen_number):
        with self.connection:
            result = self.cursor.execute('SELECT result FROM logic WHERE number_chosen = ?', (chosen_number,)).fetchall()
            if len(result) != 0:
                return result[0][0]
            else:
                return None

    def count_rows(self):
        """ Считаем количество строк """
        with self.connection:
            result = self.cursor.execute('SELECT * FROM order_info').fetchall()
            return len(result)

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()