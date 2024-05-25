from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("Home.html")


@app.route('/adminlogin')
def adminlogin():
    return render_template("adminlogin.html", role='Admin')


@app.route("/Admin")
def admin():
    return render_template("Admin.html")


# JOBS = [{
#     'id': 1,
#     'title': 'Data Analyst',
#     'location': 'Bengaluru, India',
#     'salary': 'Rs. 10,00,000'
# }, {
#     'id': 2,
#     'title': 'Data Scientist',
#     'location': 'Delhi, India',
#     'salary': 'Rs. 15,00,000'
# }, {
#     'id': 3,
#     'title': 'Frontend Developer',
#     'location': 'San Francisco, USA',
#     'salary': '$120,000'
# }]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
