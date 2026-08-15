from datetime import datetime
import csv


#Patient Class
class Patient:
    def __init__ (self,patient_id,name,age,phone):
        self.__patient_id = patient_id
        self.__name = name
        self.__age = age
        self.__phone = phone

    def to_dict(self):
        patient_data = {'ID':self.__patient_id,'Name':self.__name,'Age':self.__age,'Phone':self.__phone}

        return patient_data

#Appointment Class
class Appointment:
    def __init__(self,appointment_id,patient_id,doctor,department,date,time,status ='Booked'):
        self.__appointment_id= appointment_id
        self.__patient_id = patient_id
        self.__doctor=doctor
        self.__department = department
        self.__date = date
        self.__time = time
        self.__status = status

    
    def update_datetime(self,new_date,new_time):
        self.__date = new_date
        self.__time = new_time

    def mark_as_completed(self):
        self.__status = 'Completed'

    def cancel_appointment(self):
        self.__status = 'Cancelled'


    def to_dict(self):
        appointment_data = {'Appointment_ID':self.__appointment_id,
                            'Patient_ID':self.__patient_id,'Doctor':self.__doctor,
                            'Department':self.__department,'Date':self.__date,
                            'Time':self.__time,'Status':self.__status
                            }

        return appointment_data



#Get Date Function       
def get_valid_future_date():
    while True:
        user_input = input('Enter appointment date (YYYY-MM-DD): ').strip()
        try:
            date_input = datetime.strptime(user_input,'%Y-%m-%d').date()

            today_date = datetime.now().date()

            if date_input < today_date :
                print("Error: You cannot book an appointment in the past!")
            else:
                return user_input

        except ValueError:
            print("Invalid date format! Please use YYYY-MM-DD")



#Get Time Function
def get_valid_future_time(selected_user_date):

    selected_date = datetime.strptime(selected_user_date,'%Y-%m-%d').date()
    today_date = datetime.now().date()

    start_time = datetime.strptime('09:00 AM','%I:%M %p').time()
    end_time   = datetime.strptime('10:00 PM','%I:%M %p').time()

    while True:
        user_time = input('Enter appointment time (HH:MM AM/PM): ').strip().upper()

        try:
            time_input = datetime.strptime(user_time,'%I:%M %p').time()

            now_time = datetime.now().time()

            if not ( time_input <= end_time and time_input >= start_time): #   end_time >= time_input >= start_time
                print('Error: Hospital working hours are from 09:00 AM to 10:00 PM.')
                continue

            if selected_date == today_date and time_input <= now_time :
                print('Error: This time has already passed today! Please choose a future time.')
                continue


            return user_time

        except ValueError:
            print('Invalid time format! Please use HH:MM AM/PM')







# HospitalSystem Class

