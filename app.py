from flask import Flask, render_template, request

from database import load_jobs_from_db, add_application_to_db, load_genders_from_db, load_typesofstudies_from_db, load_yearofstudy_from_db

app = Flask(__name__)




@app.route("/")
def home():
    return render_template('home.html')

@app.route("/poll")
def poll_page():
    firsquestion = load_jobs_from_db()
    genders = load_genders_from_db()
    typesofstudies = load_typesofstudies_from_db()
    yearofstudy = load_yearofstudy_from_db()
    return render_template('poll.html', firsquestion=firsquestion, genders = genders, typesofstudies=typesofstudies, yearofstudy=yearofstudy)  


# @app.route("/api/poll")
# def list_page():
#     firsquestion = load_jobs_from_db()
#     return jsonify(firsquestion) 

@app.route("/final")
def final_page():   
    return render_template('final.html')

@app.route("/poll/final", methods=['post'])
def submit_page():   
  data = request.form
  #print(data['first_question'], data['second_question'])
  

  add_application_to_db(data)
  #add_application_to_db(data)
  return render_template('final.html', data=data)

# @app.route("/poll/<id>")
# def show_job(id):
#   job = load_job_from_db(id)
#   return jsonify(job)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

