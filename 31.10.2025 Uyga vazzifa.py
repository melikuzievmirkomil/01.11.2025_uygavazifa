import psycopg2

class Data_connect:
    def __init__(self, dbname, user, password, host='localhost', port=5432):
        self.connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        self.cursor = self.connection.cursor()
        print("✅ Databasega bog'lanildi!")

    # --- Jadvallarni yaratish ---
    def create_tables(self):
        d = '''CREATE TABLE IF NOT EXISTS department(id SERIAL PRIMARY KEY, title VARCHAR(50));'''
        c = '''CREATE TABLE IF NOT EXISTS country(id SERIAL PRIMARY KEY, title VARCHAR(50), type VARCHAR(50));'''
        e = '''CREATE TABLE IF NOT EXISTS employee(
                id SERIAL PRIMARY KEY, 
                first_name VARCHAR(50), 
                last_name VARCHAR(50),
                country_id INT REFERENCES country(id) ON DELETE SET NULL,
                department_id INT REFERENCES department(id) ON DELETE SET NULL,
                salary NUMERIC,
                email VARCHAR(100),
                phone VARCHAR(20)
            );'''
        self.cursor.execute(d)
        self.cursor.execute(c)
        self.cursor.execute(e)
        self.connection.commit()
        print("✅ Jadvallar yaratildi!")

    # --- Department CRUD ---
    def add_department(self, title):
        self.cursor.execute("INSERT INTO department (title) VALUES (%s);", (title,))
        self.connection.commit()
        print(f"✅ '{title}' qo‘shildi.")

    def view_department(self):
        self.cursor.execute("SELECT * FROM department;")
        rows = self.cursor.fetchall()
        if rows:
            for item in rows:
                print(f"Department ID: {item[0]}, Nomi: {item[1]}")
        else:
            print("⚠️ Ma'lumotlar mavjud emas.")

    def update_department(self, id, new_title):
        self.cursor.execute("UPDATE department SET title=%s WHERE id=%s;", (new_title, id))
        self.connection.commit()
        print(f"✏️ ID {id} bo'lgan department yangilandi!")

    def del_department(self, id):
        self.cursor.execute("DELETE FROM department WHERE id=%s;", (id,))
        self.connection.commit()
        print(f"🗑️ ID {id} bo'lgan department o‘chirildi.")

    # --- Country CRUD ---
    def add_country(self, title, type):
        self.cursor.execute("INSERT INTO country (title, type) VALUES (%s, %s);", (title, type))
        self.connection.commit()
        print(f"✅ '{title}' qo‘shildi.")

    def view_country(self):
        self.cursor.execute("SELECT * FROM country;")
        rows = self.cursor.fetchall()
        if rows:
            for item in rows:
                print(f"Country ID: {item[0]}, Nomi: {item[1]}, Turi: {item[2]}")
        else:
            print("⚠️ Ma'lumotlar mavjud emas.")

    def update_country(self, id, new_title, new_type):
        self.cursor.execute("UPDATE country SET title=%s, type=%s WHERE id=%s;", (new_title, new_type, id))
        self.connection.commit()
        print(f"✏️ ID {id} bo'lgan country yangilandi!")

    def del_country(self, id):
        self.cursor.execute("DELETE FROM country WHERE id=%s;", (id,))
        self.connection.commit()
        print(f"🗑️ ID {id} bo'lgan country o‘chirildi.")

    # --- Employee CRUD ---
    def add_employee(self, first_name, last_name, country_id, department_id, salary, email, phone):
        self.cursor.execute("""
            INSERT INTO employee (first_name, last_name, country_id, department_id, salary, email, phone)
            VALUES (%s,%s,%s,%s,%s,%s,%s);
        """, (first_name, last_name, country_id, department_id, salary, email, phone))
        self.connection.commit()
        print(f"✅ Xodim {first_name} {last_name} qo‘shildi!")

    def view_employee(self):
        self.cursor.execute('''
            SELECT e.id, e.first_name, e.last_name, c.title, d.title, e.salary, e.email, e.phone
            FROM employee e
            LEFT JOIN country c ON e.country_id=c.id
            LEFT JOIN department d ON e.department_id=d.id
            ORDER BY e.id;
        ''')
        rows = self.cursor.fetchall()
        if rows:
            for item in rows:
                print(f"ID: {item[0]}, Ismi: {item[1]}, Familiyasi: {item[2]}, Davlat: {item[3]}, Bo‘lim: {item[4]}, "
                      f"Oylik: {item[5]}, Email: {item[6]}, Tel: {item[7]}")
        else:
            print("⚠️ Ma'lumotlar mavjud emas.")

    def update_employee(self, id, new_salary):
        self.cursor.execute("UPDATE employee SET salary=%s WHERE id=%s;", (new_salary, id))
        self.connection.commit()
        print(f"✏️ ID {id} bo'lgan xodimning maoshi yangilandi!")

    def del_employee(self, id):
        self.cursor.execute("DELETE FROM employee WHERE id=%s;", (id,))
        self.connection.commit()
        print(f"🗑️ ID {id} bo'lgan xodim o‘chirildi.")

    def search_employee(self, country_title=None, department_title=None):
        query = '''
        SELECT e.first_name, e.last_name, c.title, d.title, e.salary
        FROM employee e
        INNER JOIN country c ON e.country_id=c.id
        INNER JOIN department d ON e.department_id=d.id
        WHERE 1=1
        '''
        params = []
        if country_title:
            query += " AND c.title ILIKE %s"
            params.append(f"%{country_title}%")
        if department_title:
            query += " AND d.title ILIKE %s"
            params.append(f"%{department_title}%")
        self.cursor.execute(query, params)
        rows = self.cursor.fetchall()
        if rows:
            print("\n🔍 Qidiruv natijalari:")
            for item in rows:
                print(f"{item[0]} {item[1]} | {item[2]} | {item[3]} | {item[4]}")
        else:
            print("❌ Xodim topilmadi.")

    def close(self):
        self.cursor.close()
        self.connection.close()
        print("🔒 Connection yopildi!")


