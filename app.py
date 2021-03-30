from flask import Flask, url_for, render_template
from authlib.integrations.flask_client import OAuth


app = Flask(__name__)
oauth = OAuth(app)



@app.route('/')
def hello_world():
    return "Hello......World!"


@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return oauth.twitter.authorize_redirect(redirect_uri)


@app.route('/authorize')
def authorize():
    token = oauth.twitter.authorize_access_token()
    resp = oauth.twitter.get('account/verify_credentials.json')
    resp.raise_for_status()
    profile = resp.json()
    # do something with the token and profile
    return redirect('/')





if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")