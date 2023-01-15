class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = list()
        self.grades = list()

    def add_student(self, name: str, grade: float):
        if self.__students_count > 0:
            self.students.append(name)
            self.grades.append(grade)
            self.__students_count -= 1

    def get_average_grade(self):
        average_grade = sum(self.grades) / len(self.grades)
        return float(f"{average_grade:.2f}")

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade()}"
