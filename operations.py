from datetime import datetime
from pathlib import Path
import csv


BASE_DIR = Path(__file__).resolve().parent


class Patient:
    def __init__(self, patient_id, name, age, phone):
        self.__patient_id = patient_id
        self.__name = name
        self.__age = age
        self.__phone = phone

    def to_dict(self):
        return {
            "ID": self.__patient_id,
            "Name": self.__name,
            "Age": self.__age,
            "Phone": self.__phone,
        }


class Appointment:
    def __init__(
        self,
        appointment_id,
        patient_id,
        doctor,
        department,
        date,
        time,
        status="Booked",
    ):
        self.__appointment_id = appointment_id
        self.__patient_id = patient_id
        self.__doctor = doctor
        self.__department = department
        self.__date = date
        self.__time = time
        self.__status = status

    def update_datetime(self, new_date, new_time):
        self.__date = new_date
        self.__time = new_time

    def mark_as_completed(self):
        self.__status = "Completed"

    def cancel_appointment(self):
        self.__status = "Cancelled"

    def to_dict(self):
        return {
            "Appointment_ID": self.__appointment_id,
            "Patient_ID": self.__patient_id,
            "Doctor": self.__doctor,
            "Department": self.__department,
            "Date": self.__date,
            "Time": self.__time,
            "Status": self.__status,
        }


def get_valid_future_date():
    while True:
        user_input = input("Enter appointment date (YYYY-MM-DD): ").strip()

        try:
            date_input = datetime.strptime(user_input, "%Y-%m-%d").date()
            today_date = datetime.now().date()

            if date_input < today_date:
                print("Error: You cannot book an appointment in the past!")
                continue

            return user_input

        except ValueError:
            print("Invalid date format! Please use YYYY-MM-DD")


def get_valid_future_time(selected_user_date):
    selected_date = datetime.strptime(selected_user_date, "%Y-%m-%d").date()
    today_date = datetime.now().date()

    start_time = datetime.strptime("09:00 AM", "%I:%M %p").time()
    end_time = datetime.strptime("10:00 PM", "%I:%M %p").time()

    while True:
        user_time = input("Enter appointment time (HH:MM AM/PM): ").strip().upper()

        try:
            time_input = datetime.strptime(user_time, "%I:%M %p").time()
            now_time = datetime.now().time()

            if not (start_time <= time_input <= end_time):
                print(
                    "Error: Hospital working hours are from "
                    "09:00 AM to 10:00 PM."
                )
                continue

            if selected_date == today_date and time_input <= now_time:
                print(
                    "Error: This time has already passed today! "
                    "Please choose a future time."
                )
                continue

            return user_time

        except ValueError:
            print("Invalid time format! Please use HH:MM AM/PM")


