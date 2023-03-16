from distutils.log import debug
from flask import Flask, redirect, render_template, url_for, render_template, request, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "secret"

db = SQLAlchemy(app)

class users(db.Model):
	_id = db.Column(db.Integer, primary_key = True)
	fname = db.Column(db.String(100))
	lname = db.Column(db.String(100))
	email = db.Column(db.String(100))
	password = db.Column(db.String(100))
	occupation = db.Column(db.String(100))
	def __init__(self, fname, lname, email, password, occupation):
		self.fname = fname
		self.lname = lname
		self.email = email
		self.password = password
		self.occupation = occupation

	def __init__(self, fname, lname, email, password, occupation):
		self.fname = fname
		self.lname = lname
		self.email = email
		self.password = password
		self.occupation = occupation


class activities(db.Model):
	_id = db.Column(db.Integer, primary_key = True)
	inSAPActivities = db.Column(db.String(100))
	location = db.Column(db.String(100))
	activeDate = db.Column(db.Date())
	activeTime = db.Column(db.Time())
	occupied = db.Column(db.Integer())

class friendships(db.Model):
	_id = db.Column(db.Integer, primary_key = True)
	ID1 = db.Column(db.Integer())
	ID2 = db.Column(db.Integer())

class events(db.Model):
	_id = db.Column(db.Integer, primary_key = True)
	eventName = db.Column(db.String(100))
	eventLocation = db.Column(db.String(100))
	eventDate = db.Column(db.Date())
	eventTime = db.Column(db.Time())
	eventParticipant = db.Column(db.String(100))


@app.route("/login",methods=["POST","GET"])
def login():
	if request.method == "POST":
		fname = "Ali"
		lname = "Tohidi"
		email = request.form.get("inputEmail")
		password = request.form.get("inputPassword")
		occupation = "Software Developer"

		#for session storage
		session["email"] = email
		session["password"] = password

		#for database storage		
		usr = users(fname,lname,email, password, occupation)
		db.session.add(usr)
		db.session.commit()
		return redirect(url_for("landing"))
	else:
		if "email" in session:
			return redirect(url_for("user"))
		return render_template("userLoginPage.html")

@app.route("/user")
def user():
	if "email" in session:
		user = session["email"]
		return f"<h1>{user}</h1>"	
	else:
		return redirect(url_for("login"))	

@app.route("/logout")
def logout():
	session.pop("email",None)
	session.pop("password",None)
	return redirect(url_for("login"))

@app.route("/view")
def view():
	return render_template("view.html",values = users.query.all())

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/outsideSAP")
def outsideSAP():
	return render_template("outsideSAP.html")

@app.route("/insideSAP")
def insideSAP():
	return render_template("insideSAP.html")


@app.route("/dashboard")
def dashboard():
	return render_template("dashboard.html", values = users.query.all())

@app.route("/calendar")
def calendar():
	return render_template("calendar.html")

@app.route("/landing")
def landing():
	return render_template("landing.html",values = users.query.all())

@app.route("/friends")
def friends():
	return render_template("friends.html")

@app.route("/activity/<activity>")
def activity(activity):
	return render_template("activityPage.html", value = activity, checkedin = False, eventCapacity= 18, eventParticipantCount = 10)

# @app.route("/admin")
# def admin():
#     return redirect(url_for("user", name="Admin!"))  # Now we when we go to /admin we will redirect to user with the argument "Admin!"

if __name__ == "__main__":
	db.create_all()
	app.run(debug = True)
