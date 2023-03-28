from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/poll")
def poll_page():   
    return render_template('poll.html')

@app.route("/final")
def final_page():   
    return render_template('final.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

