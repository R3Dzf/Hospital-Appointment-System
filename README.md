<div align="center">

# 🏥 Hospital Appointment System

A Python command-line application for managing patients and hospital appointments with scheduling validation, CSV persistence, analytics, and visualization.

![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Analysis-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

</div>

---

## Overview

**Hospital Appointment System** is a modular Python project that simulates the day-to-day workflow of a small hospital appointment desk.

The application can register patients, create and manage appointments, validate scheduling rules, inspect doctor schedules, save data to CSV files, calculate operational statistics, and display appointment charts.

The project was built to practice practical Python concepts rather than only basic CRUD operations. It combines:

- Object-oriented programming
- File persistence
- Date and time validation
- Scheduling conflict detection
- Data analysis
- Data visualization
- Modular project structure

---

## Main Features

### Patient Management

- Register a new patient
- Generate patient IDs automatically
- Validate age input
- Save patient data immediately to CSV
- Load saved patient records when the application starts

### Appointment Management

- Book an appointment for an existing patient
- Generate appointment IDs automatically
- Display all appointments
- Search by appointment ID
- Reschedule booked appointments
- Cancel appointments
- Mark appointments as completed
- Track appointment states:
  - `Booked`
  - `Completed`
  - `Cancelled`

### Scheduling Validation

Appointments are validated before being accepted.

The system:

- Rejects dates in the past
- Restricts appointment times to **09:00 AM – 10:00 PM**
- Rejects times that have already passed when booking for today
- Detects conflicts for the same doctor
- Requires at least a **30-minute gap** between the same doctor's active appointments
- Re-checks doctor conflicts when an appointment is rescheduled

### Doctor Schedule

A doctor schedule can be displayed for a selected date, including:

- Appointment time
- Patient ID
- Appointment status

### Analytics

The analytics module uses Pandas and NumPy to report:

- Average patient age
- Average appointments per day
- Maximum appointments recorded on one day
- Busiest appointment day(s)
- Completion percentage
- Cancellation percentage
- Upcoming booked appointments sorted by date and time
- Merged patient and appointment information

### Visualization Dashboard

Matplotlib is used to display four charts:

- Appointments per doctor
- Appointments per day
- Appointment status distribution
- Department demand

---

## Application Flow

```text
Start Application
      │
      ▼
Load Patients & Appointments
      │
      ▼
   Main Menu
      │
 ┌────┼───────────────────────────────┐
 ▼    ▼        ▼        ▼             ▼
Add  Book    Search   Update       Analyze
Patient Appointment Appointment Appointment Data
      │
      ▼
Validate Date / Time
      │
      ▼
Check Doctor Conflict
      │
      ▼
Save to CSV
```

---

## Project Structure

```text
Hospital-Appointment-System/
├── main.py
├── operations.py
├── analysis.py
├── visualization.py
├── patients.csv
├── appointments.csv
├── requirements.txt
├── .gitignore
└── README.md
```

### File Responsibilities

| File | Responsibility |
| --- | --- |
| `main.py` | CLI menu and application entry point |
| `operations.py` | Patient/appointment models, scheduling rules, CRUD operations, CSV persistence |
| `analysis.py` | Statistical analysis and operational reports |
| `visualization.py` | Matplotlib appointment dashboard |
| `patients.csv` | Demo patient records |
| `appointments.csv` | Demo appointment records |
| `requirements.txt` | Python dependencies |

---

## Tech Stack

| Technology | Usage |
| --- | --- |
| **Python** | Main application logic |
| **CSV** | Lightweight persistent storage |
| **Pandas** | Data loading, grouping, filtering, merging and sorting |
| **NumPy** | Statistical calculations |
| **Matplotlib** | Data visualization |
| **datetime** | Date/time parsing and scheduling validation |
| **pathlib** | Reliable project-relative file paths |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/R3Dzf/Hospital-Appointment-System.git
cd Hospital-Appointment-System
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```

---

## Main Menu

When the program starts, the following menu is displayed:

```text
------------------ Welcome to Hospital Appointment System Menu ------------------
1. Add a patient
2. Book an appointment
3. Display all appointments
4. Search appointments
5. Update an appointment
6. Cancel an appointment
7. Mark an appointment completed
8. Display a doctor schedule
9. Analyze appointment data
10. Show appointment charts
11. Save data
12. Exit
```

---

## Example Booking Workflow

```text
Enter Patient ID
      │
      ▼
Verify Patient Exists
      │
      ▼
Enter Doctor & Department
      │
      ▼
Choose Future Date
      │
      ▼
Choose Time Within Working Hours
      │
      ▼
Check 30-Minute Doctor Gap
      │
      ├── Conflict → Reject
      │
      └── Available
             │
             ▼
      Create Appointment
             │
             ▼
        Save to CSV
```

---

## Data Storage

The project deliberately uses CSV files to keep the storage layer simple and easy to inspect.

### `patients.csv`

```text
ID,Name,Age,Phone
```

### `appointments.csv`

```text
Appointment_ID,Patient_ID,Doctor,Department,Date,Time,Status
```

The repository includes sample records so the analysis and visualization features can be tested immediately.

> The bundled CSV content is demonstration data for the project, not a real hospital database.

---

## Engineering Concepts Demonstrated

This project demonstrates hands-on use of:

- Classes and encapsulation
- Object-oriented design
- Modular Python code
- Persistent file storage
- Defensive input validation
- Exception handling
- Date/time processing
- Scheduling conflict detection
- Collection searching and filtering
- Pandas grouping and merging
- Statistical analysis with NumPy
- Visualization with Matplotlib

---

## Recent Code Improvements

The project has also been cleaned up to make the repository easier to run and maintain:

- Fixed the analytics module so it runs correctly
- Added a proper `__main__` entry-point guard
- Added project-relative file paths
- Added doctor-conflict validation when rescheduling
- Made chart status handling work with any number of appointment statuses
- Added `requirements.txt`
- Added a Python `.gitignore`
- Improved naming, output messages, formatting and code organization

---

## Possible Future Improvements

- Replace CSV storage with SQLite or PostgreSQL
- Add a graphical desktop interface
- Build a Flask/FastAPI web version
- Add staff authentication and role-based access
- Add dedicated doctor management
- Add patient medical-history records
- Add appointment reminders
- Add advanced search and filtering
- Export reports to PDF or Excel
- Add automated tests

---

## Author

**Ahmed Youssef Bosha**  
Computer & Control Engineering Student — Tanta University

GitHub: [@R3Dzf](https://github.com/R3Dzf)

---

<div align="center">

Built as a practical Python project combining OOP, scheduling logic, persistence, analytics, and visualization.

</div>
