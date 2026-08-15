<div align="center">

# 🏥 Hospital Appointment System

### A Python-based hospital appointment management system with scheduling, CSV persistence, analytics, and data visualization.

![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Analysis-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

</div>

---

## 📌 Overview

**Hospital Appointment System** is a command-line application built in Python to manage patients and hospital appointments efficiently.

The project combines **Object-Oriented Programming**, **file handling**, **input validation**, **data analysis**, and **data visualization** in one complete workflow. It allows hospital staff to register patients, schedule and manage appointments, inspect doctors' schedules, analyze appointment activity, and display visual dashboards.

---

## ✨ Features

### 👤 Patient Management
- Register new patients.
- Automatically generate unique patient IDs.
- Validate patient age input.
- Store patient information persistently in a CSV file.

### 📅 Appointment Management
- Book appointments for registered patients.
- Automatically generate unique appointment IDs.
- Search appointments by ID.
- Display all appointments.
- Reschedule existing appointments.
- Cancel appointments.
- Mark appointments as completed.
- Track appointment status as **Booked**, **Completed**, or **Cancelled**.

### 🕒 Smart Scheduling & Validation
- Prevent appointments from being created in the past.
- Restrict appointment times to hospital working hours: **09:00 AM – 10:00 PM**.
- Prevent booking a time that has already passed when scheduling for the current day.
- Detect doctor scheduling conflicts.
- Enforce a minimum **30-minute gap** between appointments for the same doctor.

### 👨‍⚕️ Doctor Schedule
- Search a doctor's schedule by name and date.
- Display patient IDs, appointment times, and appointment statuses for the selected day.

### 📊 Data Analysis
The system can generate useful operational insights including:
- Average patient age.
- Average number of appointments per day.
- Maximum appointments recorded on a single day.
- Identification of the busiest appointment day(s).
- Appointment completion percentage.
- Appointment cancellation percentage.
- Chronologically sorted upcoming booked appointments.
- Combined patient and appointment information using data merging.

### 📈 Visualization Dashboard
The project includes a Matplotlib dashboard containing:
- Appointments per doctor.
- Appointments per day.
- Appointment status distribution.
- Appointment demand by department.

---

## 🧠 Concepts Demonstrated

This project demonstrates practical use of:

- Object-Oriented Programming (OOP)
- Classes and encapsulation
- Modular Python programming
- CSV file handling
- Exception handling
- Input validation
- Date and time processing
- Conflict detection algorithms
- Data manipulation with Pandas
- Numerical analysis with NumPy
- Data visualization with Matplotlib
- Grouping, filtering, sorting, and merging datasets

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Core application logic |
| **CSV** | Persistent patient and appointment storage |
| **Pandas** | Data processing and analysis |
| **NumPy** | Statistical calculations |
| **Matplotlib** | Charts and visualization dashboard |
| **datetime** | Date/time validation and scheduling |

---

## 📁 Project Structure

```text
Hospital-Appointment-System/
│
├── main.py               # Main CLI menu and application entry point
├── operations.py         # Patient and appointment classes + core operations
├── analysis.py           # Statistical analysis and reporting
├── visualization.py      # Appointment visualization dashboard
├── patients.csv          # Stored patient records
└── appointments.csv      # Stored appointment records
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/R3Dzf/Hospital-Appointment-System.git
cd Hospital-Appointment-System
```

### 2. Install the required Python packages

```bash
pip install pandas numpy matplotlib
```

> Recommended: **Python 3.12 or newer**.

---

## ▶️ Run the Application

Start the program with:

```bash
python main.py
```

You will be presented with the main menu:

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

## 🔄 Example Workflow

```text
Add Patient
    ↓
Generate Patient ID
    ↓
Book Appointment
    ↓
Validate Date & Time
    ↓
Check Doctor Availability
    ↓
Save Appointment to CSV
    ↓
Manage / Analyze / Visualize Appointment Data
```

---

## 💾 Data Storage

The application uses two CSV files as lightweight persistent storage:

### `patients.csv`

```text
ID, Name, Age, Phone
```

### `appointments.csv`

```text
Appointment_ID, Patient_ID, Doctor, Department, Date, Time, Status
```

Data is loaded automatically when the system starts and saved whenever records are modified.

---

## 📊 Analytics Dashboard

The visualization module transforms appointment data into an easy-to-understand dashboard, helping identify:

- Doctor workload.
- Daily appointment volume.
- Appointment completion/cancellation distribution.
- Departments receiving the highest demand.

This adds a basic **data-driven decision support layer** to the appointment management system instead of limiting the project to CRUD operations only.

---

## 🚀 Possible Future Improvements

- Graphical desktop or web interface.
- SQLite / PostgreSQL database integration.
- Authentication and role-based access for admins, doctors, and receptionists.
- Doctor and department management modules.
- Appointment reminders via email or SMS.
- Patient medical history records.
- REST API integration.
- Advanced reporting and filtering.
- Export reports to PDF or Excel.

---

## 👨‍💻 Author

**Ahmed Youssef**

Computer & Control Engineering Student  
Interested in Software Development, Automation, and Artificial Intelligence.

GitHub: [@R3Dzf](https://github.com/R3Dzf)

---

<div align="center">

### ⭐ If you find this project useful, consider giving the repository a star!

</div>
