import os
from sqlalchemy import create_engine, text 


db_connection_string = os.environ['DB_CONNECTION_STRING']


engine = create_engine(
  db_connection_string, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from firstquestion"))
    firstquestion = []
    for row in result.all():
      firstquestion.append(row)
    return firstquestion

def load_ourquestions_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from ourquestions"))
    ourquestions = []
    for row in result.all():
      ourquestions.append(row)
    return ourquestions
    
def load_genders_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from genders"))
    genders = []
    for row in result.all():
      genders.append(row)
    return genders

def load_typesofstudies_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from typesofstudies"))
    typesofstudies = []
    for row in result.all():
      typesofstudies.append(row)
    return typesofstudies

def load_yearofstudy_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from yearofstudy"))
    yearofstudy = []
    for row in result.all():
      yearofstudy.append(row)
    return yearofstudy

def add_application_to_db(data):
  with engine.connect() as conn:
    query = text("INSERT INTO application (gender, typesofstudies, yearofstudy, first_question, second_question, third_question, fourth_question, fifth_question, sixth_question, seventh_question, eighth_question, ninth_question, tenth_question, eleventh_question, twelfth_question, thirteenth_question, fourteenth_question, fifteenth_question, sixteenth_question, seventeenth_question, eighteenth_question, nineteenth_question, twentieth_question) VALUES (:gender, :typesofstudies, :yearofstudy,  :first_question, :second_question, :third_question, :fourth_question, :fifth_question, :sixth_question, :seventh_question, :eighth_question, :ninth_question, :tenth_question, :eleventh_question, :twelfth_question, :thirteenth_question, :fourteenth_question, :fifteenth_question, :sixteenth_question, seventeenth_question, :eighteenth_question, :nineteenth_question, :twentieth_question)") 
    conn.execute(query, {'gender': data['gender'], 'typesofstudies' : data['typesofstudies'], 'yearofstudy' : data['yearofstudy'], 'first_question': data['first_question'],'second_question': data['second_question'], 'third_question' : data['third_question'], 'fourth_question' : data['fourth_question'], 'fifth_question' : data['fifth_question'], 'sixth_question': data['sixth_question'] , 'seventh_question': data['seventh_question'], 'eighth_question': data['eighth_question'], 'ninth_question': data['ninth_question'],'tenth_question' : data['tenth_question'], 'eleventh_question' : data['eleventh_question'], 'twelfth_question' : data['twelfth_question'], 'thirteenth_question' : data['thirteenth_question'], 'fourteenth_question' : data['fourteenth_question'], 'fifteenth_question' : data['fifteenth_question'], 'sixteenth_question': data['sixteenth_question'], 'seventeenth_question' : data['seventeenth_question'], 'eighteenth_question' : data['eighteenth_question'], 'nineteenth_question' : data['nineteenth_question'], 'twentieth_question' : data['twentieth_question']})
            

    
    


