from flask import Flask, flash, redirect, render_template, request, session, url_for, flash
#from flask_bootstrap import Bootstrap

app = Flask(__name__)
#Bootstrap(app)
#app.secret_key= "pickaprivatekeyplease"
@app.route("/rogan", methods=['GET', 'POST'])
def rogan():
    return render_template('Rogan.html')

@app.route("/ballard", methods=['GET', 'POST'])
def ballard():
    return render_template('Ballard.html')

@app.route("/rosborough", methods=['GET', 'POST'])
def rosborough():
    return render_template('Rosborough.html')

@app.route("/gillespie", methods=['GET', 'POST'])
def gillespie():
    return render_template('Gillespie.html')

@app.route("/wa", methods=['GET', 'POST'])
def wa():
    return render_template('WA.html')

@app.route("/index", methods=['GET', 'POST'])
def index():
    return render_template('index.html')



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
