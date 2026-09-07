from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "qiskit_fall_fest_2026_secret_key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    email = request.form.get('email')
    college = request.form.get('college')
    
    # Here you can handle storing registration data (e.g., SQLite database)
    flash(f"Thank you {name}, your registration for Qiskit Fall Fest 2026 was successful!", "success")
    return redirect(url_for('index', _anchor='register'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)