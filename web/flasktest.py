from flask  import Flask;
from flask import request;

app = Flask(__name__);

@app.route('/',methods=['POST'])

def  home():
	return '<h1>Home</h1>';

@app.route('/signin',methods=['GET'])
def  signinin_form():
	return '''<form action="/signin" method="post">
			  <p><input name="username"></p>
			  <p><input name="password" type="password"></p>
			  <p><button type="submit">Sign In</button></p>
			  </form>'''

@app.route('/signin',methods=['POST'])
def  signin():
	if  request.form['username'] == 'admin' and request.form['password']=='password':
		return  '<h3> hello admin </h3>';
	return '<h3> Bad user or passworld </h3>' ;


if  __name__ == '__main__':
	app.run();