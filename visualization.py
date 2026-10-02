from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


APPOINTMENTS_FILE = Path(__file__).resolve().parent / "appointments.csv"


def show_appointment_charts():
    print("\n--- Charts Dashboard ---")

    try:
        df = pd.read_csv(APPOINTMENTS_FILE)
    except FileNotFoundError:
        print("Error: appointments.csv not found!")
        return

    if df.empty:
        print("No appointments to visualize!")
        return

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(
        "Hospital Appointments Dashboard",
        fontsize=18,
        fontweight="bold",
    )

    doctor_count = df.groupby("Doctor")["Appointment_ID"].count()
    axes[0, 0].bar(doctor_count.index, doctor_count.values)
    axes[0, 0].set_title("Appointments per Doctor")
    axes[0, 0].set_ylabel("Appointments")
    axes[0, 0].tick_params(axis="x", rotation=45)

    daily_counts = df.groupby("Date")["Appointment_ID"].count()
    axes[0, 1].bar(daily_counts.index, daily_counts.values)
    axes[0, 1].set_title("Appointments per Day")
    axes[0, 1].set_ylabel("Appointments")
    axes[0, 1].tick_params(axis="x", rotation=30)

    status_count = df.groupby("Status")["Appointment_ID"].count()
    explode = [0.08] * len(status_count)
    axes[1, 0].pie(
        status_count.values,
        labels=status_count.index,
        explode=explode,
        autopct="%1.1f%%",
    )
    axes[1, 0].set_title("Appointment Statuses")

    demand = df.groupby("Department")["Appointment_ID"].count()
    axes[1, 1].bar(demand.index, demand.values)
    axes[1, 1].set_title("Department Demand")
    axes[1, 1].set_ylabel("Appointments")
    axes[1, 1].tick_params(axis="x", rotation=30)

    plt.tight_layout()
    plt.show()
