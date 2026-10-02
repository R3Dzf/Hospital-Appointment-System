import numpy as np
import pandas as pd

import operations


analysis = operations.HospitalSystem()


def average_patient_age():
    if len(analysis.patient) == 0:
        print("There are no patients to analyze.")
        return

    df = pd.read_csv(analysis.patient_file)
    print(f"Average patient age: {df['Age'].mean():.2f} years")


def analyze_appointment_data():
    if len(analysis.appointment) == 0:
        print("There are no appointments to analyze.")
        return

    df = pd.read_csv(analysis.appointment_file)
    daily_counts = df.groupby("Date")["Appointment_ID"].count()

    avg_per_day = np.mean(daily_counts)
    max_per_day = np.max(daily_counts)
    busiest_days = daily_counts[daily_counts == max_per_day].index

    print(f"Average appointments per day: {avg_per_day:.2f}")
    print(f"Maximum appointments in one day: {max_per_day}")
    print("Busiest day(s):", *list(busiest_days))


def cancellation_and_completion_percentages():
    if len(analysis.appointment) == 0:
        print("There are no appointments to analyze.")
        return

    df = pd.read_csv(analysis.appointment_file)
    total_appointments = len(df)

    cancelled_count = len(df[df["Status"] == "Cancelled"])
    completed_count = len(df[df["Status"] == "Completed"])

    print(
        f"Completed: {(completed_count / total_appointments) * 100:.2f}% "
        f"({completed_count} appointments)"
    )
    print(
        f"Cancelled: {(cancelled_count / total_appointments) * 100:.2f}% "
        f"({cancelled_count} appointments)"
    )


def operation_appointments():
    if len(analysis.appointment) == 0:
        print("There are no appointments to analyze.")
        return

    appointments = pd.read_csv(analysis.appointment_file)

    appointments["Real_Time"] = pd.to_datetime(
        appointments["Date"] + " " + appointments["Time"],
        errors="coerce",
    )
    appointments = appointments.sort_values(by="Real_Time").drop(
        "Real_Time", axis=1
    )

    print(
        "--------------------------- "
        "Upcoming Booked Appointments "
        "---------------------------"
    )
    print(
        appointments.query("Status == 'Booked'")
        .head(10)
        .to_string(index=False)
    )

    patients = pd.read_csv(analysis.patient_file)
    merged = pd.merge(
        appointments,
        patients,
        left_on="Patient_ID",
        right_on="ID",
    )

    print()
    print("------------ Patients and Appointments ------------")
    print(
        merged[["Name", "Doctor", "Date", "Time"]]
        .head(10)
        .to_string(index=False)
    )


def run_all():
    print(
        """
=====================================================
     SYSTEM DATA ANALYSIS & PERFORMANCE REPORT
=====================================================
"""
    )

    print("Analyzing data...\n")
    average_patient_age()
    analyze_appointment_data()
    cancellation_and_completion_percentages()
    operation_appointments()
