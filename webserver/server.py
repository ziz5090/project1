#!/usr/bin/env python2.7

"""
Columbia W4111 Intro to databases
Example webserver

To run locally

    python server.py

Go to http://localhost:8111 in your browser


A debugger such as "pdb" may be helpful for debugging.
Read about it online.
"""

import os
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template,url_for, g, redirect, Response

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)


#
# The following uses the sqlite3 database test.db -- you can use this for debugging purposes
# However for the project you will need to connect to your Part 2 database in order to use the
# data
#
# XXX: The URI should be in the format of: 
#
#     postgresql://USER:PASSWORD@w4111db.eastus.cloudapp.azure.com/username
#
# For example, if you had username ewu2493, password foobar, then the following line would be:
#
DATABASEURI = "postgresql://zz2371:YFFSNB@w4111db.eastus.cloudapp.azure.com/zz2371"
#
#DATABASEURI = "sqlite:///test.db"

#
# This line creates a database engine that knows how to connect to the URI above
#
engine = create_engine(DATABASEURI)

usernameAndPassword = dict()
#
# START SQLITE SETUP CODE
#
# after these statements run, you should see a file test.db in your webserver/ directory
# this is a sqlite database that you can query like psql typing in the shell command line:
# 
#     sqlite3 test.db
#
# The following sqlite3 commands may be useful:
# 
#     .tables               -- will list the tables in the database
#     .schema <tablename>   -- print CREATE TABLE statement for table
# 
# The setup code should be deleted once you switch to using the Part 2 postgresql database
#
#engine.execute("""DROP TABLE IF EXISTS test;""")
#engine.execute("""CREATE TABLE IF NOT EXISTS test (
#  id serial,
#  name text
#);""")
#engine.execute("""CREATE TABLE IF NOT EXISTS users (
#  name text,
#  password int
#);""")


#engine.execute("""INSERT INTO test(name) VALUES ('grace hopper'), ('alan turing'), ('ada lovelace');""")

#
# END SQLITE SETUP CODE
#



@app.before_request
def before_request():
  """
  This function is run at the beginning of every web request 
  (every time you enter an address in the web browser).
  We use it to setup a database connection that can be used throughout the request

  The variable g is globally accessible
  """
  try:
    g.conn = engine.connect()
  except:
    print "uh oh, problem connecting to database"
    import traceback; traceback.print_exc()
    g.conn = None

@app.teardown_request
def teardown_request(exception):
  """
  At the end of the web request, this makes sure to close the database connection.
  If you don't the database could run out of memory!
  """
  try:
    g.conn.close()
  except Exception as e:
    pass


#
# @app.route is a decorator around index() that means:
#   run index() whenever the user tries to access the "/" path using a GET request
#
# If you wanted the user to go to e.g., localhost:8111/foobar/ with POST or GET then you could use
#
#       @app.route("/foobar/", methods=["POST", "GET"])
#
# PROTIP: (the trailing / in the path is important)
# 
# see for routing: http://flask.pocoo.org/docs/0.10/quickstart/#routing
# see for decorators: http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
loginName ="?"

@app.route('/')
def index():
  """
  request is a special object that Flask provides to access web request information:

  request.method:   "GET" or "POST"
  request.form:     if the browser submitted a form, this contains the data in the form
  request.args:     dictionary of URL arguments e.g., {a:1, b:2} for http://localhost?a=1&b=2

  See its API: http://flask.pocoo.org/docs/0.10/api/#incoming-request-data
  """

  # DEBUG: this is debugging code to see what request looks like
  print request.args
  try: 
  	cursor = g.conn.execute("SELECT User_Name,Password FROM users")
  except Exception, e:
	pass	
  rec = cursor.fetchall()
  for row in rec:
      usernameAndPassword[row[0]] = row[1];
  cursor.close()




  #
  # Flask uses Jinja templates, which is an extension to HTML where you can
  # pass data to a template and dynamically generate HTML based on the data
  # (you can think of it as simple PHP)
  # documentation: https://realpython.com/blog/python/primer-on-jinja-templating/
  #
  # You can see an example template in templates/index.html
  #
  # context are the variables that are passed to the template.
  # for example, "data" key in the context variable defined below will be 
  # accessible as a variable in index.html:
  #
  #     # will print: [u'grace hopper', u'alan turing', u'ada lovelace']
  #     <div>{{data}}</div>
  #     
  #     # creates a <div> tag for each element in data
  #     # will print: 
  #     #
  #     #   <div>grace hopper</div>
  #     #   <div>alan turing</div>
  #     #   <div>ada lovelace</div>
  #     #
  #     {% for n in data %}
  #     <div>{{n}}</div>
  #     {% endfor %}
  #
  Name = loginName
  context = dict(data = Name)


  #
  # render_template looks in the templates/ folder for files.
  # for example, the below file reads template/index.html
  #
  return render_template("index.html",**context)

