class Ward:
    people = []

    def __init__(self, name, yob=0):
        self.name = name
        self.yob = yob

    @classmethod
    def add_person(cls, person):
        cls.people.append(person)

    def describe(self):
        print(f"Name: {self.name}, Year of Birth: {self.yob}, ", end='')

    @classmethod
    def describe_all(cls):
        for person in cls.people:
            person.describe()

    @classmethod
    def count_doctor(cls):
        count = sum(isinstance(person, Doctor) for person in cls.people)
        return count

    @classmethod
    def sort_age(cls):
        cls.people = sorted(cls.people, key=lambda d: d.yob)

    @classmethod
    def compute_average(cls):
        sum_age = 0
        quantity = 0
        for person in cls.people:
            if (isinstance(person, Teacher)):
                quantity += 1
                sum_age += person.yob

        return sum_age/quantity


class Student(Ward):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        super().describe()
        print(f"Grade: {self.grade}")


class Doctor(Ward):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        super().describe()
        print(f"Specialist: {self.specialist}")


class Teacher(Ward):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        super().describe()
        print(f"Subject: {self.subject}")


# 2a
student1 = Student(name=" studentA ", yob=2010, grade="7")
student1.describe()

teacher1 = Teacher(name=" teacherA ", yob=1969, subject=" Math ")
teacher1.describe()

doctor1 = Doctor(name=" doctorA ", yob=1945, specialist=" Endocrinologists ")
doctor1.describe()

# 2b
print()
teacher2 = Teacher(name=" teacherB ", yob=1995, subject=" History ")
doctor2 = Doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")
ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()
Ward.describe_all()

# 2c
print(f"\nNumber of doctors : {ward1.count_doctor()}")

# 2d
print("\nAfter sorting Age of Ward1 people ")
ward1.sort_age()
ward1.describe_all()

# 2e
print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")
