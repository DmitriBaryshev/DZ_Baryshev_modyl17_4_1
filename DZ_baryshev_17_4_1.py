import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('academy.db')
cursor = conn.cursor()

# Запрос 1: Вывести все возможные пары строк преподавателей и групп
cursor.execute("SELECT e.last_name AS teacher, g.group_name AS group_name FROM Employees e, Groups g")
rows = cursor.fetchall()
print("Запрос 1:")
for row in rows:
    print(row)

# Запрос 2: Вывести названия факультетов, фонд финансирования кафедр которых превышает фонд финансирования факультета
cursor.execute("SELECT f.faculty_name FROM Faculties f WHERE f.department_funding > f.faculty_funding")
rows = cursor.fetchall()
print("\nЗапрос 2:")
for row in rows:
    print(row)

# Запрос 3: Вывести фамилии кураторов групп и названия групп, которые они курируют
cursor.execute("SELECT e.last_name AS curator, g.group_name FROM Employees e JOIN Groups g ON e.employee_id = g.curator_id")
rows = cursor.fetchall()
print("\nЗапрос 3:")
for row in rows:
    print(row)

# Запрос 4: Вывести имена и фамилии преподавателей, которые читают лекции у группы "P107"
cursor.execute("SELECT e.first_name, e.last_name FROM Employees e JOIN Lectures l ON e.employee_id = l.employee_id JOIN Groups g ON l.group_id = g.group_id WHERE g.group_name = 'P107'")
rows = cursor.fetchall()
print("\nЗапрос 4:")
for row in rows:
    print(row)

# Запрос 5: Вывести фамилии преподавателей и названия факультетов, на которых они читают лекции
cursor.execute("SELECT e.last_name, f.faculty_name FROM Employees e JOIN Departments d ON e.department_id = d.department_id JOIN Faculties f ON d.faculty_id = f.faculty_id")
rows = cursor.fetchall()
print("\nЗапрос 5:")
for row in rows:
    print(row)

# Запрос 6: Вывести названия кафедр и названия групп, которые к ним относятся
cursor.execute("SELECT d.department_name, g.group_name FROM Departments d JOIN Groups g ON d.department_id = g.department_id")
rows = cursor.fetchall()
print("\nЗапрос 6:")
for row in rows:
    print(row)

# Запрос 7: Вывести названия дисциплин, которые читает преподаватель "Samantha Adams"
cursor.execute("SELECT s.subject_name FROM Subjects s JOIN Lectures l ON s.subject_id = l.subject_id JOIN Employees e ON l.employee_id = e.employee_id WHERE e.first_name = 'Samantha' AND e.last_name = 'Adams'")
rows = cursor.fetchall()
print("\nЗапрос 7:")
for row in rows:
    print(row)

# Запрос 8: Вывести названия кафедр, на которых читается дисциплина "Database Theory"
cursor.execute("SELECT d.department_name FROM Departments d JOIN Subjects s ON d.department_id = s.department_id WHERE s.subject_name = 'Database Theory'")
rows = cursor.fetchall()
print("\nЗапрос 8:")
for row in rows:
    print(row)

# Запрос 9: Вывести названия групп, которые относятся к факультету “Computer Science”
cursor.execute("SELECT g.group_name FROM Groups g JOIN Departments d ON g.department_id = d.department_id JOIN Faculties f ON d.faculty_id = f.faculty_id WHERE f.faculty_name = 'Computer Science'")
rows = cursor.fetchall()
print("\nЗапрос 9:")
for row in rows:
    print(row)

# Запрос 10: Вывести названия групп 5-го курса и название факультетов, к которым они относятся
cursor.execute("SELECT g.group_name, f.faculty_name FROM Groups g JOIN Faculties f ON g.faculty_id = f.faculty_id WHERE g.course_number = 5")
rows = cursor.fetchall()
print("\nЗапрос 10:")
for row in rows:
    print(row)

# Запрос 11: Вывести полные имена преподавателей и лекции, которые они читают (названия дисциплин и групп), при этом отобрать только те лекции, которые читаются в аудитории “B103”
cursor.execute("SELECT e.first_name, e.last_name, s.subject_name, g.group_name FROM Employees e JOIN Lectures l ON e.employee_id = l.employee_id JOIN Subjects s ON l.subject_id = s.subject_id JOIN Groups g ON l.group_id = g.group_id WHERE l.classroom = 'B103'")
rows = cursor.fetchall()
print("\nЗапрос 11:")
for row in rows:
    print(row)

# Закрытие соединения с базой данных
conn.close()
