from flask import Flask, url_for, render_template
from authlib.integrations.flask_client import OAuth


app = Flask(__name__)
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
    client_kwargs={'scope': 'openid email profile'},
)



@app.route('/')
def hello_world():
    return "Hello......World!"


@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return oauth.twitter.authorize_redirect(redirect_uri)


@app.route('/authorize')
def authorize():
    token = oauth.twitter.authorize_access_token()      #creates the Google OAuth client
    resp = oauth.twitter.get('userinfo')                #Access token from Google (to get user info) on line 16
    resp.raise_for_status()                             #Containers the information you specified in scope (line 17)
    user_info = resp.json()                             #Sets user_info equal to the .json response from url in line 16 and information specified in line 17
    # do something with the token and profile
    return redirect('/')





if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")