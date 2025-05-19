import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    password="whbdgh8153",
    database="student",
)

cursor = db.cursor()

# 添加学生
def add_student():
    id = input("请输入学号: ")
    name = input("请输入姓名: ")
    age = input("请输入年龄: ")
    gender = input("请输入性别: ")
    sql = "INSERT INTO students (id, name, age, gender) VALUES (%s, %s, %s, %s)"
    try:
        cursor.execute(sql, (id, name, age, gender))
        db.commit()
        print("添加成功！")
    except pymysql.err.IntegrityError:
        print("该学号已存在，添加失败。")

# 删除学生
def delete_student():
    id = input("请输入要删除的学号: ")
    cursor.execute("SELECT * FROM students WHERE id = %s", (id,))
    if cursor.fetchone():
        cursor.execute("DELETE FROM students WHERE id = %s", (id,))
        db.commit()
        print("删除成功！")
    else:
        print("该学号不存在对应的学生。")

# 查找学生
def search_student():
    id = input("请输入要查找的学号: ")
    cursor.execute("SELECT * FROM students WHERE id = %s", (id,))
    student = cursor.fetchone()
    if student:
        print("学号:", student[0])
        print("姓名:", student[1])
        print("年龄:", student[2])
        print("性别:", student[3])
    else:
        print("该学号不存在对应的学生。")

# 修改学生
def update_student():
    id = input("请输入要修改的学号: ")
    cursor.execute("SELECT * FROM students WHERE id = %s", (id,))
    if cursor.fetchone():
        name = input("请输入新姓名: ")
        age = input("请输入新年龄: ")
        sql = "UPDATE students SET name = %s, age = %s WHERE id = %s"
        cursor.execute(sql, (name, age, id))
        db.commit()
        print("修改成功！")
    else:
        print("该学号不存在对应的学生。")

def main():
    while True:
        print("\n学生信息管理系统")
        print("1. 添加学生")
        print("2. 删除学生")
        print("3. 查找学生")
        print("4. 修改学生")
        print("5. 退出系统")
        choice = input("请选择操作 (1-5): ")
        if choice == "1":
            add_student()
        elif choice == "2":
            delete_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            print("退出系统")
            break
        else:
            print("无效输入，请重新选择。")

if __name__ == "__main__":
    main()
    db.close()
