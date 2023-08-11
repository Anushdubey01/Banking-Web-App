def calculate_new_cgpa(current_cgpa, total_credits, improved_grade, course_credits):
    # Mapping of grades to grade points
    grade_points = {'S': 10, 'A': 9, 'B': 8, 'C': 7, 'D': 6, 'E': 5}
    
    # Calculate total credit points before improvement
    total_credit_points_before = current_cgpa * total_credits
    
    # Calculate total credit points after improvement
    total_credit_points_after = total_credit_points_before - (grade_points['E'] * course_credits) + (grade_points[improved_grade] * course_credits)
    
    # Calculate new CGPA
    new_cgpa = total_credit_points_after / total_credits
    
    return new_cgpa

# Take user input
current_cgpa = float(input("Enter your current CGPA: "))
total_credits = int(input("Enter your total credits: "))
improved_grade = input("Enter the improved grade (S, A, B, C, D, E): ")
course_credits = int(input("Enter the credits of the course: "))

# Calculate new CGPA
new_cgpa = calculate_new_cgpa(current_cgpa, total_credits, improved_grade, course_credits)

print(f"Your new CGPA after improving the grade to {improved_grade} will be approximately: {new_cgpa:.2f}")
