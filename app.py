from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('CV.html')


if __name__ == '__main__':
    app.run(debug=True)



# @app.route('/about')
# def getAboutFunc():
#     return redirect(url_for('about'))
#
# @app.route('/about')
# def about():
#     return redirect('/catalog')
