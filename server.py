from flask import Flask, redirect, render_template, request
import csv

app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def my_pages(page_name):
    return render_template(page_name)

@app.route('/contact_form', methods=['POST', 'GET'])
def contact_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "Contact form submission failed"
    else:
        return "Something went wrong, please try again"
    

def write_to_csv(data):
    with open('database.csv', 'a', newline='') as csvfile:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([email, subject, message])
