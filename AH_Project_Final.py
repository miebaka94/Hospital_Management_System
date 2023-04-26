# Written by Austin, Abbey, and Miebaka
# CPRG-216-E [2023-04-25]
########################################################################################################################
# Doctor Class
class Doctor:
    def __init__(self, D_ID=None, D_Name=None, D_Spec=None, D_Time=None,
                 D_Qual=None, D_Room=None):
        self.doctor_id = D_ID
        self.name = D_Name
        self.specialization = D_Spec
        self.working_time = D_Time
        self.qualification = D_Qual
        self.room_number = D_Room

    # Doctor getters
    def get_doctor_id(self):
        return self.doctor_id

    def get_name(self):
        return self.name

    def get_specialization(self):
        return self.specialization

    def get_working_time(self):
        return self.working_time

    def get_qualification(self):
        return self.qualification

    def get_room_number(self):
        return self.room_number

    # Doctor Setters
    def set_doctor_id(self, new_id):
        self.doctor_id = new_id
        return new_id

    def set_name(self, new_name):
        self.name = new_name
        return new_name

    def set_specialization(self, new_specialization):
        self.specialization = new_specialization
        return new_specialization

    def set_working_time(self, new_working_time):
        self.working_time = new_working_time
        return new_working_time

    def set_qualification(self, new_qualification):
        self.qualification = new_qualification
        return new_qualification

    def set_room_number(self, new_room_number):
        self.room_number = new_room_number
        return new_room_number

    def __str__(self):
        return f'{self.doctor_id}_{self.name}_{self.specialization}_{self.working_time}_' \
               f'{self.qualification}_{self.room_number}'


########################################################################################################################

# Doctor_Manager Class
class Doctor_Manager:
    def __init__(self):
        self.doctors = []  # makes an empty list when it constructs
        self.doctors = self.read_doctors_file()

    def format_dr_info(self, doctor):
        formatted_doctor = Doctor(doctor)
        return f"{formatted_doctor}"

    # Edits Dr Info
    def enter_dr_info(self):
        N_D_ID = input("Enter the doctor's ID: \n")
        N_D_Name = input("Enter the doctor's name: \n")
        N_D_Spec = input("Enter the doctor's speciality: \n")
        N_D_Time = input("Enter the doctor's available time: \n")
        N_D_Qual = input("Enter the doctor's qualification: \n")
        N_D_Room = input("Enter the doctor's room number: \n")

        N_D = Doctor(N_D_ID, N_D_Name, N_D_Spec, N_D_Time, N_D_Qual, N_D_Room)
        return N_D

    # Parses data from lines on the .txt file and imports them into an object
    def read_doctors_file(self):
        D_List = []
        file = open('doctors.txt', 'r')
        for line in file:
            Part = line.strip().split('_')
            D_ID = Part[0]  # assigns the split data into the list by number
            D_Name = Part[1]
            D_Spec = Part[2]
            D_Time = Part[3]
            D_Qual = Part[4]
            D_Room = Part[5]
            Read_D = Doctor(D_ID, D_Name, D_Spec, D_Time, D_Qual, D_Room)
            D_List.append(Read_D)
        return D_List

    def display_doctors_list(self):
        for doctor in self.doctors:
            print(self.display_doctor_info(doctor))

    def write_list_of_doctors_to_file(self):
        file = open("doctors.txt", "w")
        for doctor in self.doctors:
            file.write(f"{doctor}\n")

    def add_dr_to_file(self):
        new_doctor = self.enter_dr_info()
        self.doctors.append(new_doctor)
        file = open("doctors.txt", "a")
        file.write(f"\n{new_doctor}")
        print(f"Doctor with ID# {new_doctor.get_doctor_id()} was added to file")

    def search_doctor_by_id(self):
        display_doctor = None
        found_doctor = None
        search_id = input("Enter Doctor ID: \n")
        for doctor in self.doctors:
            if doctor.get_doctor_id() == search_id:
                found_doctor = True
                display_doctor = self.display_doctor_info(doctor)
                break
            else:
                found_doctor = False
                continue
        if found_doctor:
            return print(display_doctor)
        else:
            print("Unable to find doctor with this ID")

    def search_doctor_by_name(self):
        display_doctor = None
        found_doctor = None
        search_name = input("Enter Doctor name: \n")
        search_doctor = search_name.strip()
        for doctor in self.doctors:
            strip_doctor = doctor.get_name()
            if strip_doctor.strip() == search_doctor:
                found_doctor = True
                display_doctor = self.display_doctor_info(doctor)
                break
            else:
                found_doctor = False
                continue
        if found_doctor:
            return print(display_doctor)
        else:
            print("Unable to find doctor with this name")

    def edit_doctor_info(self):
        search_id = input("Enter ID# of the doctor that you wish to edit: \n")
        for doctor in self.doctors:
            if doctor.get_doctor_id() == search_id:
                N_D_Name = input("Enter new name: \n")
                N_D_Spec = input("Enter new speciality: \n")
                N_D_Time = input("Enter new timing: \n")
                N_D_Qual = input("Enter new qualification: \n")
                N_D_Room = input("Enter new room number: \n")
                doctor.set_name(N_D_Name)
                doctor.set_specialization(N_D_Spec)
                doctor.set_working_time(N_D_Time)
                doctor.set_qualification(N_D_Qual)
                doctor.set_room_number(N_D_Room)
                self.write_list_of_doctors_to_file()
                return print(f"Doctor whose ID is {search_id} has been edited")
            else:
                continue

    def display_doctor_info(self, doctor):
        return f'{doctor.get_doctor_id():<5} {doctor.get_name():<20} {doctor.get_specialization():<15}' \
               f'{doctor.get_working_time():<15} {doctor.get_qualification():<15} ' \
               f'{doctor.get_room_number()}\n'


