import operations
import numpy as np
import pandas as pd


analysis = operations.HospitalSystem()



def average_patient_age():

    if len(analysis.patient) == 0:
        print('There is no patient\'s')
        return


    df = pd.read_csv('patients.csv')

    print(f'Average Patient Age is : {df['Age'].mean()} year')


def analyze_appointment_data():
      
    if len(analysis.appointment) == 0:
        print('There is no appointment\'s')
        return

    df = pd.read_csv('appointments.csv')

    daily_counts = df.groupby('Date')['Appointment_ID'].count()

    avg_per_day = np.mean(daily_counts)

    max_per_day = np.max(daily_counts)

    busiest_days = daily_counts[daily_counts == max_per_day].index


    print(f"Average appointments per day: {avg_per_day:.2f}")
    print(f"Max appointments per day: {max_per_day}  | On Day :", *list(busiest_days))


def  cancellation_and_completion_percentages():
    if len(analysis.appointment) == 0:
            print('There is no appointment\'s')
            return

    df = pd.read_csv('appointments.csv')

    total_appointments = len(df)

    cancelled_days = len(df[df['Status'] == 'Cancelled'])
    completed_days = len(df[df['Status'] == 'Completed'])

    print(f"Completed Percentage : {(completed_days/total_appointments)*100:.2f} % and It's Count is : {completed_days}")
    print(f"Cancellation Percentage : {(cancelled_days/total_appointments)*100:.2f} % and It's Count is : {cancelled_days}")


def operation_appointments():
    if len(analysis.appointment) == 0:
        print('There is no appointment\'s')
        return

    df = pd.read_csv('appointments.csv')

    df['Real_Time'] = pd.to_datetime(df['Date']+' '+df['Time'])

    df = df.sort_values(by='Real_Time')
    df = df.drop('Real_Time',axis=1)


    print('--------------------------- Sorted Appointments by Date and Time ---------------------------')
    print(df.query("Status == 'Booked'").head(10).to_string(index=False))


    app = pd.read_csv('appointments.csv')
    pat = pd.read_csv('patients.csv')
    merged = pd.merge(app,pat , left_on ='Patient_ID',right_on='ID')


    print()
    print('------------ Merged Patients and Appointments ------------')
    print(merged[['Name', 'Doctor', 'Date', 'Time']].head(10).to_string(index=False))




def run_all():
    print("""
            =====================================================
                 SYSTEM DATA ANALYSIS & PERFORMANCE REPORT 
            =====================================================
          """)
    
    print("Analyzing data... Please wait...\n")
    average_patient_age()
    analyze_appointment_data()
    cancellation_and_completion_percentages()
    operation_appointments()





    

