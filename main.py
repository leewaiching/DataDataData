from flask import Flask, render_template, request

app = Flask(__name__)




@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    info = request.form['data']
    info = info.upper()
    return render_template('index.html', output=info)
  return render_template('index.html')


app.run(host='0.0.0.0', port=81)
