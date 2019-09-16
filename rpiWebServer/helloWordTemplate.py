from flask import Flask, render_template
from flask import make_response, Response
import sqlite3
import datetime
app = Flask(__name__)

@app.route('/AnimeMindo')
def AnimeMindo():
   return render_template('AnimeMindo.html')


@app.route('/Imagenes')
def Imagenes():
    db = sqlite3.connect('prueba_blob.sqlite')
    img = db.execute('SELECT * FROM imagenes').fetchone()
    print("select")
    response = make_response(img[1])
    response.headers['Content-Type'] = img[2]
    response.headers['Content-Disposition'] = 'attachment; filename=img.jpg'
    return (response)
    
@app.route("/")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
   return render_template('index.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)