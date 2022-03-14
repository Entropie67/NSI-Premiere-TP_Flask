from flask import Flask, render_template, request
import datetime
import codepython

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
  id = result['id']
  pwd = result['password']
  if codepython.identification(id, pwd):
    return render_template("result.html", nom=id, pwd=pwd)
  else:
    return f"<p>Pas moyen,d'ou tu imagines que c'est {id}</p>"

app.run(debug=True)