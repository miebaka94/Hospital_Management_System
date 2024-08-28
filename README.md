Alberta Hospital Management System
Overview
The Alberta Hospital Management System is a Python-based program designed to manage doctors and patients within a hospital environment. The system allows users to perform various operations such as adding, editing, and searching for doctors and patients. This README file provides an overview of the project's structure, functionality, and usage instructions.

Project Structure
The project consists of the following classes:

Doctor Class: Manages individual doctor information such as ID, name, specialization, working hours, qualifications, and room number.
Doctor Manager Class: Manages a collection of doctors, including loading, searching, adding, editing, and displaying doctor information.
Patient Class: Manages individual patient information such as ID, name, disease, gender, and age.
Patient Manager Class: Manages a collection of patients, including loading, searching, adding, editing, and displaying patient information.
Key Features
Doctor Management:

Add new doctors.
Search for a doctor by name or ID.
Edit existing doctor information.
Display doctor details.
Patient Management:

Add new patients.
Search for a patient by ID.
Edit existing patient information.
Display patient details (Note: Implementation incomplete).
Menu-driven Interface:

The program offers a simple text-based menu interface that guides users through different options.
Usage
Running the Program:

Run the main script in a Python environment. The program will start with a welcome message and a menu that allows you to select between managing doctors, patients, or exiting the program.
Menu Options:

Main Menu:

1 - Doctors: Navigate to the Doctors Menu.
2 - Patients: Navigate to the Patients Menu (Note: Not fully implemented).
3 - Exit Program: Exit the application.
Doctors Menu:

1 - Display Doctors list: Display all doctors in the system.
2 - Search for doctor by ID: Search and display a doctor by their ID.
3 - Search for doctor by name: Search and display a doctor by their name.
4 - Add doctor: Add a new doctor to the system.
5 - Edit doctor info: Edit information for an existing doctor.
6 - Back to the Main Menu: Return to the main menu.
Patients Menu:

The Patient menu is not yet fully implemented and will display a message indicating this.
Adding and Editing Information:

When adding or editing doctors, the program will prompt you to input the relevant information (e.g., ID, name, specialization, etc.). You can leave fields blank during editing if you do not wish to change the existing information.
Known Issues and Limitations
The Patient_Manager class is partially implemented and does not yet support full functionality for managing patients.
The program currently does not persist data across sessions; it only manages data during runtime.
The search functions in both Doctor_Manager and Patient_Manager classes return None if the first entry does not match, rather than continuing the search through the list.
Error handling and input validation are limited. The program expects correct input types.
Future Enhancements
Implement file reading and writing to persist doctor and patient data across sessions.
Complete the implementation of the Patient_Manager class.
Improve the user interface with better input validation and error handling.
Add more detailed search and filtering options for doctors and patients.
Requirements
Python 3.x
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any questions or suggestions, please contact Miebaka Semenitari at [semenitari@icloud.com].

