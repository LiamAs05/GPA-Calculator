def calculate_gpa(course_entries):
    total_points = 0
    total_weight = 0
    
    for entry in course_entries:
        if not entry[0] or not entry[1]:
            continue
        try:
            grade = int(entry[0].get())
            weight = int(entry[1].get())
        except:
            continue
        total_points += grade * weight
        total_weight += weight

    if total_weight == 0:
        return 0

    gpa = total_points / total_weight
    return gpa