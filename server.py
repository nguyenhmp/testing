from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def index():
	if session.has_key('count'):
		session['count'] += 1
	else:
		session['count'] = 1
	return render_template('index.html', counter=session['count'])
@app.route('/two')
def two():
	session['count'] += 1
	return redirect('/')
@app.route('/reset')
def reset():
	session['count'] = 0
	return redirect('/')
app.run(debug=True)
