# Sumbitted by  : Syed Muhammad Mudasir
# Rollno        : F21BSEEN1E02007
# Semester      : 5th
# Section       : E1
# Project       : Institute Configuration In Tkinter
# Sumbitted To  : Sir Nauman

# To install All The packages just type 

# "pip install -r requirements.txt" 

# in the terminal of vscode or whichever IDE you are Using




import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class InstituteConfigurationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Institute Configuration App")

        # Data storage
        self.faculty_data = []
        self.department_data = []
        self.campus_data = []

        # Create tabs
        self.notebook = ttk.Notebook(root)
        self.campus_tab = ttk.Frame(self.notebook)
        self.faculty_tab = ttk.Frame(self.notebook)
        self.department_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.campus_tab, text="Campus")
        self.notebook.add(self.faculty_tab, text="Faculty")
        self.notebook.add(self.department_tab, text="Department")

        # Initializing tabs
        self.init_campus_tab()
        self.init_faculty_tab()
        self.init_department_tab()

        self.notebook.pack(expand=1, fill="both")

        # Center the window on the screen
        self.center_window()

    # Function For Centering out the window
    def center_window(self):  
        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the position of the window
        x_position = (screen_width - self.root.winfo_reqwidth()) / 2
        y_position = (screen_height - self.root.winfo_reqheight()) / 2

        # Set the window position
        self.root.geometry(f"+{int(x_position)}+{int(y_position)}")


