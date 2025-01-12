from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chapter1', methods=['GET', 'POST'])
def chapter1():
    if request.method == 'POST':
        answers = request.form
        score = 0
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
