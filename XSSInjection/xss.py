from flask import *
app = Flask(__name__)
app.secret_key = '1234567'

@app.route('/httponly')
def ho():
    resp=make_response(render_template('xss.html'))
    resp.set_cookie('a','b',httponly=True)
    resp.set_cookie('c','d')

    return resp

@app.route('/csp')
def csp_test():
    import random
    import string
    length = 10
    pool = string.ascii_lowercase
    result = ''

    for i in range(lenth):
        result = result + rondom.choice(pool)


    resp = make_response(render_template('xss.html',nonce = result))
    resp.headers['Content-Security-Policy'] = f"script-src 'nonce-{result}' "
    return resp



if __name__ == '__main__':
    app.run('0.0.0.0', port=80,debug=True)

