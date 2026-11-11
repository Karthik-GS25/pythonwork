"""59. Validate and append student marks records with exceptions."""


class InvalidMarksError(Exception):
    pass


def save_record(name, marks, file_name="student_records.txt"):
    assert name.strip(), "Student name cannot be empty"
    try:
        value = float(marks)
        if not 0 <= value <= 100:
            raise InvalidMarksError("Marks must be between 0 and 100")
        with open(file_name, "a", encoding="utf8") as file:
            file.write(f"{name.strip()}: {value:g}\n")
        return True
    except ValueError:
        return False
    finally:
        pass


print(save_record("Amrita", 90, "student_records_demo.txt"))