########################################################################################################################
# Patient Class
class Patient:
    def __init__(self, P_ID=None, P_Name=None, Disease=None, Gender=None, Age=None):
        self.P_ID = P_ID
        self.P_Name = P_Name
        self.P_Disease = Disease
        self.P_Gender = Gender
        self.P_Age = Age

    # Patient Getters
    def get_p_id(self):
        return self.P_ID

    def get_p_name(self):
        return self.P_Name

    def get_disease(self):
        return self.P_Disease

    def get_gender(self):
        return self.P_Gender

    def get_age(self):
        return self.P_Age

    # Patient Setters
    def set_p_id(self, N_P_ID):
        self.P_ID = N_P_ID
        return N_P_ID

    def set_p_name(self, N_P_Name):
        self.P_Name = N_P_Name
        return N_P_Name

    def set_disease(self, N_P_Disease):
        self.P_Disease = N_P_Disease
        return N_P_Disease

    def set_gender(self, N_P_Gender):
        self.P_Gender = N_P_Gender
        return N_P_Gender

    def set_age(self, N_P_Age):
        self.P_Age = N_P_Age
        return N_P_Age

    def __str__(self):
        return f'{self.P_ID}_{self.P_Name}_{self.P_Disease}_{self.P_Gender}_{self.P_Age}'


