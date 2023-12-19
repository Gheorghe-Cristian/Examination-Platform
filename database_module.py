import sqlite3
    
class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect("test_database.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS tests
                   (nume_test TEXT,
                   nr_intrebari INT);''')
        self.conn.commit()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS intrebari (
            test_id INT,
            intrebare TEXT,
            answer_1 TEXT,
            answer_2 TEXT,
            answer_3 TEXT,
            answer_4 TEXT,
            correct_answer INT       
            );''')
        self.conn.commit()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS resultate (
            test_id INT,
            nume_test TEXT,       
            nume_student TEXT,
            nota REAL       
        );''')
        self.conn.commit()

    def adauga_test(self, nume_test, nr_intrebari):
        self.cursor.execute('INSERT INTO tests (nume_test, nr_intrebari) VALUES (?, ?)', (nume_test, nr_intrebari))
        self.conn.commit()
    def adauga_intrebare(self, test_id, intrebare, answer_1, answer_2, answer_3, answer_4, correct_answer):
        self.cursor.execute('INSERT INTO intrebari (test_id, intrebare, answer_1, answer_2, answer_3, answer_4, correct_answer) VALUES (?, ?, ?, ?, ?, ?, ?)', (test_id, intrebare, answer_1, answer_2, answer_3, answer_4, correct_answer))
        self.conn.commit()
    def afiseaza_test(self):
        self.cursor.execute('SELECT * FROM tests')
        return self.cursor.fetchall()
    def returneaza_rowid(self, nume_test, nr_intrebari):
        self.cursor.execute('SELECT rowid FROM tests WHERE nume_test = ? and nr_intrebari = ?', (nume_test, nr_intrebari))
        row = self.cursor.fetchone() 
        if row:
            return row[0]  
        else:
            return None
    def find_by_name(self, secventa_cautata):
        self.cursor.execute("SELECT * FROM tests WHERE nume_test = ?", (secventa_cautata,))
        return self.cursor.fetchall()
    def filter_by_questions(self, nr_questions):
        self.cursor.execute("SELECT * FROM tests WHERE nr_intrebari = ?", (nr_questions,))
        return self.cursor.fetchall()
    def afiseaza_intrebari(self, test_id):
        self.cursor.execute('SELECT * FROM intrebari WHERE test_id = ?', (test_id,))
        return self.cursor.fetchall()
    def adauga_rezultat(self, test_id, nume_test, nume_student, nota):
        self.cursor.execute('INSERT INTO resultate (test_id, nume_test, nume_student, nota) VALUES (?, ?, ?, ?)', (test_id, nume_test, nume_student, nota))
        self.conn.commit()
    def intrebari_corecte_a_unui_test(self, test_id):
        self.cursor.execute('SELECT correct_answer FROM intrebari WHERE test_id = ?', (test_id,))
        return self.cursor.fetchall()
    def afiseaza_rezultate_student(self, nume_student):
        self.cursor.execute('SELECT * FROM resultate WHERE nume_student = ?', (nume_student,))
        return self.cursor.fetchall()
    def afiseaza_rezultate_prof(self):
        self.cursor.execute('SELECT * FROM resultate')
        return self.cursor.fetchall()
    def afiseaza_nume_test(self, rowid):
        self.cursor.execute('SELECT nume_test FROM tests WHERE rowid = ?', (rowid,))
        return self.cursor.fetchall()
    def close(self):
        self.conn.close()
