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
    
def load_genders_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from genders"))
    genders = []
    for row in result.all():
      genders.append(row)
    return genders
    
# def load_job_from_db(id):
#   with engine.connect() as conn:
#     result = conn.execute(
#       text("SELECT * FROM firstquestion WHERE id = :val"),
#       val=id
#     )
#     rows = result.all()
#     if len(rows) == 0:
#       return None
#     else:
#       return dict(rows[0])
    


def add_application_to_db(data):
  with engine.connect() as conn:
    query = text("INSERT INTO applicationn (gender, first_question, second_question) VALUES (:gender, :first_question, :second_question)") 
    conn.execute(query, {'gender': data['gender'],'first_question': data['first_question'], 'second_question': data['second_question']})
            

    
    


