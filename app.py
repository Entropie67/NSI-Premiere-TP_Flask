from flask import Flask, render_template, request
import datetime


app = Flask(__name__)

@app.route('/')
def index():
  date = datetime.datetime.now()
  h = date.hour
  m = date.minute
  s = date.second
  return render_template("index.html", heure=h, minute=m, seconde=s)

@app.route('/result',methods = ['POST'])
def resultat():
  result = request.form
  n = result['nom']
  p = result['prenom']
  return render_template("result.html", nom=n, prenom=p)

app.run(debug=True)