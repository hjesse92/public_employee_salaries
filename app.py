
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
   index_file="index.html"
   return render_template(index_file)

@app.route("/department-job")
def department_job():
    department_job_file="department-job.html"
    return render_template(department_job_file)

@app.route("/overtime-pay")
def overtime_pay():
    overtime_pay_file="overtime-pay.html"
    return render_template(overtime_pay_file)

@app.route("/city-comparison-dashboard")
def city_comparison_dashboard():
    city_comparison_dashboard_file="city-comparison-dashboard.html"
    return render_template(city_comparison_dashboard_file)

if __name__ == "__main__":
   app.run(debug=True)
