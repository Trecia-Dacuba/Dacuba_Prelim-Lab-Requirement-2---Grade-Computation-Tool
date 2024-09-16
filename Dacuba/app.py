from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_required_grades(prelim_grade):
    passing_grade = 75
    prelim_weight = 0.20
    midterm_weight = 0.30
    final_weight = 0.50
    grade_range = (0, 100)

    if not (grade_range[0] <= prelim_grade <= grade_range[1]):
        return "Error: Preliminary grade must be between 0 and 100."
    
    current_total = prelim_grade * prelim_weight
    midterm_final_weight = midterm_weight + final_weight
    required_total = passing_grade - current_total
    min_required_average = required_total / midterm_final_weight

    if min_required_average > 100:
        return "Error: It is not possible to achieve the passing grade with this preliminary score."
    
    if min_required_average < grade_range[0]:
        min_required_average = grade_range[0]
    
    return round(min_required_average, 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    required_grade = None
    error = None
    
    if request.method == 'POST':
        try:
            prelim_grade = float(request.form['prelim_grade'])
            required_grade = calculate_required_grades(prelim_grade)
        except ValueError:
            error = "Error: Please enter a valid number."

    return render_template('index.html', required_grade=required_grade, error=error)

if __name__ == '__main__':
    app.run(debug=True)