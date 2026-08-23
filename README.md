"# Python_oops_Basic_to_Advance" 

## Day 1 — Topics Covered
- OOP Basics
- Why OOP?
- Classes
- Objects
- Class vs Object
- Attributes
- Methods
- self
- __init__()
- Instance Attributes
- Creating Multiple Objects
- Using self to access object data
- Basic OOP Practice with Car and Student classes

---

## Day 2 — Variables & Methods
- Instance Variables
- Class Variables
- Instance Methods
- Class Methods
- cls
- @classmethod
- Static Methods
- @staticmethod
- Alternative Constructors
- self vs cls
- Instance vs Class vs Static Methods

---

## Day 3 — Inheritance
- Inheritance
- Parent/Base Class
- Child/Derived Class
- Basic Inheritance
- Inherited Attributes & Methods
- super()
- Method Overriding
- Single Inheritance
- Multilevel Inheritance
- Multiple Inheritance
- Hierarchical Inheritance
- Hybrid Inheritance
- "IS-A" Relationship

---

## Day 4 — Polymorphism
- Polymorphism
- Method Overriding
- Duck Typing
- Method Overloading
- Operator Overloading
- Dunder Methods
- Polymorphism in AI/ML

---

## Day 5 — Encapsulation & Abstraction
- Encapsulation
- Public, Protected & Private conventions
- _variable
- __variable
- Name Mangling
- Getters & Setters
- @property
- Property Setter
- Abstraction
- Abstract Classes
- ABC
- @abstractmethod
- Encapsulation vs Abstraction

---

## Day 6 — Advanced Python OOP
- Dunder/Magic Methods
- __str__()
- __repr__()
- __len__()
- __eq__()
- __add__()
- Operator Overloading
- Composition
- Aggregation
- Association
- Multiple Inheritance
- MRO (Method Resolution Order)
- super() with MRO
- object Class

---

## Day 7 — OOP Final Project & Interview Preparation
### 🏗️ Final Project — Student Management System

Classes
Person (Abstract Class)
│
├── Student
│
└── Teacher

StudentManager
└── manages Student objects

#### Person
- Common name and age
- Abstract display_role()

#### Student
- Inherits from Person
- course
- Protected-style age property
- Encapsulated marks
- display()
- is_passed()
- display_role()
- __str__()

#### Teacher
- Inherits from Person
- subject
- display_role()

#### StudentManager
- Stores students
- add_student()
- display_all()
- find_student()
- remove_student()