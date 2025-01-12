from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for Chapter 1
@app.route('/chapter1', methods=['GET', 'POST'])
def chapter1():
    if request.method == 'POST':
        # Process form data
        answers = request.form
        score = 0
        # Logic to evaluate answers
        if answers.get('question1') == 'D':
            score += 1
        if answers.get('question2') == 'A':
            score += 1
        if answers.get('question3') == 'A':
            score += 1
        if answers.get('question4') == 'D':
            score += 1
        if answers.get('question5') == 'B':
            score += 1
        if answers.get('question6') == 'B':
            score += 1
        if answers.get('question7') == 'A':
            score += 1
        if answers.get('question8') == 'A':
            score += 1
        return render_template('chapter1.html', score=score)
    return render_template('chapter1.html', score=None)

if __name__ == '__main__':
    app.run(debug=True)
