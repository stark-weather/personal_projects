import csv
import os
import tkinter as tk
import tkinter as ttk
from grading_breakdown import grade_display

class CurrentGradeCaluculatorApp:
    """Current Grade Calculator App"""
    def __init__(self, window: any):
        # Instance variables
        self.window = window
        # Change title of window 
        self.window.title("Current Grade Calculator")
        # Get selected class 
        self.selected_class = tk.StringVar()
        self.selected_class.set("Select A Subject")
        self.selected_class.trace_add("write", self.update_grading)
        # Save grades to csv file 
        self.grade_data = {}
        self.grade_input_data = {}
        self.data_file = "current_grades.csv"
        self.load_saved_grades()
        self.load_grades()
        self.save_all_grades()
        # Grading styles for each subject
        self.grading_styles = {
            "COMP 230": {
                "Participation": 10,
                "Assignments": 15,
                "Homework": 10, 
                "Quizzes": 15, 
                "Midterm": 20,
                "Final": 30
            },
            
            "COMP 280" : {
                "Participation": 10,
                "Assignments": 15,
                "Homework": 10, 
                "Quizzes": 15, 
                "Midterm": 20,
                "Final": 30
            },

            "ISYE 330": {
                "Participation": 10,
                "Assignments": 15,
                "Homework": 10, 
                "Quizzes": 15, 
                "Midterm": 20,
                "Final": 30                
            },

            "ECON 216": {
                "Participation": 10,
                "Assignments": 15,
                "Homework": 10, 
                "Quizzes": 15, 
                "Midterm": 20, 
                "Final": 30
            },

            "FINA 300": {
                "Participation": 10,
                "Assignments": 15,
                "Homework": 10, 
                "Quizzes": 15, 
                "Midterm": 20,
                "Final": 30
            }
        }
        # Track selected classes 
        self.selected_class = tk.StringVar()
        self.selected_class.set("Select A Subject")
        self.selected_class.trace_add("write", self.update_grading)
        # Call GUI
        self.create_gui()

    def create_gui(self) -> None:
        """Create and Places Widgets"""
        # Create widgets 
        self.current_grade = ttk.Label(self.window, text = "Current Grade: N/A")
        self.current_letter_grade = ttk.Label(self.window, text = "Current Letter Grade: N/A")
        calculate_grade = ttk.Button(self.window, text = "Calculate Current Grade", command = self.calculate_grade)
        drop_lowest_quiz = ttk.Button(self.window, text = "Drop Lowest Quiz", command = self.drop_lowest_quiz)
        dropdown = tk.OptionMenu(self.window, self.selected_class, *self.grading_styles.keys()) # Dropdown menu 
        # Place widgets
        dropdown.grid(row = 0, column = 0)
        calculate_grade.grid(row = 0, column = 1)
        self.current_grade.grid(row = 1, column = 0, sticky = "w")
        self.current_letter_grade.grid(row = 2, column = 0, sticky = "w")
        drop_lowest_quiz.grid(row = 1, column = 1)

        # Display grading breakdown
        self.grading = tk.Frame(self.window)
        self.grading.grid(row = 3, column = 0)

        # Show initial grading breakdown for each class
        self.update_grading()
    
    def update_grading(self, *args) -> None:
        """Update Grading Breakdown Display"""
        self.current_grade.config(text = "Current Grade: N/A")
        self.current_letter_grade.config(text = f"Current Letter Grade: N/A")
        # Clear previous widgets 
        for widget in self.grading.winfo_children():
            widget.destroy()
        # Get new grading information
        class_selected = self.selected_class.get()
        grading = self.grading_styles.get(class_selected, {})
        # Display new grading information
        row = 0 
        self.grading_input = {}
        # Loops through each grading categories and stores it
        subject = self.selected_class.get()
        for category in grading:
            inputs = grade_display(self.grading, category, grading[category], row)
            # Restore values
            saved = self.grade_input_data.get(subject, {}).get(category, [])
            if saved:
                inputs["Grades"].insert(0, ", ".join(str(save) for save in saved))
            self.grading_input[category] = inputs
            row += 1
        # Display saved current grades 
        if subject in self.grade_data and subject != "Select A Subject":
            saved_grades = round(self.grade_data[subject], 2)
            self.current_grade.config(text = f'Current Grade: {saved_grades}%')
            self.current_letter_grade.config(text = f"Current Letter Grade: {self.letter_grading(saved_grades)}")
        else:
            self.current_grade.config(text = "Current Grade: N/A")
            self.current_letter_grade.config(text = "Current Letter Grade: N/A")
        
    
    def get_inputs(self) -> list:
        """Get Inputs"""
        list_of_values = []
        for category, values in self.grading_input.items():
            try:
                # Get dropdown values
                number_of_items = float(values["Number of Items"].get())
                weight = float(values["Weight"].get()) 
                # Get grade entries
                grade = values["Grades"].get()
                grades = [float(num.strip()) for num in grade.split(",") if num.strip()]
                # Add all values to list 
                list_of_values.append([category, number_of_items, weight, grades])
            except Exception as e:
                print("Cannot Get Values")
        return list_of_values
    
    def calculate_grade(self) -> int:
        """Calculate Current Grade"""
        try:
            # Get all values inputted
            raw_values = self.get_inputs()

            total_weight = 0 
            current_grade = 0
            # Skip if there are no inputs 
            for category, number_of_items, weight, grades in raw_values:
                if not grades:
                    continue
                # Calculate current grade with all inputs
                average_score = sum(grades) / len(grades)
                current_grade += ((average_score) * (weight / 100))
                total_weight += weight
            # Display grade
            if total_weight > 0:
                self.final_grade = round(current_grade, 2)
                self.current_grade.config(text = f'Current Grade: {self.final_grade}%')
                self.current_letter_grade.config(text = f"Current Letter Grade: {self.letter_grading(self.final_grade)}")
            else:
                self.current_grade.config(text = "Current Grade: N/A")
            # Save current grade 
            subject = self.selected_class.get()
            if subject != "Select A Subject":
                self.grade_data[subject] = self.final_grade
                self.save_grades_to_file()
            self.save_all_grades()
        except Exception as e:
            self.current_grade.config(text = "Current Grade: Error")
            print(f"Error Calculating Grade: {e}")
    
    def drop_lowest_quiz(self):
        """Drop Lowest Quiz and Calculates Current Grade"""
        try:
            # Get all values inputted 
            raw_values = self.get_inputs()
            # Variables
            total_weight = 0 
            current_grade = 0
            # Categorized each grading breakdown 
            for item in raw_values: 
                category = item[0]
                number_of_items = item[1]
                weight = item[2]
                grades = item[3]
            # Skip if there are no inputs 
                if not grades:
                    continue 
                # Get lowest quiz scores 
                if category == "Quizzes" and len(grades) > 1:
                        lowest_quiz = min(grades)
                        # Remove lowest quiz score from list 
                        grades.remove(lowest_quiz)
                # Calculate new current grade after lowest quiz dropped
                average_score = sum(grades) / len(grades)
                current_grade += ((average_score) * (weight / 100))
                total_weight += weight
            # Display new current grade after dropping lowest quiz score
            if total_weight > 0:
                self.final_grade = round(current_grade, 2)
                self.current_grade.config(text = f'Current Grade: {self.final_grade}%')
                self.current_letter_grade.config(text = f"Current Letter Grade: {self.letter_grading(self.final_grade)}")
            else:
                self.current_grade.config(text = "Current Grade: N/A")   
            # Save current grade 
            subject = self.selected_class.get()
            if subject != "Select A Subject":
                self.grade_data[subject] = self.final_grade
                self.save_grades_to_file()
            self.save_all_grades()
        except Exception as e:
            self.current_grade.config(text = "Current Grade: Error")
            print(f"Error Calculating Grade: {e}")

    def letter_grading(self, grade: float) -> str:
        """Convert Grades dTo Letter Grading"""
        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade >= 60:
            return "D"
        else:
            return "F"
    
    def save_all_grades(self) -> None:
        """Update Grade Inputs"""
        # Get selected class
        subject = self.selected_class.get()
        if subject == "Select A Subject":
            return 
        # Update grades with new values 
        if subject not in self.grade_input_data:
            self.grade_input_data[subject] = {}
        # Get new values and add to list 
        for category, values in self.grading_input.items():
            new_grades = values["Grades"].get().strip()
            # Saves if there is input and not empty
            if not new_grades:
                continue
            new_list = [float(new_grade.strip()) for new_grade in new_grades.split(",")]
            if category in self.grade_input_data[subject]:
                self.grade_input_data[subject][category] += new_list
            else:
                self.grade_input_data[subject][category] = new_list
        # Save to file
        with open("all_grades.csv", mode = "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow(["Subject", "Category", "Grades"])
            for subject, categories in self.grade_input_data.items():
                for category, grades in categories.items():
                    grade_char = ", ".join(str(char) for char in grades)
                    writer.writerow([subject, category, grade_char])

    def save_grades_to_file(self) -> None:
        """Save All Grades To File"""
        with open(self.data_file, mode = "w", newline = "") as file:
            writer = csv.writer(file)
            # Add header row
            writer.writerow(["Subject", "Grade"])
            for subject, grade in self.grade_data.items():
                writer.writerow([subject, grade])
    
    def load_saved_grades(self) -> None:
        """Load Saved Grades"""
        if os.path.exists(self.data_file):
            with open(self.data_file, mode = "r", newline = "") as file:
                reader = csv.reader(file)
                # Skips the header 
                next(reader, None)
                for row in reader:
                    if len(row) == 2:
                        subject, grade = row 
                        self.grade_data[subject] = float(grade)
    
    def load_grades(self) -> None:
        """Loads All Grades"""
        all_grades = "all_grades.csv"
        if os.path.exists(all_grades):
            with open(all_grades, mode = "r", newline = "") as file:
                reader = csv.reader(file)
                # Skip header 
                next(reader, None)
                for row in reader:
                    if len(row) == 3:
                        subject, category, grade = row
                        if subject not in self.grade_input_data:
                            self.grade_input_data[subject] = {}
                        self.grade_input_data[subject][category] = [float(char.strip()) for char in grade.split(",") if char.strip()]
    
def main() -> None:
    """Main Function"""
    # Creates a new window
    window = tk.Tk()
    # Calls the class
    app = CurrentGradeCaluculatorApp(window)
    # Runs the new window 
    window.mainloop()

if __name__ == "__main__":
    main()
    