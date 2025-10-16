# Student Grade Management System 📚

A Python-based student grade management system that helps track student performance, calculate grades, and generate detailed academic reports.
<div align="center">

### Don't want to clone? No problem! Run it instantly:

[![Open in Codespaces](https://img.shields.io/badge/Open%20in-Codespaces-green?style=for-the-badge&logo=github)](https://codespaces.new/sridharchinthaparthi/student-grade-manager)

**Perfect for:**
- 📱 Mobile browsing - Test from your phone!
- ⚡ Quick exploration - No setup required
- 🧪 Experimentation - Fork and modify

</div>

## Features

- **Student Data Entry**: Add multiple students with roll numbers and marks
- **Automatic Grade Calculation**: Calculates total, average, percentage, and letter grades
- **Pass/Fail Status**: Automatically determines student status based on percentage
- **Class Statistics**: 
  - Total pass/fail count
  - Class average percentage
  - Highest and lowest scores
- **Top Performers List**: Displays top 3 students ranked by percentage
- **Subject-wise Analysis**: Shows average marks for each subject
- **Search Functionality**: Find students by name or roll number
- **Clean Reports**: Formatted output for easy reading

## Grading System

| Percentage | Grade | Status |
|------------|-------|--------|
| 90% - 100% | A+ | Pass |
| 80% - 89% | A | Pass |
| 70% - 79% | B | Pass |
| 60% - 69% | C | Pass |
| 50% - 59% | D | Pass |
| 40% - 49% | E | Pass |
| Below 40% | F | Fail |

## Technologies Used

- Python 3.10
- Built-in data structures (Lists, Dictionaries)
- String manipulation methods
- Sorting algorithms

## Skills Demonstrated

This project showcases proficiency in:
- **Variables & Data Types**: Integers, floats, strings, lists, dictionaries
- **Multi-variable Creation**: Managing multiple data points simultaneously
- **Inbuilt Methods**: String methods (strip, title, upper, lower), list methods (append, sum)
- **Indexing & Slicing**: Accessing and manipulating list elements
- **Copy Operations**: Creating independent copies of data structures
- **Typecasting**: Converting between integers, floats, and strings
- **Input/Output**: User interaction and formatted output
- **Operators**: Arithmetic, comparison, and logical operators
- **Conditional Statements**: If-elif-else for grade assignment
- **Looping Statements**: For loops for iteration, nested loops for sorting
- **List Comprehension Concepts**: Data manipulation and filtering

## Installation

```bash
git clone https://github.com/sridharchinthaparthi/student-grade-manager.git
cd student-grade-manager
```

## Usage

Run the program:

```bash
python grades.py
```

Follow the prompts:
1. Enter the number of students
2. For each student, provide:
   - Name
   - Roll Number
   - Marks for 5 subjects (out of 100)
3. View comprehensive reports:
   - Individual grade reports
   - Class statistics
   - Top performers
   - Subject-wise analysis
4. Search for specific students

## Example Output

```
========================================
  STUDENT GRADE MANAGEMENT
========================================

How many students? 2

Student 1:
Name: sri
Roll Number: 1
Enter marks (out of 100):
  Subject 1: 45
  Subject 2: 56
  Subject 3: 47
  Subject 4: 87
  Subject 5: 65

Student 2:
Name: sam
Roll Number: 2
Enter marks (out of 100):
  Subject 1: 56
  Subject 2: 47
  Subject 3: 86
  Subject 4: 87
  Subject 5: 47

================================================================================
GRADE REPORT
================================================================================

Name: Sri
Roll No: 1
Marks: [45.0, 56.0, 47.0, 87.0, 65.0]
Total: 300.00 | Average: 60.00 | Percentage: 60.00%
Grade: C | Status: Pass
--------------------------------------------------------------------------------

Name: Sam
Roll No: 2
Marks: [56.0, 47.0, 86.0, 87.0, 47.0]
Total: 323.00 | Average: 64.60 | Percentage: 64.60%
Grade: C | Status: Pass
--------------------------------------------------------------------------------

================================================================================
CLASS STATISTICS
================================================================================
Total Students: 2
Passed: 2
Failed: 0

Class Average: 62.30%
Highest Percentage: 64.60%
Lowest Percentage: 60.00%

================================================================================
TOP PERFORMERS
================================================================================
1. Sam - 64.60%
2. Sri - 60.00%

================================================================================
SUBJECT WISE ANALYSIS
================================================================================
Subject 1: Average = 50.50
Subject 2: Average = 51.50
Subject 3: Average = 66.50
Subject 4: Average = 87.00
Subject 5: Average = 56.00

================================================================================

Search for a student? (y/n): y
Enter name or roll number: 2

Found!
Name: Sam
Roll: 2
Percentage: 64.60%
Grade: C

================================================================================
Thank you for using the system!
================================================================================
```

## Learning Objectives

This project was built to practice and demonstrate understanding of:
- Working with multiple data structures
- Data validation and processing
- Implementing sorting algorithms manually
- Creating user-friendly CLI applications
- Managing student records programmatically

## Future Enhancements

- Add more subjects dynamically
- Export reports to text files
- Graphical charts for performance visualization
- Edit and delete student records
- Attendance tracking integration

## Author

**Sridhar Chinthaparthi**

GitHub: [@sridharchinthaparthi](https://github.com/sridharchinthaparthi)

## License

This project is open source and available under the MIT License.

---


*Built with Python to simplify student grade management and analysis.*
