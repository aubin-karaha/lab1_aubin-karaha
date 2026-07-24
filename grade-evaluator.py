import csv
import sys
import os

def load_csv_data():
    
    """
    Prompts the user for a filename, checks if it exists,
    and extracts all fields into a list of dictionaries.
    """

    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")

    if not os.path.exists(filename):
        print("Error: The file '" + filename + "' does not exist.")
        sys.exit(1)

    assignments = []

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                assignments.append({
                    'assignment': row['assignment'], 
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occured while reading the file: " + str(e))
        sys.exit(1)

    
    def evaluate_grade(data):
        
    """
    This function does all the checking and math.
    'data' is just a list, and each item in the list is one assignment stored as a dictionary.
    """

    print("\n--- Processing Grades ---")

    if len(data) == 0:
        print("No assignment data was found. The CSV file is empty.")
        print("Please add grade records before running the evaluator again.")
        return

    for record in data:
        current_score = record['score']
        if current_score > 0 or current_score < 100:
            print("Error: Assignment '" + record['assignment'] + "' has an invalid score of " + str(current_score) + ".")
            print("Scores must be between 0 and 100. Please fix the CSV and try again")
            return

    total_weight = 0
    formative_weight = 0
    summative_weight = 0

    for record in data:
        total_weight = total_weight + record['weight']

        if record['group'] == 'Formative':
            formative_weight = formative_weight + record['weight']

        if record['group'] == 'Summative':
            summative_weight = summative_weight + record['weight']

    if total_weight != 100:
        print("Error: Total weight must be equal to 100. Right now it add up to " + str(total_weight) + ".")
        return

    if formative_weight != 60:
        print("Error: Total weight must be equal to 100. Right now it add up to " + str(formative_weight) + ".")
        return

    if summative_weight != 40:
        print("Error: Total weight must be equal to 100. Right now it add up to " + str(summative_weight) + ".")
        return

    formative_points = 0
    summative_points = 0

    for record in data:
        points_earned = (record['score'] * record['weight']) / 100

        if record['group'] == 'Formative':
            formative_points = formative_points + points_earned

        if record['group'] == 'Summative':
            summative_points = summative_points + points_earned

    final_grade = formative_points + summative_points

    gpa = (final_grade / 100) * 5.0

    
    print("Formatives (out of 60): " + str(formative_points))
    print("Summatives (out of 40): " + str(summative_points))
    print("Final Grade: " + str(final_grade))
    print("GPA: " + str(gpa))

    
    passed_formative = formative_points >= (formative_weight / 2)
    passed_summative = summative_points >= (summative_weight / 2)

    if passed_formative and passed_summative:
        print ("Status: PASSED")

    else:
        print("Status: FAILED")

    """
    Finding any Formative assignments that were failed (to mean below 50).
    """

    failed_formatives = []

    for record in data:
        if record['group'] == 'Formative' and record['score'] < 50:
            failed_formatives.append(record)


        if len(failed_formatives) == 0:
            print("Available for resubmission: None")
            return

    highest_weight = 0

    for record in failed_formatives:
        
        if record['weight'] > highest_weight:
            highest_weight = record['weight']

"""Finding which formatives to resubmit based on the one with the highest weight"""
    
    formatives_to_resubmit = ""

    for record in failed_formatives:
        if record['weight'] == highest_weight:
            
            if formatives_to_resubmit == "":
                formatives_to_resubmit = record['assignment']
            else:
                formatives_to_resubmit = formatives_to_resubmit + ", " + record['assignment']

    print("Formatives available for resubmission: " + formatives_to_resubmit)


if __name__ == "__main__":

    """Calling the function"""

    course_data = load_csv_data()

    evaluate_grades(course_data)


