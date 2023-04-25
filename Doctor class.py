# Doctor Class
class Doctor:
    def __init__(self, Doctor_ID, Doctor_Name, Doctor_Spec, Doctor_Time, Doctor_Qual, Doctor_Room):
        self.Doctor_ID = Doctor_ID
        self.Doctor_Name = Doctor_Name
        self.Doctor_Spec = Doctor_Spec
        self.Doctor_Time = Doctor_Time
        self.Doctor_Qual = Doctor_Qual
        self.Doctor_Room = Doctor_Room

    def get_doctor_id(self):
        return self.Doctor_ID

    def get_doctor_name(self):
        return self.Doctor_Name

    def get_doctor_spec(self):
        return self.Doctor_Spec

    def get_doctor_time(self):
        return self.Doctor_Time

    def get_doctor_qual(self):
        return self.Doctor_Qual

    def get_doctor_room(self):
        return self.Doctor_Room

    def set_doctor_id(self, N_ID):
        self.Doctor_ID = N_ID

    def set_doctor_name(self, N_Name):
        self.Doctor_Name = N_Name

    def set_doctor_spec(self, N_Spec):
        self.Doctor_Spec = N_Spec

    def set_doctor_time(self, N_Time):
        self.Doctor_Time = N_Time

    def set_doctor_qual(self, N_Qual):
        self.Doctor_Qual = N_Qual

    def set_doctor_room(self, N_Room):
        self.Doctor_Room = N_Room

    def __str__(self):
        return str({self.Doctor_ID}, "_", {self.Doctor_Name}, "_", {self.Doctor_Spec}, "_", {self.Doctor_Time}, "_", {self.Doctor_Qual}, "_", {self.Doctor_Room})

# Doctor Manager Class
class Doctor_Manager:
    def __init__(self):
        self.Doctors = []
        self.Load_Doctors

    def format_dr_info(self, dr):
        return str(dr)

    def enter_dr_info(self):
        dr_id = input("Enter Doctor's ID: \n")
        dr_name = input("Enter Doctor's Name: \n")
        dr_spec = input("Enter Doctor's Specilization: \n")
        dr_time = input("Enter Doctor's Work Time: \n")
        dr_qual = input("Enter Doctor's Qualifications: \n")
        dr_room = input("Enter Doctor's Room: \n")
        d_info = Doctor(dr_id, dr_name, dr_spec, dr_time, dr_qual, dr_room)
        return d_info

    def load_doctors(self):
        dr_data = []
        for x in dr_data:
            dr_id, dr_name, dr_spec, dr_time, dr_qual, dr_room = x.strip().split('_')
            dr = Doctor(dr_id, dr_name, dr_spec, dr_time, dr_qual, dr_room)
            self.Doctor.append(dr)

    def search_doctor_by_name(self, dr_name):
        for dr in self.Doctor:
            if dr.get_doctor_name() == dr_name:
                return dr
            return None

    def search_doctor_by_id(self, dr_id):
        for dr in self.Doctor:
            if dr.get_doctor_id() == dr_id:
                return dr
            return None

    def display_doctor_info(self, dr):
        if dr:
            print("ID, Name, Speciality, Time, Qualifications, Room Number")
            print(f'{Doctor.dr_id} {Doctor.dr_name} {Doctor.dr_spec} {Doctor.dr_time} {Doctor.dr_qual} {Doctor.dr_room}')
        else:
            print("unable to find Doctor")

    def edit_doctor_info(self, dr):
        print("Enter new info for the Doctor (leave blank to make no changes)")
        new_dr_id = input("Enter the new ID: \n")
        new_dr_name = input("Enter the new Name: \n")
        new_dr_spec = input("Enter the new Specilization: \n")
        new_dr_time = input("Enter the new Time: \n")
        new_dr_qual = input("Enter the new Qualifications: \n")
        new_dr_room = input("Enter the new Room #: \n")
        if new_dr_id:
            Doctor.set_doctor_id(new_dr_id)
        if new_dr_name:
            Doctor.set_doctor_name(new_dr_name)
        if new_dr_spec:
            Doctor.set_doctor_spec(new_dr_spec)
        if new_dr_time:
            Doctor.set_doctor_time(new_dr_time)
        if new_dr_qual:
            Doctor.set_doctor_qual(new_dr_qual)
        if new_dr_room:
            Doctor.set_doctor_room(new_dr_room)
