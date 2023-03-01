from dataclasses import dataclass, field
from typing import List


@dataclass()
class Subject:
    identifier: int
    name: str
    is_obligatory: bool = True
    teachers_names: List[str] = field(default_factory=list)

    def assign_teacher(self, name):
        self.teachers_names.append(name)


# @dataclass(frozen=True)
@dataclass()
class Grade:
    value: int
    FAILING_GRADE = ClassVar = 1

    def is_passing(self):
        return self.value > Grade.FAILING_GRADE

    def __repr__(self):
        return str(self.value)


# @dataclass(frozen=True)
@dataclass()
class FinalGrade(Grade):
    subject = str

    def __repr__(self):
        return f"{self.subject}: {self.value}"


def run_example():
    math = Subject(identifier=1, name="Matematyka")
    print(math)

    math.assign_teacher("Bob")
    math.assign_teacher("Karola")
    print(math)


if __name__ == "__main__":
    run_example()