class HospitalSystem:
    def __init__(self):
        self.patient = []
        self.appointment = []
        self.patient_file = 'patients.csv'
        self.appointment_file = 'appointments.csv'

        self.load_patient()
        self.load_appointment()



    def generate_patient_id(self):
        IDs=[]
        if len(self.patient) == 0:
            return 1
        else:
            for patient in self.patient:
                IDs.append(int(patient.to_dict()['ID']))
            return max(IDs)+1     
        

    def generate_appointment_id(self):
            IDs=[]
            if len(self.appointment) == 0:
                return 1
            else:
                for appointment in self.appointment:
                    IDs.append(int(appointment.to_dict()['Appointment_ID']))
                return max(IDs)+1  


    def add_patient(self):
        print("\n--- Add New Patient ---")

        new_id = self.generate_patient_id()
        print(f"Patient ID: {new_id}")

        name = input('Enter your name:')

        while True:
            try:
                age = int(input('Enter your age:'))
                if age<0:
                    print('Invalid age! Please enter a valid positive number.')
                    continue
                elif age==0:
                    print('Invalid age! Age cannot be Zero.')
                    continue

                break

            except ValueError:
                print('Age Must be numbers only!')


        phone = input('Enter your phone number:')

        patient = Patient(new_id,name,age,phone)
        self.patient.append(patient)
        self.save_patient()

        print(f"Patient '{name}' added successfully!")




    def save_patient(self):
        with open(self.patient_file,'w',newline='') as f:
            g = csv.writer(f)
            g.writerow(['ID','Name','Age','Phone'])
            for patient in self.patient:
                data = patient.to_dict()
                row = [data['ID'],data['Name'],data['Age'],data['Phone']]
                g.writerow(row)



    def load_patient(self):

        try:
            with open(self.patient_file,'r') as f:
                g = csv.reader(f)

                header=next(g,0)
                if header == 0:
                    return 

                
                for row in g:
                    data = Patient(row[0],row[1],row[2],row[3])
                    self.patient.append(data)

        except FileNotFoundError:
            print('Cannot find the file!')



    def save_appointment(self):
        with open(self.appointment_file,'w',newline='') as f:
            g = csv.writer(f)
            g.writerow(['Appointment_ID','Patient_ID','Doctor','Department','Date','Time','Status'])
            for appointment in self.appointment:
                data = appointment.to_dict()
                row = [data['Appointment_ID'],data['Patient_ID'],data['Doctor'],data['Department'],data['Date'],data['Time'],data['Status']]
                g.writerow(row)


    def load_appointment(self):
        try:
            with open(self.appointment_file,'r') as f:
                g = csv.reader(f)

                header=next(g,0)
                if header == 0:
                    return 
                
                for row in g:
                    data = Appointment(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
                    self.appointment.append(data)

        except FileNotFoundError:
            print('Cannot find the file!')



    def book_appointment(self):
        print("\n--- Book an Appointment ---")
        while True:
            try:
                p_id = int(input('Enter Patient ID:'))
            except ValueError:
                print("Invalid ID format! Please enter a number.")
                continue

            patient_found =False

            for patient in self.patient:
                if int(patient.to_dict()['ID']) == p_id:
                    patient_found = True
                    print(f"Patient '{patient.to_dict()['Name']}' found!") 
                    break


            if not patient_found:
                print("Error: Patient ID not found! Please add the patient first.")
                return
            else:
                break



        doctor = input("Enter Doctor's Name: ")
        department = input("Enter Department: ")


        date = get_valid_future_date()
        time = get_valid_future_time(date)


        user_date = datetime.strptime(date,'%Y-%m-%d').date()

        new_t = datetime.strptime(time, "%I:%M %p")

        conflict = False
        for appt in self.appointment:
            appt_data = appt.to_dict()

            saved_date = datetime.strptime(appt_data['Date'],'%Y-%m-%d').date()

            if (appt_data['Doctor'].lower().strip() == doctor.lower().strip() and 
                saved_date== user_date and 
                appt_data['Status'] != 'Cancelled'):

                saved_t = datetime.strptime(appt_data['Time'], "%I:%M %p")

                diff_in_minutes = abs((new_t - saved_t).total_seconds() / 60)

                if diff_in_minutes < 30:
                    conflict = True
                    break
                


        if conflict:
            print(f"Error: Dr. {doctor} is unavailable at {time}. Please leave at least a 30-minute gap between appointments.")
            return


        new_appt_id = self.generate_appointment_id()

        new_appointment = Appointment(new_appt_id, p_id, doctor, department, date, time)

        self.appointment.append(new_appointment)

        self.save_appointment()

        print(f"\nSuccess: Appointment (ID: {new_appt_id}) booked for Patient ID {p_id} with Dr. {doctor}!") 



    def display_all_appointments(self):
        print("\n--- All Appointments ---")

        if len(self.appointment) == 0:
            print("No appointments found!")
            return

        for appt in self.appointment:
            data = appt.to_dict()
            print(f"ID: {data['Appointment_ID']} | Patient ID: {data['Patient_ID']} | Doctor: {data['Doctor']} | Department: {data['Department']} | Date: {data['Date']} | Time: {data['Time']} | Status: {data['Status']}")



    def search_appointments(self):
        print("\n--- Search Appointment ---")

        if len(self.appointment) == 0:
            print("No appointments in the system to search!")
            return

        search_id = input("Enter Appointment ID to search: ").strip()
        found = False

        for appt in self.appointment:
            data = appt.to_dict()
            if str(data['Appointment_ID']) == str(search_id):
                print("\nAppointment Found:")
                print(f"ID: {data['Appointment_ID']} | Patient ID: {data['Patient_ID']} | Doctor: {data['Doctor']} | Department: {data['Department']} | Date: {data['Date']} | Time: {data['Time']} | Status: {data['Status']}")
                found = True
                break

        if not found:
            print(f"No appointment found with ID '{search_id}'")  


    def update_appointment(self):
        print("\n--- Update Appointment ---")

        if len(self.appointment) == 0:
            print("No appointments available to update!")
            return

        app_id = input("Enter Appointment ID to update: ").strip()

        for appt in self.appointment:
            data = appt.to_dict()
            if str(data['Appointment_ID']) == str(app_id):
                if data['Status'] != 'Booked':
                    print(f"Cannot update appointment! Current status is '{data['Status']}'. Only 'Booked' appointments can be updated.")
                    return

                print(f"Updating date and time for Appointment ID '{app_id}'...")
                new_date = get_valid_future_date()
                new_time = get_valid_future_time(new_date)

                appt.update_datetime(new_date,new_time)

                self.save_appointment()
                print("Appointment updated successfully!")
                return

        print(f"Appointment ID '{app_id}' not found!") 



    def cancel_appointment(self):
        print("\n--- Cancel Appointment ---")

        if len(self.appointment) == 0:
            print("No appointments available to cancel!")
            return

        app_id = input("Enter Appointment ID to cancel: ").strip()

        for appt in self.appointment:
            data = appt.to_dict()
            if str(data['Appointment_ID']) == str(app_id):
                if data['Status'] != 'Booked':
                    print(f"Cannot cancel! Current status is '{data['Status']}'.")
                    return


                appt.cancel_appointment()
                self.save_appointment()

                print(f"Appointment ID '{app_id}' cancelled successfully!")
                return

        print(f"Appointment ID '{app_id}' not found!")


    def mark_appointment_completed(self):
        print("\n--- Mark Appointment Completed ---")

        if len(self.appointment) == 0:
            print("No appointments available!")
            return

        app_id = input("Enter Appointment ID: ").strip()

        for appt in self.appointment:
            data = appt.to_dict()
            if str(data['Appointment_ID']) == str(app_id):
                if data['Status'] != 'Booked':
                    print(f"Cannot complete! Current status is '{data['Status']}'.")
                    return
                
                appt.mark_as_completed()
                self.save_appointment()

                print(f"Appointment ID '{app_id}' marked as completed!")
                return

        print(f"Appointment ID '{app_id}' not found!")



    def display_doctor_schedule(self):
        print("\n--- Doctor Schedule ---")
        if len(self.appointment) == 0:
            print("No appointments in the system!")
            return

        doc_name = input("Enter Doctor's Name: ").strip()
        date = get_valid_future_date()

        found = False
        print(f"\nSchedule for Dr. {doc_name} on {date}:")
        for appt in self.appointment:
            data = appt.to_dict()
            if data['Doctor'].lower() == doc_name.lower() and data['Date'] == date:
                print(f"Time: {data['Time']} | Patient ID: {data['Patient_ID']} | Status: {data['Status']}")
                found = True

        if not found:
            print("No appointments found for this doctor on this date.")




    def save_data(self):
        self.save_patient()
        self.save_appointment()
        print("\nAll data saved successfully to CSV files!")