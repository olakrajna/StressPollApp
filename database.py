from sqlalchemy import create_engine, text 
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from firstquestion"))
    firstquestion = []
    for row in result.all():
      firstquestion.append(row)
    return firstquestion

engine = create_engine(
  db_connection_string, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

