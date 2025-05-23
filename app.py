from flask import Flask, request
import math
import psycopg2

app = Flask(__name__)

#Database connection
def get_db_connection():
  conn = psycopg2.connect(
    host = "db",
    database = "flaskdb",
    user = "flaskuser",
    password = "1234"
  )
  return conn

@app.route('/')
def home():
  return 'Welcome! Please go to <a href="/form">/form</a> to submit your info.'
@app.route('/save', methods=['POST'])
def save():
  firstname = request.form['firstname']
  lastname = request.form['lastname']
  height = float(request.form['height'])
  phone = request.form['phone']
# Simple formula for healthy weight range based on height
  min_weight = math.floor(18.5 * height * height / 10000)
  max_weight = math.ceil(24.9 * height * height / 10000)
#save to database
  conn = get_db_connection()
  cur = conn.cursor()
  cur.execute('INSERT INTO users(firstname,lastname,phone,height) VALUES (%s,%s,%s,%s)',
  (firstname,lastname,phone,height))
  conn.commit()
  cur.close()
  conn.close()

# Show result on the browser for you
  return f"""
  Hello {firstname} {lastname}!<br>
  Phone: {phone}<br>
  Height: {height} cm<br>
  Suggested Weight Range: {min_weight} kg- {max_weight} kg <br>
  <b> Your data has been saved successfully! </b>
  """
if __name__=='__main__':
  app.run(host='0.0.0.0', debug=True)
