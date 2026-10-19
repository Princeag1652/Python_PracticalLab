
import pickle
import shelve
from pathlib import Path


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student(name='{self.name}', marks={self.marks})"


# Save an object using pickle
def save_with_pickle(student, filename):
    with open(filename, "wb") as file:
        pickle.dump(student, file)
    print(f"[pickle] Object saved to {filename}")


# Restore an object using pickle
def load_with_pickle(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)


# Save and restore objects using shelve
def save_with_shelve(student, filename):
    with shelve.open(filename) as database:
        database["student1"] = student
    print("[shelve] Object saved with key 'student1'")


def load_with_shelve(filename):
    with shelve.open(filename) as database:
        return database["student1"]


if __name__ == "__main__":
    pickle_file = "objects.pkl"
    shelve_file = "object_store"

    # Create an object
    student = Student("Aarav", [85, 90, 92])

    print("=" * 50)
    print("       OBJECT PERSISTENCE ENGINE")
    print("=" * 50)

    print("\n--- Original Object ---")
    print(student)

    # Pickle serialization and restoration
    save_with_pickle(student, pickle_file)
    restored_student = load_with_pickle(pickle_file)

    print("[pickle] Object restored successfully")
    print("Restored:", restored_student)

    # Shelve serialization and restoration
    save_with_shelve(student, shelve_file)
    restored_shelve = load_with_shelve(shelve_file)

    print("[shelve] Object restored successfully")
    print("Restored:", restored_shelve)

    print("\nPersistence test completed successfully.")
    print(f"Pickle file: {Path(pickle_file).resolve()}")
    print(f"Shelve database base: {Path(shelve_file).resolve()}")