class HospitalSystem:
    def __init__(self):
        self.patient = []
        self.appointment = []
        self.patient_file = BASE_DIR / "patients.csv"
        self.appointment_file = BASE_DIR / "appointments.csv"

        self.load_patient()
        self.load_appointment()

    def generate_patient_id(self):
        if not self.patient:
            return 1

        ids = [int(patient.to_dict()["ID"]) for patient in self.patient]
        return max(ids) + 1

    def generate_appointment_id(self):
        if not self.appointment:
            return 1

        ids = [
            int(appointment.to_dict()["Appointment_ID"])
            for appointment in self.appointment
        ]
        return max(ids) + 1

    def _doctor_has_conflict(
        self,
        doctor,
        date,
        time,
        exclude_appointment_id=None,
    ):
        requested_date = datetime.strptime(date, "%Y-%m-%d").date()
        requested_time = datetime.strptime(time, "%I:%M %p")

        for appointment in self.appointment:
            data = appointment.to_dict()

            if (
                exclude_appointment_id is not None
                and str(data["Appointment_ID"]) == str(exclude_appointment_id)
            ):
                continue

            if data["Status"] == "Cancelled":
                continue

            saved_date = datetime.strptime(data["Date"], "%Y-%m-%d").date()
            if (
                data["Doctor"].strip().lower() != doctor.strip().lower()
                or saved_date != requested_date
            ):
                continue

            saved_time = datetime.strptime(data["Time"], "%I:%M %p")
            difference = abs(
                (requested_time - saved_time).total_seconds() / 60
            )

            if difference < 30:
                return True

        return False

    def add_patient(self):
        print("\n--- Add New Patient ---")

        new_id = self.generate_patient_id()
        print(f"Patient ID: {new_id}")

        name = input("Enter patient name: ").strip()

        while True:
            try:
                age = int(input("Enter patient age: "))
                if age <= 0:
                    print("Invalid age! Please enter a positive number.")
                    continue
                break
            except ValueError:
                print("Age must contain numbers only!")

        phone = input("Enter phone number: ").strip()

        patient = Patient(new_id, name, age, phone)
        self.patient.append(patient)
        self.save_patient()

        print(f"Patient '{name}' added successfully!")

    def save_patient(self):
        with self.patient_file.open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Age", "Phone"])

            for patient in self.patient:
                data = patient.to_dict()
                writer.writerow(
                    [
                        data["ID"],
                        data["Name"],
                        data["Age"],
                        data["Phone"],
                    ]
                )

    def load_patient(self):
        try:
            with self.patient_file.open("r", encoding="utf-8") as file:
                reader = csv.reader(file)
                header = next(reader, None)
                if header is None:
                    return

                for row in reader:
                    if len(row) < 4:
                        continue
                    self.patient.append(
                        Patient(row[0], row[1], row[2], row[3])
                    )

        except FileNotFoundError:
            return

    def save_appointment(self):
        with self.appointment_file.open(
            "w",
            newline="",
            encoding="utf-8",
        ) as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    "Appointment_ID",
                    "Patient_ID",
                    "Doctor",
                    "Department",
                    "Date",
                    "Time",
                    "Status",
                ]
            )

            for appointment in self.appointment:
                data = appointment.to_dict()
                writer.writerow(
                    [
                        data["Appointment_ID"],
                        data["Patient_ID"],
                        data["Doctor"],
                        data["Department"],
                        data["Date"],
                        data["Time"],
                        data["Status"],
                    ]
                )

    def load_appointment(self):
        try:
            with self.appointment_file.open("r", encoding="utf-8") as file:
                reader = csv.reader(file)
                header = next(reader, None)
                if header is None:
                    return

                for row in reader:
                    if len(row) < 7:
                        continue
                    self.appointment.append(
                        Appointment(
                            row[0],
                            row[1],
                            row[2],
                            row[3],
                            row[4],
                            row[5],
                            row[6],
                        )
                    )

        except FileNotFoundError:
            return

    def book_appointment(self):
        print("\n--- Book an Appointment ---")

        while True:
            try:
                patient_id = int(input("Enter Patient ID: "))
            except ValueError:
                print("Invalid ID format! Please enter a number.")
                continue

            patient_found = None
            for patient in self.patient:
                if int(patient.to_dict()["ID"]) == patient_id:
                    patient_found = patient
                    break

            if not patient_found:
                print(
                    "Error: Patient ID not found! "
                    "Please add the patient first."
                )
                return

            print(
                f"Patient '{patient_found.to_dict()['Name']}' found!"
            )
            break

        doctor = input("Enter Doctor's Name: ").strip()
        department = input("Enter Department: ").strip()

        date = get_valid_future_date()
        time = get_valid_future_time(date)

        if self._doctor_has_conflict(doctor, date, time):
            print(
                f"Error: Dr. {doctor} is unavailable at {time}. "
                "Please leave at least a 30-minute gap "
                "between appointments."
            )
            return

        new_appointment_id = self.generate_appointment_id()
        new_appointment = Appointment(
            new_appointment_id,
            patient_id,
            doctor,
            department,
            date,
            time,
        )

        self.appointment.append(new_appointment)
        self.save_appointment()

        print(
            f"\nSuccess: Appointment (ID: {new_appointment_id}) "
            f"booked for Patient ID {patient_id} with Dr. {doctor}!"
        )

    def display_all_appointments(self):
        print("\n--- All Appointments ---")

        if not self.appointment:
            print("No appointments found!")
            return

        for appointment in self.appointment:
            data = appointment.to_dict()
            print(
                f"ID: {data['Appointment_ID']} | "
                f"Patient ID: {data['Patient_ID']} | "
                f"Doctor: {data['Doctor']} | "
                f"Department: {data['Department']} | "
                f"Date: {data['Date']} | "
                f"Time: {data['Time']} | "
                f"Status: {data['Status']}"
            )

    def search_appointments(self):
        print("\n--- Search Appointment ---")

        if not self.appointment:
            print("No appointments in the system to search!")
            return

        search_id = input("Enter Appointment ID to search: ").strip()

        for appointment in self.appointment:
            data = appointment.to_dict()
            if str(data["Appointment_ID"]) == search_id:
                print("\nAppointment Found:")
                print(
                    f"ID: {data['Appointment_ID']} | "
                    f"Patient ID: {data['Patient_ID']} | "
                    f"Doctor: {data['Doctor']} | "
                    f"Department: {data['Department']} | "
                    f"Date: {data['Date']} | "
                    f"Time: {data['Time']} | "
                    f"Status: {data['Status']}"
                )
                return

        print(f"No appointment found with ID '{search_id}'")

    def update_appointment(self):
        print("\n--- Update Appointment ---")

        if not self.appointment:
            print("No appointments available to update!")
            return

        appointment_id = input(
            "Enter Appointment ID to update: "
        ).strip()

        for appointment in self.appointment:
            data = appointment.to_dict()

            if str(data["Appointment_ID"]) != appointment_id:
                continue

            if data["Status"] != "Booked":
                print(
                    "Cannot update appointment! "
                    f"Current status is '{data['Status']}'. "
                    "Only 'Booked' appointments can be updated."
                )
                return

            print(
                f"Updating date and time for "
                f"Appointment ID '{appointment_id}'..."
            )
            new_date = get_valid_future_date()
            new_time = get_valid_future_time(new_date)

            if self._doctor_has_conflict(
                data["Doctor"],
                new_date,
                new_time,
                exclude_appointment_id=appointment_id,
            ):
                print(
                    f"Error: Dr. {data['Doctor']} is unavailable at "
                    f"{new_time}. Please leave at least a "
                    "30-minute gap between appointments."
                )
                return

            appointment.update_datetime(new_date, new_time)
            self.save_appointment()
            print("Appointment updated successfully!")
            return

        print(f"Appointment ID '{appointment_id}' not found!")

    def cancel_appointment(self):
        print("\n--- Cancel Appointment ---")

        if not self.appointment:
            print("No appointments available to cancel!")
            return

        appointment_id = input(
            "Enter Appointment ID to cancel: "
        ).strip()

        for appointment in self.appointment:
            data = appointment.to_dict()

            if str(data["Appointment_ID"]) != appointment_id:
                continue

            if data["Status"] != "Booked":
                print(
                    f"Cannot cancel! Current status is "
                    f"'{data['Status']}'."
                )
                return

            appointment.cancel_appointment()
            self.save_appointment()
            print(
                f"Appointment ID '{appointment_id}' "
                "cancelled successfully!"
            )
            return

        print(f"Appointment ID '{appointment_id}' not found!")

    def mark_appointment_completed(self):
        print("\n--- Mark Appointment Completed ---")

        if not self.appointment:
            print("No appointments available!")
            return

        appointment_id = input("Enter Appointment ID: ").strip()

        for appointment in self.appointment:
            data = appointment.to_dict()

            if str(data["Appointment_ID"]) != appointment_id:
                continue

            if data["Status"] != "Booked":
                print(
                    f"Cannot complete! Current status is "
                    f"'{data['Status']}'."
                )
                return

            appointment.mark_as_completed()
            self.save_appointment()
            print(
                f"Appointment ID '{appointment_id}' "
                "marked as completed!"
            )
            return

        print(f"Appointment ID '{appointment_id}' not found!")

    def display_doctor_schedule(self):
        print("\n--- Doctor Schedule ---")

        if not self.appointment:
            print("No appointments in the system!")
            return

        doctor_name = input("Enter Doctor's Name: ").strip()
        date = get_valid_future_date()

        print(f"\nSchedule for Dr. {doctor_name} on {date}:")
        found = False

        for appointment in self.appointment:
            data = appointment.to_dict()
            if (
                data["Doctor"].strip().lower()
                == doctor_name.strip().lower()
                and data["Date"] == date
            ):
                print(
                    f"Time: {data['Time']} | "
                    f"Patient ID: {data['Patient_ID']} | "
                    f"Status: {data['Status']}"
                )
                found = True

        if not found:
            print("No appointments found for this doctor on this date.")

    def save_data(self):
        self.save_patient()
        self.save_appointment()
        print("\nAll data saved successfully to CSV files!")
