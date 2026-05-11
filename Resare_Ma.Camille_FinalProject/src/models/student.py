"""
Student model module.
"""


class Student:
    """Represents a student."""

    def __init__(self, student_id, name, grades):
        self.student_id = student_id
        self.name = name
        self.grades = grades

    def average(self):
        """Compute average grade."""
        return sum(self.grades) / len(self.grades)

    def to_dict(self):
        """Convert object to dictionary."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "grades": self.grades
        }