# Campus Area Start

    def init_campus_tab(self):
        # Widgets for Campus tab
        campus_frame = ttk.LabelFrame(self.campus_tab, text="Campus Information")
        campus_frame.grid(row=0, column=0, padx=10, pady=10)

        campus_id_label = ttk.Label(campus_frame, text="Campus ID:")
        campus_id_label.grid(row=0, column=0, sticky=tk.W)
        campus_id_entry = ttk.Entry(campus_frame)
        campus_id_entry.grid(row=0, column=1, pady=5)

        campus_name_label = ttk.Label(campus_frame, text="Campus Name:")
        campus_name_label.grid(row=1, column=0, sticky=tk.W)
        campus_name_entry = ttk.Entry(campus_frame)
        campus_name_entry.grid(row=1, column=1, pady=5)


        contact_info_label = ttk.Label(campus_frame, text="Contact Information:")
        contact_info_label.grid(row=3, column=0, padx=6, sticky=tk.W)

        telephone_label = ttk.Label(campus_frame, text="Telephone Number:")
        telephone_label.grid(row=4, column=0, sticky=tk.W)
        telephone_entry = ttk.Entry(campus_frame)
        telephone_entry.grid(row=4, column=1, pady=5)

        email_label = ttk.Label(campus_frame, text="Email:")
        email_label.grid(row=5, column=0, sticky=tk.W)
        email_entry = ttk.Entry(campus_frame)
        email_entry.grid(row=5, column=1, pady=5)

        address_label = ttk.Label(campus_frame, text="Address:")
        address_label.grid(row=2, column=0, sticky=tk.W)
        address_entry = ttk.Entry(campus_frame)
        address_entry.grid(row=2, column=1, pady=5)

        departments_label = ttk.Label(campus_frame, text="List of Departments:")
        departments_label.grid(row=6, column=0, sticky=tk.W)
        departments_text = tk.Text(campus_frame, height=4, width=30)
        departments_text.grid(row=6, column=1, pady=5)

        add_button = ttk.Button(campus_frame, text="Add Campus", command=lambda: self.add_campus(
            campus_id_entry.get(), campus_name_entry.get(), address_entry.get(),
            telephone_entry.get(), email_entry.get(), departments_text.get("1.0", tk.END).strip().split('\n')))
        add_button.grid(row=7, column=0, columnspan=2, pady=10)

        # "Display Campus" button
        display_button = ttk.Button(campus_frame, text="Display Campus", command=self.display_campus)
        display_button.grid(row=8, column=0, columnspan=2, pady=5)

        # "Clear Entries" button
        clear_button = ttk.Button(campus_frame, text="Clear Entries", command=lambda: self.clear_entries(
            campus_id_entry, campus_name_entry, address_entry,
            telephone_entry, email_entry, departments_text))
        clear_button.grid(row=9, column=0, columnspan=2, pady=5)

    def add_campus(self, campus_id, campus_name, address, telephone, email, departments):
        # Validation check for required fields
        if not all([campus_id, campus_name, address, telephone, email, departments]):
            messagebox.showerror("Error", "Please fill all the required fields.")
            return

        # Access the departments data
        print("Departments:", departments)

        # Store campus information in the data list
        self.campus_data.append({
            "Campus ID": campus_id,
            "Campus Name": campus_name,
            "Address": address,
            "Telephone Number": telephone,
            "Email": email,
            "Departments": departments
        })

        # Save campus data to a text file
        self.save_campus_data_to_file()

        # Display success message
        messagebox.showinfo("Success", "Campus added successfully!")

    def display_campus(self):
        # Create a new window to display campus information
        display_window = tk.Toplevel(self.root)
        display_window.title("Campus Information")

        # Create a Text widget with a vertical scrollbar
        campus_info_text = tk.Text(display_window, height=20, width=50)
        campus_info_text.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # Create a scrollbar and link it to the Text widget
        scrollbar = tk.Scrollbar(display_window, command=campus_info_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        campus_info_text.config(yscrollcommand=scrollbar.set)

        for campus in self.campus_data:
            campus_info_text.insert(tk.END, "\n".join([f"{key}: {value}" for key, value in campus.items()]))
            campus_info_text.insert(tk.END, "\n\n")

        # Add "Close" button
        close_button = ttk.Button(display_window, text="Close", command=display_window.destroy)
        close_button.pack(padx=10, pady=10)

        # Add "Delete" button
        delete_button = ttk.Button(display_window, text="Delete", command=lambda: self.confirm_delete_campus(display_window, campus_info_text))
        delete_button.pack(padx=10, pady=5)

    def confirm_delete_campus(self, window, text_widget):
        # Check if there is more than one selection
        if len(text_widget.tag_ranges(tk.SEL)) > 2:
            messagebox.showwarning("Warning", "Please select only one campus entry to delete.")
            return

        # Check if any text is selected in the Text widget
        if not text_widget.tag_ranges(tk.SEL):
            messagebox.showwarning("Warning", "Please select at least one campus entry to delete.")
            return

        # Get the selected text in the Text widget
        selected_text = text_widget.get(tk.SEL_FIRST, tk.SEL_LAST).strip()

        # Display confirmation message
        confirm_delete = messagebox.askyesno("Confirmation", "Are you sure you want to delete this campus entry?")

        if confirm_delete:
            # Delete campus if confirmed
            self.delete_campus(window, text_widget, selected_text)

    def delete_campus(self, window, text_widget, selected_text):
        # Find the campus entry with the selected information
        for campus in self.campus_data:
            campus_info = "\n".join([f"{key}: {value}" for key, value in campus.items()])
            if campus_info.strip() == selected_text:
                # Remove the selected campus from the data
                self.campus_data.remove(campus)
                break

        # Save the updated campus data to a text file
        self.save_campus_data_to_file()

        # Update the displayed campus information
        text_widget.delete(1.0, tk.END)
        for campus in self.campus_data:
            text_widget.insert(tk.END, "\n".join([f"{key}: {value}" for key, value in campus.items()]))
            text_widget.insert(tk.END, "\n\n")

    def save_campus_data_to_file(self):
        # Save campus data to a text file
        with open("campus_data.txt", "w") as file:
            for campus in self.campus_data:
                file.write("\n".join([f"{key}: {value}" for key, value in campus.items()]))
                file.write("\n\n")

# Campus end


# Faculty Area Start

    def init_faculty_tab(self):
        # Widgets for Faculty tab
        faculty_frame = ttk.LabelFrame(self.faculty_tab, text="Faculty Information")
        faculty_frame.grid(row=0, column=0, padx=10, pady=10)

        faculty_id_label = ttk.Label(faculty_frame, text="Faculty ID:")
        faculty_id_label.grid(row=0, column=0, sticky=tk.W)
        faculty_id_entry = ttk.Entry(faculty_frame)
        faculty_id_entry.grid(row=0, column=1, pady=5)

        full_name_label = ttk.Label(faculty_frame, text="Full Name:")
        full_name_label.grid(row=1, column=0, sticky=tk.W)
        full_name_entry = ttk.Entry(faculty_frame)
        full_name_entry.grid(row=1, column=1, pady=5)

        contact_info_label = ttk.Label(faculty_frame, text="Contact Information:")
        contact_info_label.grid(row=2, column=0, padx=6 , sticky=tk.W)

        phone_label = ttk.Label(faculty_frame, text="Telephone Number:")
        phone_label.grid(row=3, column=0, sticky=tk.W)
        phone_entry = ttk.Entry(faculty_frame)
        phone_entry.grid(row=3, column=1, pady=5)

        email_label = ttk.Label(faculty_frame, text="Email:")
        email_label.grid(row=4, column=0, sticky=tk.W)
        email_entry = ttk.Entry(faculty_frame)
        email_entry.grid(row=4, column=1, pady=5)

        address_label = ttk.Label(faculty_frame, text="Address:")
        address_label.grid(row=5, column=0, sticky=tk.W)
        address_entry = ttk.Entry(faculty_frame)
        address_entry.grid(row=5, column=1, pady=5)

        department_label = ttk.Label(faculty_frame, text="Department Affiliation:")
        department_label.grid(row=6, column=0, sticky=tk.W)
        department_entry = ttk.Entry(faculty_frame)
        department_entry.grid(row=6, column=1, pady=5)

        qualifications_label = ttk.Label(faculty_frame, text="Qualifications:")
        qualifications_label.grid(row=7, column=0, sticky=tk.W)
        qualifications_entry = ttk.Entry(faculty_frame)
        qualifications_entry.grid(row=7, column=1, pady=5)

        teaching_subjects_label = ttk.Label(faculty_frame, text="Teaching Subjects:")
        teaching_subjects_label.grid(row=8, column=0, sticky=tk.W)
        teaching_subjects_text = tk.Text(faculty_frame, height=4, width=30)
        teaching_subjects_text.grid(row=8, column=1, pady=5)

        add_button = ttk.Button(faculty_frame, text="Add Faculty", command=lambda: self.add_faculty(
            faculty_id_entry.get(), full_name_entry.get(), phone_entry.get(), email_entry.get(),
            address_entry.get(), department_entry.get(), qualifications_entry.get(),
            teaching_subjects_text.get("1.0", tk.END).strip().split('\n')))
        add_button.grid(row=9, column=0, columnspan=2, pady=10)

        # "Display Faculty" button
        display_button = ttk.Button(faculty_frame, text="Display Faculty", command=self.display_faculty)
        display_button.grid(row=10, column=0, columnspan=2, pady=5)

        # "Clear Entries" button
        clear_button = ttk.Button(faculty_frame, text="Clear Entries", command=lambda: self.clear_entries(
            faculty_id_entry, full_name_entry, phone_entry, email_entry,
            address_entry, department_entry, qualifications_entry,
            teaching_subjects_text))
        clear_button.grid(row=11, column=0, columnspan=2, pady=5)

    def add_faculty(self, faculty_id, full_name, phone, email, address, department, qualifications, teaching_subjects):
        
        # Validation check for required fields
        if not all([faculty_id, full_name, phone, email, address, department, qualifications, teaching_subjects]):
            messagebox.showerror("Error", "Please fill all the required fields.")
            return
        
        # Access the qualifications data
        print("Qualifications:", qualifications)

        # Store faculty information in the data list
        self.faculty_data.append({
            "Faculty ID": faculty_id,
            "Full Name": full_name,
            "Phone Number": phone,
            "Email": email,
            "Address": address,
            "Department Affiliation": department,
            "Qualifications": qualifications,
            "Teaching Subjects": teaching_subjects
        })

        # Save faculty data to a text file
        self.save_data_to_file()

        # Display success message
        messagebox.showinfo("Success", "Faculty added successfully!")

    def display_faculty(self):
        # A new window to display faculty information
        display_window = tk.Toplevel(self.root)
        display_window.title("Faculty Information")

        # A Text widget with a vertical scrollbar
        faculty_info_text = tk.Text(display_window, height=20, width=50)
        faculty_info_text.pack(side=tk.LEFT, fill=tk.Y , padx=10 ,pady=10)

        # A scrollbar and link it to the Text widget
        scrollbar = tk.Scrollbar(display_window, command=faculty_info_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        faculty_info_text.config(yscrollcommand=scrollbar.set)

        for faculty in self.faculty_data:
            faculty_info_text.insert(tk.END, "\n".join([f"{key}: {value}" for key, value in faculty.items()]))
            faculty_info_text.insert(tk.END, "\n\n")

        # "Close" button
        close_button = ttk.Button(display_window, text="Close", command=display_window.destroy)
        close_button.pack(padx=10 ,pady=10)

        # "Delete" button
        delete_button = ttk.Button(display_window, text="Delete", command=lambda: self.confirm_delete_faculty(display_window, faculty_info_text))
        delete_button.pack(padx=10 , pady=5)

    def confirm_delete_faculty(self, window, text_widget):
        # Check if there is more than one selection
        if len(text_widget.tag_ranges(tk.SEL)) > 2:
            messagebox.showwarning("Warning", "Please select only one faculty entry to delete.")
            return

        # Check if any text is selected in the Text widget
        if not text_widget.tag_ranges(tk.SEL):
            messagebox.showwarning("Warning", "Please select at least one faculty entry to delete.")
            return

        # Get the selected text in the Text widget
        selected_text = text_widget.get(tk.SEL_FIRST, tk.SEL_LAST).strip()

        # Display confirmation message
        confirm_delete = messagebox.askyesno("Confirmation", "Are you sure you want to delete this faculty entry?")

        if confirm_delete:
            # Delete faculty if confirmed
            self.delete_faculty(window, text_widget, selected_text)

    def delete_faculty(self, window, text_widget, selected_text):
        # Find the faculty entry with the selected information
        for faculty in self.faculty_data:
            faculty_info = "\n".join([f"{key}: {value}" for key, value in faculty.items()])
            if faculty_info.strip() == selected_text:
                # Remove the selected faculty from the data
                self.faculty_data.remove(faculty)
                break

        # Save the updated faculty data to a text file
        self.save_data_to_file()

        # Update the displayed faculty information
        text_widget.delete(1.0, tk.END)
        for faculty in self.faculty_data:
            text_widget.insert(tk.END, "\n".join([f"{key}: {value}" for key, value in faculty.items()]))
            text_widget.insert(tk.END, "\n\n")

    def save_data_to_file(self):
        # Save faculty data to a text file
        with open("faculty_data.txt", "w") as file:
            for faculty in self.faculty_data:
                file.write("\n".join([f"{key}: {value}" for key, value in faculty.items()]))
                file.write("\n\n")

# Faculty end


# Department Area Start

    def init_department_tab(self):
        # Widgets for Department tab
        department_frame = ttk.LabelFrame(self.department_tab, text="Department Information")
        department_frame.grid(row=0, column=0, padx=10, pady=10)

        department_id_label = ttk.Label(department_frame, text="Department ID:")
        department_id_label.grid(row=0, column=0, sticky=tk.W)
        department_id_entry = ttk.Entry(department_frame)
        department_id_entry.grid(row=0, column=1, pady=5)

        department_name_label = ttk.Label(department_frame, text="Department Name:")
        department_name_label.grid(row=1, column=0, sticky=tk.W)
        department_name_entry = ttk.Entry(department_frame)
        department_name_entry.grid(row=1, column=1, pady=5)

        head_of_department_label = ttk.Label(department_frame, text="Head of Department:")
        head_of_department_label.grid(row=2, column=0, sticky=tk.W)
        head_of_department_entry = ttk.Entry(department_frame)
        head_of_department_entry.grid(row=2, column=1, pady=5)

        contact_info_label = ttk.Label(department_frame, text="Contact Information:")
        contact_info_label.grid(row=3, column=0, padx=6 , sticky=tk.W)

        telephone_label = ttk.Label(department_frame, text="Telephone Number:")
        telephone_label.grid(row=4, column=0, sticky=tk.W)
        telephone_entry = ttk.Entry(department_frame)
        telephone_entry.grid(row=4, column=1, pady=5)

        email_label = ttk.Label(department_frame, text="Email:")
        email_label.grid(row=5, column=0, sticky=tk.W)
        email_entry = ttk.Entry(department_frame)
        email_entry.grid(row=5, column=1, pady=5)

        office_location_label = ttk.Label(department_frame, text="Office Location:")
        office_location_label.grid(row=6, column=0, sticky=tk.W)
        office_location_entry = ttk.Entry(department_frame)
        office_location_entry.grid(row=6, column=1, pady=5)

        description_label = ttk.Label(department_frame, text="Description:")
        description_label.grid(row=7, column=0, sticky=tk.W)
        description_text = tk.Text(department_frame, height=4, width=30)
        description_text.grid(row=7, column=1, pady=5)

        add_button = ttk.Button(department_frame, text="Add Department", command=lambda: self.add_department(
            department_id_entry.get(), department_name_entry.get(), head_of_department_entry.get(),
            telephone_entry.get(), email_entry.get(), office_location_entry.get(),
            description_text.get("1.0", tk.END).strip().split('\n')))
        add_button.grid(row=8, column=0, columnspan=2, pady=10)

        # "Display Department" button
        display_button = ttk.Button(department_frame, text="Display Department", command=self.display_department)
        display_button.grid(row=9, column=0, columnspan=2, pady=5)

        # "Clear Entries" button
        clear_button = ttk.Button(department_frame, text="Clear Entries", command=lambda: self.clear_entries(
            department_id_entry, department_name_entry, head_of_department_entry,
            telephone_entry, email_entry, office_location_entry, description_text))
        clear_button.grid(row=10, column=0, columnspan=2, pady=5)

    def add_department(self, department_id, department_name, head_of_department, telephone, email, office_location, description):
        # Validation check for required fields
        if not all([department_id, department_name, head_of_department, telephone, email, office_location, description]):
            messagebox.showerror("Error", "Please fill all the required fields.")
            return

        # Access the description data
        print("Description:", description)

        # Store department information in the data list
        self.department_data.append({
            "Department ID": department_id,
            "Department Name": department_name,
            "Head of Department": head_of_department,
            "Telephone Number": telephone,
            "Email": email,
            "Office Location": office_location,
            "Description": description
        })

        # Save department data to a text file
        self.save_department_data_to_file()

        # Display success message
        messagebox.showinfo("Success", "Department added successfully!")

    def display_department(self):
        # A new window to display department information
        display_window = tk.Toplevel(self.root)
        display_window.title("Department Information")

        # A Text widget with a vertical scrollbar
        department_info_text = tk.Text(display_window, height=20, width=50)
        department_info_text.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # A scrollbar and link it to the Text widget
        scrollbar = tk.Scrollbar(display_window, command=department_info_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        department_info_text.config(yscrollcommand=scrollbar.set)

        for department in self.department_data:
            department_info_text.insert(tk.END, "\n".join([f"{key}: {value}" for key, value in department.items()]))
            department_info_text.insert(tk.END, "\n\n")

        # "Close" button
        close_button = ttk.Button(display_window, text="Close", command=display_window.destroy)
        close_button.pack(padx=10, pady=10)

        # "Delete" button
        delete_button = ttk.Button(display_window, text="Delete", command=lambda: self.confirm_delete_department(display_window, department_info_text))
        delete_button.pack(padx=10, pady=5)

    def confirm_delete_department(self, window, text_widget):
        # Check if there is more than one selection
        if len(text_widget.tag_ranges(tk.SEL)) > 2:
            messagebox.showwarning("Warning", "Please select only one department entry to delete.")
            return

        # Check if any text is selected in the Text widget
        if not text_widget.tag_ranges(tk.SEL):
            messagebox.showwarning("Warning", "Please select at least one department entry to delete.")
            return

        # Get the selected text in the Text widget
        selected_text = text_widget.get(tk.SEL_FIRST, tk.SEL_LAST).strip()

        # Display confirmation message
        confirm_delete = messagebox.askyesno("Confirmation", "Are you sure you want to delete this department entry?")

        if confirm_delete:
            # Delete department if confirmed
            self.delete_department(window, text_widget, selected_text)

    def delete_department(self, window, text_widget, selected_text):
        # Find the department entry with the selected information
        for department in self.department_data:
            department_info = "\n".join([f"{key}: {value}" for key, value in department.items()])
            if department_info.strip() == selected_text:
                # Remove the selected department from the data
                self.department_data.remove(department)
                break

        # Save the updated department data to a text file
        self.save_department_data_to_file()

        # Update the displayed department information
        text_widget.delete(1.0, tk.END)
        for department in self.department_data:
            text_widget.insert(tk.END, "\n".join([f"{key}: {value}" for key, value in department.items()]))
            text_widget.insert(tk.END, "\n\n")

    def save_department_data_to_file(self):
        # Save department data to a text file
        with open("department_data.txt", "w") as file:
            for department in self.department_data:
                file.write("\n".join([f"{key}: {value}" for key, value in department.items()]))
                file.write("\n\n")

# Depatment end

    def clear_entries(self, *entries):
        # Clear the content of the specified entry widgets
        for entry in entries:
            if isinstance(entry, tk.Entry):
                entry.delete(0, tk.END)
            elif isinstance(entry, tk.Text):
                entry.delete(1.0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = InstituteConfigurationApp(root)
    root.mainloop()
