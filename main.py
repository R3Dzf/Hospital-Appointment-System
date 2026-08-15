import operations as op
import visualization as vs
import analysis as an
import matplotlib.pyplot as plt

plt.style.use('Solarize_Light2')


hospital = op.HospitalSystem()

def showmenu():

    while True:
        print('------------------ Welcome to Hospital Appointment System Menu ------------------')
        print('1. Add a patient')
        print('2. Book an appointment')
        print('3. Display all appointments')
        print('4. Search appointments')
        print('5. Update an appointment')
        print('6. Cancel an appointment')
        print('7. Mark an appointment completed')
        print('8. Display a doctor schedule')
        print('9. Analyze appointment data')
        print('10. Show appointment charts')
        print('11. Save data')
        print('12. Exit')



        choice = input('Enter your choice from the above menu (1-12):')

        if choice == '1':
            hospital.add_patient()
            
        elif choice == '2':
            hospital.book_appointment()
            
        elif choice == '3':
            hospital.display_all_appointments()
            
        elif choice == '4':
            hospital.search_appointments()
            
        elif choice == '5':
            hospital.update_appointment()
            
        elif choice == '6':
            hospital.cancel_appointment()
            
        elif choice == '7':
            hospital.mark_appointment_completed()
            
        elif choice == '8':
            hospital.display_doctor_schedule()
            

        elif choice == '9':
            an.run_all()
            
            
        elif choice == '10':
            vs.show_appointment_charts()

        elif choice == '11':
            hospital.save_data()
            
        elif choice== '12':
            print('Good Bye!')
            break
        else:
            print('Invalid choice')


        input('Press Enter to Continue......')    
    

showmenu()