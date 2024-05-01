import json
import pandas as pd

class StudentDB:
    def _init_(self, filename):
        self.filename = filename
        try:
            with open(self.filename, "r") as fr:
                self.data = json.load(fr)
        except FileNotFoundError:
            self.data = {}

    def save(self):
        with open(self.filename, "w") as fw:
            json.dump(self.data, fw)

    def add(self, id, name, contact):
        self.data[id] = {"Stu_ID": id,"Student Name": name, "Contact Number": contact}
        self.save()

    def update(self, id, name=None, contact=None):
        if id in self.data:
            # if id:
                # self.data[id]["Student ID"] = id
            if name:
                self.data[id]["Student Name"] = name
            if contact:
                self.data[id]["Contact Number"] = contact
            self.save()

    def delete(self, id):
        if id in self.data:
            del self.data[id]
            self.save()

    def display(self):
        if self.data:
            df = pd.DataFrame(self.data.values(), index=self.data.keys())
            print(df)
        else:
            print("No data to display.\n-----------------")

def main():
    db = StudentDB("students.json")

    while True:
        print("1. Add student")
        print("2. Update student")
        print("3. Delete student")
        print("4. Display all students")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            id = input("Enter Enrollment No: ")
            name = input("Enter Student Name: ")
            contact = input("Enter Contact Number: ")
            db.add(id, name, contact)
        elif choice == "2":
            id = input("Enter Enrollment No of the student to update: ")
            name = input("Enter new Student Name (leave blank to keep the same): ")
            contact = input("Enter new Contact Number (leave blank to keep the same): ")
            db.update(id, name or None, contact or None)
        elif choice == "3":
            id = input("Enter Enrollment No of the student to delete: ")
            db.delete(id)
        elif choice == "4":
            db.display()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "_main_":
    main()