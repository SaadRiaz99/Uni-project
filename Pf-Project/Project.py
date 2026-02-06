import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
from PIL import Image, ImageTk


def save_data():
    data = {"Patients": patients, "Appointments": appointments}
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)


def load_data():
    global patients, appointments
    if os.path.exists("data.json"):
        with open("data.json", "r") as file:
            data = json.load(file)
            patients = data.get("Patients", [])
            appointments = data.get("Appointments", [])
    else:
        patients, appointments = [], []


def clear_window():
    for widget in main_container.winfo_children():
        widget.destroy()


def show_main_menu():
    clear_window()

    tk.Label(main_container, text="Main Menu", font=("georgia", 20,), bg="white").pack(pady=20)

    buttons = [
        ("Register Patient", register_patient_screen),
        ("Show Doctors", show_doctors_screen),
        ("Book Appointment", book_appointment_screen),
        ("View Appointments", view_appointments_screen),
        ("Exit", root.quit)
    ]

    for text, command in buttons:
        tk.Button(main_container, text=text, width=40, height=2, command=command,
                  bg="gray", fg="white", font="georgia,20,bold").pack(pady=5)



def register_patient_screen():
    clear_window()
    tk.Label(main_container, text="Register Patient", font=("georgia", 16), bg="white").pack(pady=10)

    tk.Label(main_container, text="Patient Name:", bg="white").pack()
    entry_name = tk.Entry(main_container)
    entry_name.pack()

    tk.Label(main_container, text="Age:", bg="white").pack()
    entry_age = tk.Entry(main_container)
    entry_age.pack()

    tk.Label(main_container, text="Disease:", bg="white").pack()
    entry_disease = tk.Entry(main_container)
    entry_disease.pack()

    def save_patient():
        name, age, disease = entry_name.get().strip(), entry_age.get().strip(), entry_disease.get().strip()
        if not name or not age or not disease:
            messagebox.showerror("Error", "All fields required")
            return

        patients.append({"name": name, "age": age, "disease": disease})
        save_data()
        messagebox.showinfo("Success", "Patient registered!")
        show_main_menu()

    tk.Button(main_container, text="Save", command=save_patient).pack(pady=10)
    tk.Button(main_container, text="Back", command=show_main_menu).pack()


def show_doctors_screen():
    clear_window()
    tk.Label(main_container, text="Doctors List", font=("georgia", 16), bg="white").pack(pady=10)

    for doc in doctors:
        tk.Label(main_container, text=f"{doc['name']} - {doc['specialization']}", bg="white").pack()

    tk.Button(main_container, text="Back", command=show_main_menu).pack(pady=20)


def book_appointment_screen():
    if not patients:
        messagebox.showerror("Error", "No patients registered!")
        return

    clear_window()
    tk.Label(main_container, text="Book Appointment", font=("georgia", 16), bg="white").pack(pady=10)

    tk.Label(main_container, text="Select Patient:", bg="white").pack()
    patient_cb = ttk.Combobox(main_container, values=[p["name"] for p in patients])
    patient_cb.pack()

    tk.Label(main_container, text="Select Doctor:", bg="white").pack()
    doctor_cb = ttk.Combobox(main_container, values=[f"{d['name']}" for d in doctors])
    doctor_cb.pack()

    tk.Label(main_container, text="Date (DD/MM/YYYY):", bg="white").pack()
    entry_date = tk.Entry(main_container)
    entry_date.pack()

    def confirm():
        appointments.append({"patient": patient_cb.get(), "doctor": doctor_cb.get(), "date": entry_date.get()})
        save_data()
        messagebox.showinfo("Success", "Booked!")
        show_main_menu()

    tk.Button(main_container, text="Confirm", command=confirm).pack(pady=10)
    tk.Button(main_container, text="Back", command=show_main_menu).pack()


def view_appointments_screen():
    clear_window()
    tk.Label(main_container, text="Appointments", font=("georgia", 16), bg="white").pack(pady=10)

    if not appointments:
        tk.Label(main_container, text="No appointments.", bg="white", fg="red").pack()
    else:
        for a in appointments:
            tk.Label(main_container, text=f"{a['patient']} with {a['doctor']} on {a['date']}", bg="white").pack()

    tk.Button(main_container, text="Back", command=show_main_menu).pack(pady=20)


patients = []
doctors = [
    {"id": 1, "name": "Dr. Ahmed", "specialization": "Cardiologist", "shift": "morning"},
    {"id": 2, "name": "Dr. Ali", "specialization": "Dermatologist", "shift": "Evening"},
    {"id": 3, "name": "Dr. Sara", "specialization": "Child Specialist", "shift": "morning"},
    {"id": 4, "name": "Dr. Ayesha", "specialization": "Neurologist", "shift": "Evening"},
    {"id": 5, "name": "Dr. Saif", "specialization": "Oncology", "shift": "morning"},
    {"id": 6, "name": "Dr. Hira", "specialization": "Radiology", "shift": "morning"},
    {"id": 7, "name": "Dr. Syed hussain", "specialization": "Plastic Surgery", "shift": "Evening"},
    {"id": 8, "name": "Dr. Irfan khan", "specialization": "Otolaryngology", "shift": "morning"},
    {"id": 9, "name": "Dr. Huzaifa ", "specialization": "Dentist", "shift": "Evening"},
    {"id": 10, "name": "Dr. Shayan raza", "specialization": "General Surgeon", "shift": "Morning"},
    {"id": 11, "name": "Dr. Sumaiya Saad", "specialization": "General Surgeon", "shift": "Morning"},
    {"id": 12, "name": "Dr. Hafsa", "specialization": "Cardiologist", "shift": "morning"}

]
appointments = []

load_data()

root = tk.Tk()
root.title("Hospital Management System")
root.geometry("800x550")

try:
    bg_image = Image.open("1693332004535.jpeg").resize((800, 550))
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except:
    root.configure(bg="gray")

main_container = tk.Frame(root, bg="white", bd=5)
main_container.place(relx=0.5, rely=0.5, anchor="center", width=500, height=440)

show_main_menu()

root.mainloop()