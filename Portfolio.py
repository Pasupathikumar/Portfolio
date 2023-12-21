'''

from flask import Flask, render_template
#import GoldRate

app = Flask(__name__, template_folder='Template', static_folder='Static')



@app.route('/')
#@app.route('/main')
def home():
    url='Template/Main.html'
    return render_template(url)
    #return render_template('sample.html')

@app.route('/goldrate')
#@app.route('/')
def Gold():

    return GoldRate.Gold()

if __name__=='__main__':
    app.run(debug=True)
'''

from flask import Flask, render_template
#from flask_limiter import Limiter
#from flask_limiter.util import get_remote_address

app = Flask(__name__, template_folder='Template', static_folder='Static')
#limiter = Limiter(app)

# Throttle requests to 10 requests per minute  C:\Users\Pasupathikumar.s\Desktop\NextBrainCompany\Portfolio\Portfolio.py

@app.route('/')
@app.route('/main')
#@limiter.limit("10/minute")
def index():
    url="Main.html"
    return render_template(url)

if __name__ == '__main__':
    app.run()
