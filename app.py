from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('CV.html')

@app.route('/assignment8')
def ass8():
    return render_template('assignment8.html', firstName='Matan', lastName='Spiro',
                           hobbies=('swimming', 'reading', 'soccer'))


if __name__ == '__main__':
    app.run(debug=True)
