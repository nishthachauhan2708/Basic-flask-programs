from flask import Flask
app = Flask(__name__)
@app.route('/user/<username>')
def show_user_profile(username):
    return f"Hello, {username}! Welcome to your profile."
@app.route('/square/<int:number>')
def square_number(number):
    return f"The square of {number} is {number**2}"
if __name__ == '__main__':
    app.run(debug=True)