#
# This is an example of a different path.  You can see it at
# 
#     localhost:8111/another
#
# notice that the functio name is another() rather than index()
# the functions for each app.route needs to have different names
#define global variable username
@app.route('/loginFinish')
def loginFinish():
    return render_template('loginFinish.html')

@app.route('/pleaseLogin')
def pleaseLogin():
    return render_template('pleaseLogin.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    render_template('login.html')
    error = None
    global loginName
    if loginName != "?":
	error = 'You have to logout first'
	return render_template('login.html', error=error)
    if request.method == 'POST':
	username = request.form['username'] 
        if username not in usernameAndPassword.keys():
	    error = 'Invalid user name'
	elif request.form['password'] != usernameAndPassword.get(username): 
            error = 'Invalid Credentials. Please try again.'
        else:
	    loginName = username
            return redirect(url_for('loginFinish'))
    return render_template('login.html', error=error)
# Example of adding new data to the database
#@app.route('/add', methods=['POST'])
#def add():
#  name = request.form['name']
 # g.conn.execute('INSERT INTO test VALUES (NULL, ?)', name)
 # return redirect('/')
@app.route('/addBook')
def addBook():
  if loginName == "?":
	return render_template('pleaseLogin.html')
  return render_template('addBook.html')
#add a new book feature
@app.route('/addbook',methods = ['POST'])
def addbook():
  ISBN = request.form['ISBN']
  Language = request.form['language']
  Title = request.form['Title']
  Price = request.form['Price']
  pubname = request.form['pub_name']
  category = request.form['category']
  year = request.form['book_year']
  error = None
  if ISBN is None or ISBN =='':
#  if ISBN.isdigit() is false:
	error = "invalid isbn"
	return render_template('commentError.html',error = error)
  if Language is None or Language =='':
	error = "invalid language"
	return render_template('commentError.html',error = error)

  if Title is None or Title =='':
        error = "invalid title"
	return render_template('commentError.html',error = error)

  if int(Price)<0 or Price is None or Price =='':
	error = "invalid price must >0"
	return render_template('commentError.html',error = error)

  if pubname is None or pubname =='':
	error = "invalid publisher"
	return render_template('commentError.html',error = error)

  if category is None or category =='':
        error ="invalid category"
	return render_template('commentError.html',error = error)

  if year is None or year =='':
        error= "invalid year"
	return render_template('commentError.html',error = error)
 
	
  temp = (ISBN,Language,Title,Price,pubname,category, year)
  cursor = g.conn.execute("INSERT INTO book(isbn,language,title,price,pub_name,category,book_year) VALUES(%s,%s,%s,%s,%s,%s,%s)",temp)
  cursor.close()
  return redirect(url_for('addBookFinish'))
#define global variable
bookname = None

@app.route('/search_book',methods=['POST'])
def search_book():
   if loginName == "?":
	return render_template('pleaseLogin.html')
   global bookname
   bookname = request.form['bookname']
   return redirect(url_for('search'))

def updateSearched():
   count = 0
   cursor2 = g.conn.execute("""SELECT c.searched FROM users u,comments c WHERE c.id = u.id and c.isbn = %s and u.user_name = %s""",(isbn,loginName,))
   rec2 =cursor2.fetchall()
   for row in rec2:
	count = int(row[0])
   count = count +1
   cursor3 =g.conn.execute("""UPDATE comments SET searched = %s WHERE isbn =%s""",(str(count),isbn,))


@app.route('/Duplicate')
def Duplicate():
	return render_template('Duplicate.html')

@app.route('/add_comment',methods=['POST'])
def add_comment():
   error= None
   if loginName =="?":
	return render_template('pleaseLogin.html')
   cursor1 = g.conn.execute("""SELECT c.isbn FROM users u,comments c WHERE c.id = u.id and u.user_name = %s""",(loginName,))
   wish = request.form['wish']
   read = request.form['read']
   rate = request.form['Rate']
   int_rate = int(rate)
   if wish != 'true' and wish != 'false':
	error = 'please input valid wish value: true or false'
	return render_template('commentError.html',error = error)
   if read != 'true' and read != 'false':
        error = 'please input valid read value: true or false'
   	return render_template('commentError.html',error = error)
   if int_rate>5 or int_rate<0:
	error = 'please input valid rate 0-5'
   	return render_template('commentError.html',error = error)
 
   uid = getUID(loginName)
   isbn_rec=[]
   rec = cursor1.fetchall()
   for row in rec:
	isbn_rec.append(row[0])
   cursor1.close()
   if isbn in isbn_rec:
	return redirect(url_for('Duplicate'))
   count = 0
   cursor2 = g.conn.execute("""SELECT c.searched FROM users u,comments c WHERE c.id = u.id and c.isbn = %s and u.user_name = %s""",(isbn,loginName,))
   rec2 =cursor2.fetchall()
   for row in rec2:
	count = int(row[0])
   cursor2.close() 
   temp =(wish,isbn,uid, read, rate, count, 'now')
   try:
   	cursor = g.conn.execute("INSERT INTO comments(Wished, ISBN,ID,Have_read,Rate,Searched,Time) VALUES(%s,%s,%s,%s,%s,%s,%s)",temp)
   except Exception, e:
	pass
   cursor.close()
   return redirect(url_for('addCommentFinish'))

@app.route('/addCommentFinish')
def addCommentFinish():
	return render_template('addCommentFinish.html')
#
#search feature
isbn =None
@app.route('/search')
def search():
   temp = []
   info = []
   cursor = g.conn.execute("""SELECT * FROM book WHERE Title = %s;""",(bookname,))
   if cursor is None:
	context = 'The book is not in the database'
   else:
        rec = cursor.fetchall()
	global isbn
  	for row in rec:
#	    for x in range(0,5):
		isbn = row[0]
		temp.append("Title: "+row[2])
		temp.append("Language: "+row[1])
		temp.append("ISBN: "+isbn)
		temp.append("Price: "+str(row[3]))
		temp.append("Publisher: "+row[4])
		temp.append("Category: "+row[5])
                temp.append("Year: "+str(row[6]))
   	context = dict(info = temp) 
	cursor.close()
        updateSearched()
   return render_template('search.html', **context)

def getUID( str):
    "This get UID from loginName"
    cursor = g.conn.execute("""SELECT id FROM users WHERE user_name = %s;""",(loginName,))
    rec = cursor.fetchall()
    for row in rec:
    	UID = row[0]
    cursor.close()
    return UID

c=[]

@app.route('/addBookFinish')
def addBookFinish():
  return render_template('addBookFinish.html')
#
@app.route('/logout',methods = ['POST'])
def logout():
  global loginName
  if loginName=="?":
	return render_template('logout.html')
  loginName = "?"
  return render_template('logout.html')
#recommendation feature
@app.route('/recommend')
def recommend():
  temp = []
  cursor = g.conn.execute("SELECT DISTINCT category FROM book")
  rec = cursor.fetchall()
  for row in rec:
      temp.append(row[0])
  context = dict(info = temp)
  cursor.close()
  global c 
  c= list(temp)
  return render_template('recommendation.html',**context)

@app.route('/recommend_book',methods = ['POST'])
def recommend_book():
  temp = []
  error = None
  bookType =request.form['name'] 
  if bookType not in c:
  	return render_template('recommendation.html',error=error)
  cursor = g.conn.execute("""SELECT b.isbn,b.title,avg(c.rate),l.web_address From BOOK b, comments c ,linked_to l WHERE b.category =%s and c.isbn =b.isbn and l.isbn=b.isbn group by b.isbn,b.title,l.web_address order by avg(c.rate) desc nulls last;""",(bookType,))
  rec = cursor.fetchall()
  for row in rec:
      temp.append(str(row[1])+" "+str('{0:.1f}'.format(row[2])))
      temp.append("Link: "+row[3])
  context2 = dict(info2 = temp)
  cursor.close()
  return render_template('recommendation.html',**context2)


if __name__ == "__main__":
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8113, type=int)
  def run(debug, threaded, host, port):
    """
    This function handles command line parameters.
    Run the server using

        python server.py

    Show the help text using

        python server.py --help

    """

    HOST, PORT = host, port
    print "running on %s:%d" % (HOST, PORT)
    app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)    #Load username & password
  run()