########################################################################################################################
# Patient_Manager Class
class PatientManager:
    def __init__(self):
        self.Patient = []
        self.Patient = self.read_patient_file()

        # Makes a new Patient Object

    def enter_patient_info(self):
        N_P_ID = input("Enter Patient ID: \n")
        N_P_Name = input("Enter Patient Name: \n")
        N_P_Disease = input("Enter Patient Disease: \n")
        N_P_Gender = input("Enter Patient Gender: \n")
        N_P_Age = input("Enter Patient Age: \n")
        N_Patient = Patient(N_P_ID, N_P_Name, N_P_Disease, N_P_Gender, N_P_Age)
        return N_Patient

    def display_patient_list(self):
        for patient in self.Patient:
            print(self.display_patient_info(patient))

    def write_list_of_patients_to_file(self):
        file = open("patients.txt", "w")
        for patient in self.Patient:
            file.write(f"{patient}\n")

    def format_patient_info(self, patient):
        formatted_patients = Patient(patient)
        return formatted_patients

    # Pulls info off the Patient file and attributes it to an object
    def read_patient_file(self):
        patient_list = []
        file = open('patients.txt', 'r')
        for line in file:
            data = line.strip().split('_')
            p_id = data[0]
            p_name = data[1]
            disease = data[2]
            gender = data[3]
            age = data[4]
            read_patient = Patient(p_id, p_name, disease, gender, age)
            patient_list.append(read_patient)
        return patient_list

    # Searches by PID for an oject
    def search_patient_by_id(self):
        display_patient = None
        found_patient = None
        search_id = input("Please enter Patient ID: \n")
        for patient in self.Patient:
            if patient.get_p_id() == search_id:
                found_patient = True
                display_patient = self.display_patient_info(patient)
                break
            else:
                found_patient = False
                continue
        if found_patient:
            return print(display_patient)
        else:
            print("Unable to find Patient with that ID#")

    def display_patient_info(self, patient):
        return f'{patient.get_p_id():<5} {patient.get_p_name():<20} {patient.get_disease():<15} ' \
               f'{patient.get_gender():<15} {patient.get_age():<15}\n'

    # Finds patient by PID then edits the object
    def edit_patient_info(self):
        search_p_id = input("Please enter the id of the Patient that you want to edit their information: \n")
        for patient in self.Patient:
            if patient.get_p_id() == search_p_id:
                N_P_Name = input("Enter new Name: \n")
                N_Disease = input("Enter new disease: \n")
                N_Gender = input("Enter new gender: \n")
                N_Age = input("Enter new age: \n")
                patient.set_p_name(N_P_Name)
                patient.set_disease(N_Disease)
                patient.set_gender(N_Gender)
                patient.set_age(N_Age)
                self.write_list_of_patients_to_file()
                return print(f'Patient with ID# {search_p_id} had been edited')
            else:
                continue

    def add_patient_to_file(self):
        N_Patient = self.enter_patient_info()
        self.Patient.append(N_Patient)
        file = open("patients.txt", "a")
        file.write(f"\n{N_Patient}")
        print(f"Patient whose ID is {N_Patient.get_p_id()} was added to file")


########################################################################################################################
# Manager Class (also menu)
class Manager:

    def display_menu(self):
        while True:
            print("[Welcome to Alberta Hospital (AH) Management system]")
            print("[Select from the following options, or select 3 to stop:]")
            print("[1] - Doctors")
            print("[2] - Patients")
            print("[3] - Exit Program")
            main_input = input("...")

            if main_input == "1":
                while True:
                    print("[Doctors Menu:]")
                    print("[1] - Display Doctors list")
                    print("[2] - Search for doctor by ID")
                    print("[3] - Search for doctor by name")
                    print("[4] - Add doctor")
                    print("[5] - Edit doctor info")
                    print("[6] - Back to the Main Menu")
                    doctors_input = input("...")

                    if doctors_input == "1":
                        doctor_manager = Doctor_Manager()
                        doctor_manager.display_doctors_list()
                        continue

                    elif doctors_input == "2":
                        doctor_manager = Doctor_Manager()
                        doctor_manager.search_doctor_by_id()
                        continue

                    elif doctors_input == "3":
                        doctor_manager = Doctor_Manager()
                        doctor_manager.search_doctor_by_name()
                        continue

                    elif doctors_input == "4":
                        doctor_manager = Doctor_Manager()
                        doctor_manager.add_dr_to_file()
                        continue

                    elif doctors_input == "5":
                        doctor_manager = Doctor_Manager()
                        doctor_manager.edit_doctor_info()
                        continue

                    elif doctors_input == "6":
                        break

                    else:
                        print("Invalid Input")
                        continue

            elif main_input == "2":
                while True:
                    print("[Patient Menu:]")
                    print("[1] - Display patient list")
                    print("[2] - Search for patient by ID")
                    print("[3] - Add patient")
                    print("[4] - Edit patient info")
                    print("[5] - Back to the Main Menu")
                    patient_input = input("...")

                    if patient_input == "1":
                        patient_manager = PatientManager()
                        patient_manager.display_patient_list()
                        continue

                    elif patient_input == "2":
                        patient_manager = PatientManager()
                        patient_manager.search_patient_by_id()
                        continue

                    elif patient_input == "3":
                        patient_manager = PatientManager()
                        patient_manager.add_patient_to_file()
                        continue

                    elif patient_input == "4":
                        patient_manager = PatientManager()
                        patient_manager.edit_patient_info()
                        continue

                    elif patient_input == "5":
                        break

                    else:
                        print("Invalid Input")
                        continue

            elif main_input == "3":
                print("[Exiting Program]")
                break

            else:
                print("Enter valid input")
                continue


# ran into some trouble with this but don't change the 1 out of it, it allows it to initialize the menu
Manager.display_menu(1)
