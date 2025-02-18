from flask import Flask, render_template, request, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import json

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = params.get("local_server", "False").lower() == "true"
app = Flask(__name__)
app.secret_key = 'super-secret-key'

if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['proud_uri']

db = SQLAlchemy(app)

class AddVuln(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    username = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    segment = db.Column(db.String(120), nullable=False)

class Posts(db.Model):
    vulnid = db.Column(db.Integer, primary_key=True)
    vulnerability = db.Column(db.String(80), nullable=False)
    segment = db.Column(db.String(200), nullable=False)
    cve = db.Column(db.String(200), nullable=False)
    finder = db.Column(db.String(120), nullable=False)

@app.route("/")
def hello():
    return render_template('index.html', params=params)

@app.route("/index")
def home():
    return render_template('dashboard.html', params=params)

@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        sql_query = request.form.get('sqlQuery')
        try:
            result = db.session.execute(sql_query)
            flash("Query executed successfully", "success")
            if result.returns_rows:
                rows = result.fetchall()
                return render_template('search.html', query_results=rows, table_info=get_table_info())
        except Exception as e:
            flash(f"Error executing query: {e}", "danger")
    return render_template('search.html')

def get_table_info():
    table_info = {}
    for table in db.metadata.tables.values():
        table_name = table.name
        columns = [col.name for col in table.columns]
        table_info[table_name] = columns
    return table_info

@app.route("/execute_query", methods=['POST'])
def execute_query():
    if request.method == 'POST':
        sql_query = request.form.get('sqlQuery')
        try:
            result = db.session.execute(sql_query)
            flash("Query executed successfully", "success")
            if result.returns_rows:
                rows = result.fetchall()
                return render_template('search.html', query_results=rows, table_info=get_table_info())
        except Exception as e:
            flash(f"Error executing query: {e}", "danger")
    return redirect('/search')

@app.route("/details", methods=['GET', 'POST'])
def details():
    if 'user' in session and session['user'] == params['user']:
        posts = AddVuln.query.all()
        print(len(posts))
        return render_template('details.html', params=params, posts=posts)

@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html', params=params)

@app.route("/insert", methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        vulnid = request.form.get('vulnid')
        vulnerability = request.form.get('Vulnerability')
        segment = request.form.get('Segment')
        cve = request.form.get('CVE')
        finder = request.form.get('Finder')
        push = Posts(vulnid=vulnid, vulnerability=vulnerability, segment=segment, cve=cve, finder=finder)
        db.session.add(push)
        db.session.commit()
        flash("Thanks for submitting your details", "danger")
    return render_template('insert.html', params=params)

@app.route("/list", methods=['GET', 'POST'])
def post():
    if 'user' in session and session['user'] == params['user']:
        posts = Posts.query.all()
        print(len(posts))
        return render_template('post.html', params=params, posts=posts)

@app.route("/logout")
def logout():
    session.pop('user')
    flash("You are logged out", "primary")
    return redirect('/login')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if 'user' in session and session['user'] == params['user']:
        posts = Posts.query.all()
        return render_template('dashboard.html', params=params, posts=posts)
    if request.method == 'POST':
        username = request.form.get('uname')
        userpass = request.form.get('password')
        if username == params['user'] and userpass == params['password']:
            session['user'] = username
            posts = Posts.query.all()
            flash("You are logged in", "primary")
            return render_template('index.html', params=params, posts=posts)
        else:
            flash("Wrong password", "danger")
    return render_template('login.html', params=params)

@app.route("/edit/<string:vulnid>", methods=['GET', 'POST'])
def edit(vulnid):
    if 'user' in session and session['user'] == params['user']:
        if request.method == 'POST':
            vulnerability = request.form.get('Vulnerability')
            segment = request.form.get('Segment')
            cve = request.form.get('CVE')
            finder = request.form.get('Finder')
            post = Posts.query.filter_by(vulnid=vulnid).first()
            post.vulnerability = vulnerability
            post.segment = segment
            post.cve = cve
            post.finder = finder
            db.session.commit()
            flash("Data updated", "success")
            return redirect('/edit/' + vulnid)
        post = Posts.query.filter_by(vulnid=vulnid).first()
        return render_template('edit.html', params=params, post=post)

@app.route("/deletemp/<string:vulnid>", methods=['GET', 'POST'])
def deletemp(vulnid):
    if 'user' in session and session['user'] == params['user']:
        post = Posts.query.filter_by(vulnid=vulnid).first()
        db.session.delete(post)
        db.session.commit()
        flash("Deleted successfully", "primary")
    return redirect('/list')

@app.route("/medicines", methods=['GET', 'POST'])
def medicine():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            description = request.form.get('description')
            username = request.form.get('username')
            email = request.form.get('email')
            segment = request.form.get('Segment')
            sql_query = text("INSERT INTO add_vuln (name, description, username, email, segment) "
                             "VALUES (:name, :description, :username, :email, :segment)")
            db.session.execute(sql_query, {'name': name, 'description': description, 'username': username, 'email': email, 'segment': segment})
            db.session.commit()
            flash("Data added successfully", "primary")
        except Exception as e:
            flash(f"Error adding data: {e}", "danger")
    return render_template('medicine.html', params=params)

if __name__ == '__main__':
    app.run(debug=True)


