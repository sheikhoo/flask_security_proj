# flask_security_proj
flask simple security project

پروژه flask شامل صغحات
- صفحه ی login/logout
  - جلوگیری از کش اطلاعات توسط مرورگر
- صفحه ی ثبت نام
  - جلوگیری از انتخاب رمز ضعیف
  - هش کردن رمز عبور
- آپلود فایل
  - بررسی پسوند و حجم فایل
  - نیاز به لاگین 

### Start the Application with the help of Docker
Go to the project directory and execute 
the following command in the terminal

    docker-compose up
    
And we are done, the **Flask App** will be starting on port 
**5000** and **MySQL** is on **3306**

### Run Application Without Docker
#### Requirements
* python 3.6
* MySQL

#### Dependencies

    pip install flask
    pip install flask-mysqldb
    
#### Start
Go to the project directory and execute 
the following command in the terminal

    python app.py
    
