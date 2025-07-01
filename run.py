from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/save_data', methods=['GET', 'POST'])
def save_data():
    if request.method == 'POST':
        regno = request.form.get('regno', '')
        name = request.form.get('name', '')
        standard = request.form.get('class', '')
        math = request.form.get('math', '')
        science = request.form.get('science', '')
        computer = request.form.get('computer', '')
    else:
        regno = request.args.get('regno', '')
        name = request.args.get('name', '')
        standard = request.args.get('class', '')
        math = request.args.get('math', '')
        science = request.args.get('science', '')
        computer = request.args.get('computer', '')
    
    print(f"Data received: {regno}, {name}, {standard}, {math}, {science}, {computer}")
    return redirect(url_for('home'))

