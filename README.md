# Python OOP Practice: The Complete Mastery Curriculum

A comprehensive, production-oriented practice curriculum for mastering Object-Oriented Programming in Python from first principles to architectural capstone projects.

---

## How This Repository is Structured

Each of the 15 concept folders is a self-contained learning module containing:
1. **`README.md` (Concept Master Guide)**: Read this first! Explains the theory, real-world motivation, memory models & ASCII diagrams, internal Python mechanics, common pitfalls, and Pythonic best practices.
2. **`problems.md` (Learn-Worthy Practice Challenges)**: Realistic problem scenarios with explicit specifications, input/output contracts, and edge cases.
3. **`*.py` (Interactive Starter Scripts)**: Scaffolding with docstrings, method outlines, and built-in test assertion harnesses (`if __name__ == "__main__":`).
4. **`solutions.md` (Production-Grade Reference Solutions)**: Complete, idiomatic, PEP 8 compliant solutions with explanations of architectural design choices.

---

## How to Practice

1. **Study the Concept**: Open the module folder and read its `README.md`.
2. **Read the Challenge**: Open `problems.md` to understand the domain story and specifications.
3. **Code the Solution**: Open the corresponding `.py` file and write your implementation.
4. **Verify Your Code**: Run the file from your terminal:
   ```bash
   python3 <script_name>.py
   ```
   If all assertions pass, your solution is correct!
5. **Review the Solution**: Check `solutions.md` to see idiomatic Python patterns, alternative approaches, and design takeaways.

---

## Learning Curriculum

| # | Concept Module | Key Mechanics Covered |
| :-: | :--- | :--- |
| **01** | [Classes and Objects](Python_OOP_Practice/01_classes_and_objects/README.md) | Blueprints, object instances, `self` parameter, `__dict__` namespace, identity vs equality. |
| **02** | [Constructors and Instance Methods](Python_OOP_Practice/02_constructors_and_instance_methods/README.md) | `__init__`, invariant validation, mutator vs query methods, mutable default argument traps. |
| **03** | [Class Attributes and Class Methods](Python_OOP_Practice/03_class_attributes_and_class_methods/README.md) | Class state, `@classmethod`, factory constructors (`from_csv`, `from_dict`), shadowing pitfalls. |
| **04** | [Static Methods](Python_OOP_Practice/04_static_methods/README.md) | `@staticmethod`, stateless domain utilities, input validation, mathematical engines. |
| **05** | [Encapsulation](Python_OOP_Practice/05_encapsulation/README.md) | Public, protected (`_`), and private (`__`), name mangling, state security, defensive copying. |
| **06** | [Properties: Getters & Setters](Python_OOP_Practice/06_properties_getters_setters/README.md) | `@property`, `@setter`, computed attributes, non-breaking API refactoring, recursion traps. |
| **07** | [Inheritance](Python_OOP_Practice/07_inheritance/README.md) | "Is-A" taxonomy, code reuse, type introspection (`isinstance`, `issubclass`). |
| **08** | [Method Overriding and `super()`](Python_OOP_Practice/08_method_overriding_and_super/README.md) | Polymorphic specialization, extending vs replacing parent behavior, constructor chaining. |
| **09** | [Multiple Inheritance & MRO](Python_OOP_Practice/09_multiple_inheritance/README.md) | Diamond Problem, C3 Linearization algorithm, `ClassName.mro()`, cooperative `super()`. |
| **10** | [Polymorphism and Duck Typing](Python_OOP_Practice/10_polymorphism_and_duck_typing/README.md) | "If it walks like a duck...", uniform interfaces, EAFP principle, eliminating conditional branches. |
| **11** | [Abstract Base Classes (ABCs)](Python_OOP_Practice/11_abstract_classes/README.md) | `abc.ABC`, `@abstractmethod`, formal interface contracts, Template Method design pattern. |
| **12** | [Composition and Aggregation](Python_OOP_Practice/12_composition_and_aggregation/README.md) | "Has-A" relationships, strong composition vs weak aggregation, component delegation. |
| **13** | [Dunder Methods & Operator Overloading](Python_OOP_Practice/13_dunder_methods_and_operator_overloading/README.md) | Python Data Model, `__str__` vs `__repr__`, math operators, `@total_ordering` comparisons. |
| **14** | [Object Relationships & Design](Python_OOP_Practice/14_object_relationships_and_design/README.md) | Multi-object collaboration, bidirectional state synchronization, SOLID design principles. |
| **15** | [Capstone Combined Projects](Python_OOP_Practice/15_combined_projects/README.md) | Large systems: Library Circulation, ATM & Banking Core, E-Commerce, and University ERP. |
