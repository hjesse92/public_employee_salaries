
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/welcome")
def index():
   index_file="index.html"
   return render_template(index_file)

@app.route("/visualizations/department-job")
def department_job():
    department_job_file="department-job.html"
    return render_template(department_job_file)

@app.route("/visualizations/state-level-view")
def state_level_view():
    state_level_view_file="state-level-view.html"
    return render_template(state_level_view_file)

@app.route("/visualizations/overtime-pay")
def overtime_pay():
    overtime_pay_file="overtime-pay.html"
    return render_template(overtime_pay_file)

@app.route("/visualizations/city-comparison-dashboard")
def city_comparison_dashboard():
    city_comparison_dashboard_file="city-comparison-dashboard.html"
    return render_template(city_comparison_dashboard_file)

@app.route("/about-us")
def about_us():
    about_us_file="about-us.html"
    return render_template(about_us_file)

@app.route("/references")
def references():
    about_us_file="references.html"
    return render_template(about_us_file)


if __name__ == "__main__":
   app.run(debug=True)
