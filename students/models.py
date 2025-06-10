from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_average_grade(self) -> float:
        students = self.students.all()
        if not students:
            return 0.0
        return round(sum(s.get_average_grade() for s in students) / len(students), 2)

    def get_average_grade_by_subject(self, subject: str) -> float:
        students = self.students.all()
        if not students:
            return 0.0
        return round(
            sum(s.get_average_grade_by_subject(subject) for s in students) / len(students),
            2
        )


class Student(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name

    def get_average_grade(self) -> float:
        grades = [g.grade for g in self.grades.all()]
        if grades:
            return round(sum(grades) / len(grades), 2)
        return 0.0

    def get_average_grade_by_subject(self, subject: str) -> float:
        grades = [g.grade for g in self.grades.filter(subject=subject)]
        if grades:
            return round(sum(grades) / len(grades), 2)
        return 0.0


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    subject = models.CharField(max_length=100)
    grade = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.subject}: {self.grade}"
