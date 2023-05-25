import tkinter as tk
import calculator

n = 0
all_entries = []

FIELDS = 3
FONT_SIZE = 14
FONT = "David"

def create_labels(course_frame, names):
    for i in range(len(names)):
        label = tk.Label(course_frame, text=names[i], font=(FONT, FONT_SIZE))
        label.grid(row=n, column=i)  # Place label in the second column
    
def update_add_button(add_course_button):
    if add_course_button:
        add_course_button.grid(row=n, column=0)

def update_calculate_button(calculate_button):
    if calculate_button:
        calculate_button.grid(row=n, column=2)

def update_gpa(gpa_label, check_gpa=False):
    if gpa_label:
        gpa_label.grid(row=n, column=1)
        if check_gpa:
            gpa_label.config(text = "GPA: " + str(calculator.calculate_gpa(all_entries)))

def create_course_entry(course_frame, num, add_course_button, calculate_button, gpa_label): 
    global n
    global all_entries
    for i in range(num):
        entry = tk.Entry(course_frame)
        entry.grid(row=n, column=i, padx=(10, 10), pady=(10,10))  # Place entry field below the label
        if i == 0:
            grade_label = entry
        if i == 1:
            weight_label = entry
    
    all_entries.append((grade_label, weight_label))
        
    n += 1
    update_add_button(add_course_button)
    update_calculate_button(calculate_button)
    update_gpa(gpa_label)
        
def main():    
    global n
    # Create the main application window
    window = tk.Tk()
    window.geometry("500x300")
    window.title("GPA Calculator")
    course_frame = tk.Frame(window)
    course_frame.pack()
    
    create_labels(course_frame, ["Grade", "Weight", "Name"])
    n += 1
    
    create_course_entry(course_frame, FIELDS, None, None, None) 
    n += 1
    
    # Button to add a new course entry
    add_course_button = tk.Button(course_frame, text="Add Course", 
                        command=lambda: create_course_entry(course_frame, FIELDS, add_course_button, calculate_button, gpa_label))
    add_course_button.grid(row=n, column=0)

    # Button to calculate the GPA
    calculate_button = tk.Button(course_frame, text="Calculate GPA", 
                       command=lambda: update_gpa(gpa_label, True))
    calculate_button.grid(row=n, column=2)

    gpa_label = tk.Label(course_frame, text="GPA: ", font=(FONT, FONT_SIZE))
    gpa_label.grid(row=n, column=1)  # Place label in the second column
    
    # Start the application
    window.mainloop()

if __name__ == "__main__":
    main()
