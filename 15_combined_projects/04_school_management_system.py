"""
## Project 4 — Comprehensive Academic University ERP

### System Specifications
1. **Abstract Base Class `Person(ABC)`**:
   - `__init__(person_id: str, name: str, email: str)`
   - `@abstractmethod def get_role(self) -> str`.
2. **Class `Teacher(Person)`**:
   - `__init__(person_id: str, name: str, email: str, department: str)`
   - Overrides `get_role() -> str`: returns `"Faculty"`.
3. **Class `Student(Person)`**:
   - `__init__(person_id: str, name: str, email: str, major: str)`
   - Attributes: `grades: dict[str, float] = {}` (course_code -> score 0-100).
   - Overrides `get_role() -> str`: returns `"Student"`.
   - Method `calculate_gpa() -> float`: 4.0 scale conversion from percentage grades.
4. **Class `Course`**:
   - `__init__(course_code: str, title: str, credits: int, capacity: int)`
   - Attributes: `instructor: Optional[Teacher] = None`, `roster: list[Student] = []`.
   - Methods: `assign_teacher(teacher)`, `enroll_student(student)`, `submit_grade(student_id, score)`.
5. **Class `Department`**:
   - Aggregates courses and teachers for an academic unit.
6. **Class `University`**:
   - Top-level container managing departments, courses, students, and staff.
   - Methods:
     - `get_deans_list(min_gpa: float = 3.8) -> list[Student]`
     - `generate_transcript(student_id: str) -> str`

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:
