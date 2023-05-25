MIN = GRADE_INDEX = 0
MAX = 100
WEIGHT = 1

def calculate_gpa(course_entries):
    """
    This function is the calculator logic.
    @param: course_entries is the user-supplied data
    @return: Grade-Point Average
    @rtype: float
    """
    total_points = 0
    total_weight = 0
    
    for entry in course_entries:
        try:
            grade = int(entry[GRADE_INDEX].get())
            weight = int(entry[WEIGHT].get())
        except:
            continue
        
        if MIN <= grade <= MAX: # checking if grade is valid
            total_points += grade * weight
            total_weight += weight
        else:
            print("Grades are allowed to be between 0 and 100 only.")
        
    if not total_weight:
        return 0

    gpa = total_points / total_weight
    return gpa