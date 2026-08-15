import pandas as pd
import matplotlib.pyplot as plt

def show_appointment_charts():
    print("\n--- Charts Dashboard ---")
    try:
        df = pd.read_csv('appointments.csv')
    except FileNotFoundError:
        print("Error: appointments.csv not found!")
        return

    if df.empty:
        print("No appointments to visualize!")
        return


    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Hospital Appointments Dashboard', fontsize=18, fontweight='bold')


   
    doctor_count = df.groupby('Doctor')['Appointment_ID'].count()
    axs[0, 0].bar(doctor_count.index, doctor_count.values, color='lime', edgecolor='black')
    axs[0, 0].set_title('Appointments per Doctor')
    axs[0, 0].set_ylabel('Appointments')
    axs[0,0].tick_params(axis = 'x', rotation = 45)


    daily_counts = df.groupby('Date')['Appointment_ID'].count()
    axs[0, 1].bar(daily_counts.index, daily_counts.values, color='skyblue', edgecolor='black')
    axs[0, 1].set_title('Appointments per Day')
    axs[0, 1].tick_params(axis='x', rotation=30) 



    status_count = df.groupby('Status')['Appointment_ID'].count()
    my_explode = [0.1] * 3
    axs[1, 0].pie(status_count.values, labels=status_count.index, explode=my_explode, autopct='%1.1f%%', colors=['skyblue', 'thistle', 'pink'])
    axs[1, 0].set_title('Appointment Statuses')


    demand = df.groupby('Department')['Appointment_ID'].count()
    axs[1, 1].bar(demand.index, demand.values, color='indianred', edgecolor='k')
    axs[1, 1].set_title('Department Demand')
    axs[1, 1].set_ylabel('Appointments')
    axs[1, 1].tick_params(axis='x', rotation=30) 


    plt.tight_layout()
    
    plt.show()
