from flask import Flask, render_template, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/counter')
def counter():
    if 'count' not in  session:
        session['count'] = 0
    else: 
        session['count'] += 1
    return render_template('counter.html')


if __name__ == "__main__":
    app.run(debug=True)
