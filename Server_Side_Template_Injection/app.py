from flask import *
app = Flask(__name__)
app.secret_key = '1234567'

@app.route('/')
def index():
    ssti = request.args.get('ssti')
    html_data = f'''
    <html>
    <h1> {ssti} </h1>
    </html>
'''
    return render_template_string(html_data)

@app.route('/b')
def ssti():
    ssti = request.args.get('ssti')
    return render_template('ssti.html',title=ssti)

if __name__ == '__main__':
    app.run('0.0.0.0', port=80,debug=True)


