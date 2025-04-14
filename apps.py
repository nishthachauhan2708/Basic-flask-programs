from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/')
def form():
    return render_template('form.html')
@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return f"Hello, {name}! Welcome to Flask."
if __name__ == '__main__':
    app.run(debug=True)