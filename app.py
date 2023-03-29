from flask import Flask, render_template, jsonify

from database import load_jobs_from_db

app = Flask(__name__)




@app.route("/")
def home():
    return render_template('home.html')

@app.route("/poll")
def poll_page():
    firsquestion = load_jobs_from_db()
    return render_template('poll.html', firsquestion=firsquestion)

# @app.route("/api/poll")
# def list_page():
#     firsquestion = load_jobs_from_db()
#     return jsonify(firsquestion) 

@app.route("/final")
def final_page():   
    return render_template('final.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

