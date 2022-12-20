import os
from flask import Flask,render_template,request,redirect,session,flash,url_for,abort
from functools import wraps
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash

app=Flask(__name__)
app.config['MYSQL_HOST']='db'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='toor'
app.config['MYSQL_DB']='db_sample'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql=MySQL(app)
 
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'uploads'

#Login
@app.route('/') 
@app.route('/login',methods=['POST','GET'])
def login():
    status=True
    if request.method=='POST':
        email=request.form["email"]
        pwd=request.form["upass"]
        cur=mysql.connection.cursor()
        cur.execute("select * from users where EMAIL=%s",[email])
        data=cur.fetchone()
        if data:
            if check_password_hash(data["UPASS"],pwd):
                session['logged_in']=True
                session['username']=data["UNAME"]
                flash('شما لاگین شدید','success')
                return redirect('home')
            else:
                flash('اطلاعات صحیح نمی باشد دوباره تلاش نمایید','danger')
        else:
            flash('اطلاعات صحیح نمی باشد دوباره تلاش نمایید','danger')
    return render_template("login.html")
  
#check if user logged in
def is_logged_in(f):
	@wraps(f)
	def wrap(*args,**kwargs):
		if 'logged_in' in session:
			return f(*args,**kwargs)
		else:
			flash('لطفا اول لاگین نمایید','danger')
			return redirect(url_for('login'))
	return wrap
  
#Registration  
@app.route('/reg',methods=['POST','GET'])
def reg():
    status=False
    if request.method=='POST':
        SpecialSym =['$', '@', '#', '%']
        val = True
        name=request.form["uname"]
        email=request.form["email"]
        pwd=request.form["upass"]

        if len(pwd) < 6:
            flash('طول رمز عبور باید حداقل 6 باشد','danger')
            val = False
            
        if len(pwd) > 20:
            flash('طول رمز عبور نباید بیشتر از 20 باشد','danger')
            val = False
            
        if not any(char.isdigit() for char in pwd):
            flash('رمز عبور باید حداقل یک عدد داشته باشد','danger')
            val = False
            
        if not any(char.isupper() for char in pwd):
            flash('رمز عبور باید حداقل یک حرف بزرگ داشته باشد','danger')
            val = False
            
        if not any(char.islower() for char in pwd):
            flash('رمز عبور باید حداقل یک حرف کوچک داشته باشد','danger')
            val = False
            
        if not any(char in SpecialSym for char in pwd):
            flash('رمز عبور باید حداقل یکی از نمادهای $@# را داشته باشد.','danger')
            val = False
            
        if val:
            cur=mysql.connection.cursor()
            cur.execute("insert into users(UNAME,UPASS,EMAIL) values(%s,%s,%s)",(name,generate_password_hash(pwd),email))
            mysql.connection.commit()
            cur.close()
            flash('ثبت نام با موفقیت انجام شد','success')
            return redirect('login')
    return render_template("reg.html",status=status)

#uploader
@app.route('/uploader', methods = ['POST','GET'])
@is_logged_in
def uploader():
    if request.method=='POST':
        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                abort(400)
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        flash('فایل با موفقیت آپلود شد','success')
    return render_template('upload.html')

#Home page
@app.route("/home")
@is_logged_in
def home():
	return render_template('home.html')
    
#logout
@app.route("/logout")
def logout():
	session.clear()
	flash('شما با موفقیت خارج شدید','success')
	return redirect(url_for('login'))
    
# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response

if __name__=='__main__':
    app.secret_key='secret123'
    app.run(host='0.0.0.0',debug=True)