# --- Boshqaruv menyusi ---
My_object = Data_connect('n71_baza', 'n71_admin', '123')
# My_object.create_tables()

def manager_tables():
    while True:
        print("\n=== Asosiy boshqaruv ===")
        print("1. Department CRUD")
        print("2. Country CRUD")
        print("3. Employee CRUD")
        print("4. Xodimlarni qidirish")
        print("5. Chiqish")

        kod = input("Tanlovingiz (1-5): ")

        # --- DEPARTMENT ---
        if kod == "1":
            print("\n****** Department ******")
            print("1. Qo'shish\n2. Ko'rish\n3. Yangilash\n4. O'chirish")
            kod1 = input("Tanlovingiz (1-4): ")
            if kod1 == "1":
                title = input("Department nomini kiriting: ")
                My_object.add_department(title)
            elif kod1 == "2":
                My_object.view_department()
            elif kod1 == "3":
                My_object.view_department()
                id = int(input("Tahrirlanadigan ID: "))
                new = input("Yangi nom: ")
                My_object.update_department(id, new)
            elif kod1 == "4":
                My_object.view_department()
                id = int(input("O'chiriladigan ID: "))
                My_object.del_department(id)

        # --- COUNTRY ---
        elif kod == "2":
            print("\n****** Country ******")
            print("1. Qo'shish\n2. Ko'rish\n3. Yangilash\n4. O'chirish")
            kod2 = input("Tanlovingiz (1-4): ")
            if kod2 == "1":
                title = input("Davlat nomini kiriting: ")
                type = input("Davlat turini kiriting: ")
                My_object.add_country(title, type)
            elif kod2 == "2":
                My_object.view_country()
            elif kod2 == "3":
                My_object.view_country()
                id = int(input("Tahrirlanadigan ID: "))
                new_title = input("Yangi nom: ")
                new_type = input("Yangi tur: ")
                My_object.update_country(id, new_title, new_type)
            elif kod2 == "4":
                My_object.view_country()
                id = int(input("O'chiriladigan ID: "))
                My_object.del_country(id)

        # --- EMPLOYEE ---
        elif kod == "3":
            print("\n****** Employee ******")
            print("1. Qo'shish\n2. Ko'rish\n3. Oylik yangilash\n4. O'chirish")
            kod3 = input("Tanlovingiz (1-4): ")
            if kod3 == "1":
                n = input("Xodim ismi: ")
                f = input("Xodim familiyasi: ")
                c = int(input("Country ID: "))
                d = int(input("Department ID: "))
                s = float(input("Oyligi: "))
                e = input("Email: ")
                p = input("Telefon: ")
                My_object.add_employee(n, f, c, d, s, e, p)
            elif kod3 == "2":
                My_object.view_employee()
            elif kod3 == "3":
                My_object.view_employee()
                id = int(input("Tahrirlanadigan ID: "))
                new_salary = float(input("Yangi oylik: "))
                My_object.update_employee(id, new_salary)
            elif kod3 == "4":
                My_object.view_employee()
                id = int(input("O'chiriladigan ID: "))
                My_object.del_employee(id)

        # --- SEARCH ---
        elif kod == "4":
            print("\n------ Xodimlarni qidirish ------")
            country = input("Qaysi davlatdagi xodimlar? (bo'sh bo'lishi mumkin): ")
            depart = input("Qaysi department? (bo'sh bo'lishi mumkin): ")
            My_object.search_employee(country or None, depart or None)

        # --- EXIT ---
        elif kod == "5":
            My_object.close()
            print("Dastur tugadi!")
            break

        else:
            print("❌ Noto‘g‘ri tanlov, qayta urinib ko‘ring.")

manager_tables()
