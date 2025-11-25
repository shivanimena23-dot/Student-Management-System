def load_data():
    try:
        with open("student.txt", "r") as f:
            data = eval(f.read())
    except:
        data = []
    return data


def save_data(data):
    with open("student.txt", "w") as f:
        f.write(str(data))


def add_student():
    roll = input("Roll No: ")
    name = input("Name: ")
    mark = float(input("Mark: "))

    data = load_data()
    data.append({"roll": roll, "name": name, "mark": mark})
    save_data(data)

    print("Added\n")


def view_students():
    data = load_data()
    for s in data:
        print(s)
    print()


def search_student():
    roll = input("Enter roll to search: ")
    data = load_data()

    for s in data:
        if s["roll"] == roll:
            print("Found:", s, "\n")
            return
    print("Not Found\n")


def update_student():
    roll = input("Enter roll to update: ")
    data = load_data()

    for s in data:
        if s["roll"] == roll:
            s["name"] = input("New Name: ")
            s["mark"] = float(input("New Mark: "))
            save_data(data)
            print("Updated\n")
            return
    print("Not Found\n")


def delete_student():
    roll = input("Enter roll to delete: ")
    data = load_data()

    new_data = [s for s in data if s["roll"] != roll]
    save_data(new_data)
    print("Deleted\n")


def topper():
    data = load_data()
    if not data:
        print("No data\n")
        return

    top = max(data, key=lambda x: x["mark"])
    avg = sum(s["mark"] for s in data) / len(data)

    print("Topper:", top)
    print("Average:", avg, "\n")

while True:
    print("1 Add")
    print("2 View")
    print("3 Search")
    print("4 Update")
    print("5 Delete")
    print("6 Topper")
    print("7 Exit")

    ch = input("Enter choice: ")

    if ch == "1": add_student()
    elif ch == "2": view_students()
    elif ch == "3": search_student()
    elif ch == "4": update_student()
    elif ch == "5": delete_student()
    elif ch == "6": topper()
    elif ch == "7": break
    else: print("Invalid\n")