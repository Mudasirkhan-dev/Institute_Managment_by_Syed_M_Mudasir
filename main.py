import tkinter as tk
from tkinter import ttk

class InstituteConfigurationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Institute Configuration App")

        # Data storage
        self.faculty_data = []
        self.department_data = []
        self.campus_data = []
        self.building_data = []
        self.room_data = []

        # Create tabs
        self.notebook = ttk.Notebook(root)
        self.faculty_tab = ttk.Frame(self.notebook)
        self.department_tab = ttk.Frame(self.notebook)
        self.campus_tab = ttk.Frame(self.notebook)
        self.building_tab = ttk.Frame(self.notebook)
        self.room_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.faculty_tab, text="Faculty")
        self.notebook.add(self.department_tab, text="Department")
        self.notebook.add(self.campus_tab, text="Campus")
        self.notebook.add(self.building_tab, text="Building")
        self.notebook.add(self.room_tab, text="Room")

        # Initialize tabs
        self.init_faculty_tab()
        self.init_department_tab()
        self.init_campus_tab()
        self.init_building_tab()
        self.init_room_tab()

        self.notebook.pack(expand=1, fill="both")

    def init_faculty_tab(self):
        # Add widgets for Faculty tab
        faculty_frame = ttk.LabelFrame(self.faculty_tab, text="Faculty Information")
        faculty_frame.grid(row=0, column=0, padx=10, pady=10)

        # faculty id
        faculty_id_label = ttk.Label(faculty_frame, text="Faculty ID:")
        faculty_id_label.grid(row=0, column=0, sticky=tk.W)
        faculty_id_entry = ttk.Entry(faculty_frame)
        faculty_id_entry.grid(row=0, column=1, pady=5)

        # faculty Name
        faculty_name_label = ttk.Label(faculty_frame, text="Faculty Name:")
        faculty_name_label.grid(row=1, column=0, sticky=tk.W)
        faculty_name_entry = ttk.Entry(faculty_frame)
        faculty_name_entry.grid(row=1, column=1, pady=5)
        
        # faculty Contact Info
        faculty_label = ttk.Label(faculty_frame, text="Faculty Contact info:" )
        faculty_label.grid(row=2, column=0, pady=10 )
            
            # faculty Telephone no
        telephoneNum_label = ttk.Label(faculty_frame, text="Telephone No:")
        telephoneNum_label.grid(row=3, column=0, padx= 10 , sticky=tk.W)
        telephoneNum_entry = ttk.Entry(faculty_frame)
        telephoneNum_entry.grid(row=3, column=1, padx= 10 , pady=5)

            # faculty Email
        email_label = ttk.Label(faculty_frame, text="Email :")
        email_label.grid(row=4, column=0, padx= 10, sticky=tk.W)
        email_entry = ttk.Entry(faculty_frame)
        email_entry.grid(row=4, column=1, padx= 10, pady=5)

        # Department affiliation
        




        # Add more fields as needed...

        # add_button = ttk.Button(faculty_frame, text="Add Faculty", command=lambda: self.add_faculty(
        #     faculty_id_entry.get(), full_name_entry.get()))
        # add_button.grid(row=2, column=0, columnspan=2, pady=10)

        # display_button = ttk.Button(faculty_frame, text="Display Faculty", command=self.display_faculty)
        # display_button.grid(row=3, column=0, columnspan=2, pady=5)

        # clear_button = ttk.Button(faculty_frame, text="Clear Entries", command=lambda: self.clear_entries(
        #     faculty_id_entry, full_name_entry))
        # clear_button.grid(row=4, column=0, columnspan=2, pady=5)

    def init_department_tab(self):
        # Add widgets for Faculty tab
        department_frame = ttk.LabelFrame(self.department_tab, text="Department Information")
        department_frame.grid(row=0, column=0, padx=10, pady=10)

        # department id
        department_id_label = ttk.Label(department_frame, text="Department ID:")
        department_id_label.grid(row=0, column=0, sticky=tk.W)
        department_id_entry = ttk.Entry(department_frame)
        department_id_entry.grid(row=0, column=1, pady=5)

        # department Name
        department_name_label = ttk.Label(department_frame, text="Department Name:")
        department_name_label.grid(row=1, column=0, sticky=tk.W)
        department_name_entry = ttk.Entry(department_frame)
        department_name_entry.grid(row=1, column=1, pady=5)
        
        # department Contact Info
        department_contact_label = ttk.Label(department_frame, text="Department Contact info:" )
        department_contact_label.grid(row=2, column=0, pady=10 )
            
            # department Telephone no
        telephoneNum_label = ttk.Label(department_frame, text="Telephone No:")
        telephoneNum_label.grid(row=3, column=0, padx= 10 , sticky=tk.W)
        telephoneNum_entry = ttk.Entry(department_frame)
        telephoneNum_entry.grid(row=3, column=1, padx= 10 , pady=5)

            # department Email
        email_label = ttk.Label(department_frame, text="Email :")
        email_label.grid(row=4, column=0, padx= 10, sticky=tk.W)
        email_entry = ttk.Entry(department_frame)
        email_entry.grid(row=4, column=1, padx= 10, pady=5)

        # Head of department (faculty member)
        





    def init_campus_tab(self):
        # Add widgets for Campus tab
        # Similar to the faculty tab, add entry fields and buttons for campus information
        # ...
        pass

    def init_building_tab(self):
        # Add widgets for Building tab
        # Similar to the faculty tab, add entry fields and buttons for building information
        # ...
        pass

    def init_room_tab(self):
        # Add widgets for Room tab
        # Similar to the faculty tab, add entry fields and buttons for room information
        # ...
        pass

    def add_faculty(self, faculty_id, full_name):
        # Add faculty information to the data list
        self.faculty_data.append({
            "Faculty ID": faculty_id,
            "Full Name": full_name,
            # Add more fields as needed...
        })
        print("Faculty added successfully!")

    def display_faculty(self):
        # Display faculty information in the console
        print("\nFaculty Information:")
        for faculty in self.faculty_data:
            print(faculty)
        print("\n")

    def clear_entries(self, *entries):
        # Clear the content of the specified entry widgets
        for entry in entries:
            entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = InstituteConfigurationApp(root)
    root.mainloop()
