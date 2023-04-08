from flask import Flask, render_template, request

from database import load_tenquestions_from_db, add_application_to_db, load_genders_from_db, load_typesofstudies_from_db, load_yearofstudy_from_db, load_ourquestions_from_db

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/poll")
def poll_page():
    firsquestion = load_tenquestions_from_db()
    genders = load_genders_from_db()
    typesofstudies = load_typesofstudies_from_db()
    yearofstudy = load_yearofstudy_from_db() 
    ourquestions = load_ourquestions_from_db()
    return render_template('poll.html', firsquestion=firsquestion, genders = genders, typesofstudies=typesofstudies, yearofstudy=yearofstudy, ourquestions=ourquestions)  

@app.route("/final")
def final_page():   
    return render_template('final.html')

@app.route("/poll/final", methods=['post'])
def submit_page():   
  data = request.form 
  add_application_to_db(data)
  return render_template('final.html', data=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

