import pymysql
from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
def show():
    return render_template("home.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/f_login")
def first_login():
    return render_template("first_login.html")

@app.route("/add_student")
def add_student():
    return render_template("add_student.html")

@app.route("/info_sms",methods=["GET","POST"])
def info_sms():
    if request.method == "POST":
        o = request.form["s"]
        l = []
        db = pymysql.connect('localhost', 'root', '', 'flask')
        sql = "select * from stu_info where Mobileno=%s"
        val = (o)
        cur = db.cursor()
        cur.execute(sql, val)
        result = cur.fetchall()
        for row in result:
            l.append(row[4])
        return render_template("add_attendance.html",k=o,m=l)
    l = []
    db = pymysql.connect('localhost', 'root', '', 'flask')
    sql = "select * from stu_info"
    cur = db.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    for row in result:
        l.append(row[0])
    return render_template("info_sms.html", p=l)


@app.route("/reg")
def stu_register():
    return"<html><head><link href='../static/bootstrap.min.css' rel='stylesheet'><script src='../static/jquery.min.js'></script><script src='../static/bootstrap.min.js'></script></head><body><h1>Choose Here</h1><form method='POST' action='/reg'><div class='row'><div class='text-center'><button type='button' class='btn btn-primary btn-lg' >Faculty Register</button><br><br><a href='/k' class='btn btn-success btn-lg'>Student Register</a></div></div><form></body></html>"

@app.route("/ct_marks",methods=["GET","POST"])
def index():

    if request.method == "POST":
        mob = request.form["m"]
        ai = request.form["ai"]
        cns = request.form["cns"]
        dmw = request.form["dmw"]
        mis = request.form["mis"]
        cc = request.form["cc"]
        db = pymysql.connect('localhost', 'root', '', 'flask')
        sql = "insert into ctmarks value(%s,%s,%s,%s,%s,%s)"
        val = (mob, ai, cns, dmw, mis, cc)
        cur = db.cursor()
        cur.execute(sql, val)
        db.commit()
        return render_template("s.html", m=mob, n=ai, o=cns, p=dmw, q=mis, r=cc)
    return render_template("ct_sms.html")

@app.route("/add_attendance",methods=["GET","POST"])
def add_attendance():
        l=[]
        db = pymysql.connect('localhost', 'root', '', 'flask')
        sql = "select * from stu_info"
        cur = db.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            l.append(row[0])
        return render_template("index2.html", s=l)

@app.route("/k",methods=["GET","POST"])
def show1():

    if request.method == "POST":
        a = request.form["m"]
        b = request.form["n"]
        c = request.form["p"]
        d = request.form["q"]
        db = pymysql.connect('localhost', 'root', '', 'flask')
        sql = "insert into stu_register value(%s,%s,%s,%s)"
        val = (a, b, c, d)
        cur = db.cursor()
        cur.execute(sql, val)
        db.commit()
    return render_template("register.html")

@app.route("/add_student",methods=["GET","POST"])
def stu_information():
    if request.method == "POST":
        a = request.form["l"]
        b = request.form["m"]
        c = request.form["n"]
        d = request.form["o"]
        e = request.form["p"]
        f = request.form["q"]
        g = request.form["r"]
        h = request.form["s"]
        db = pymysql.connect('localhost', 'root', '', 'flask')
        sql = "insert into stu_info value(%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (a, b, c, d, e, f, g, h)
        cur = db.cursor()
        cur.execute(sql, val)
        db.commit()
    return render_template("add_student.html")

@app.route("/check",methods=["GET","POST"])
def check():
    if request.method == "POST":
        c=0
        m =request.form["x"]
        n = request.form["y"]
        db = pymysql.connect('localhost', 'root', '', 'flask')
        sql = "select * from stu_register"
        cur = db.cursor()
        cur.execute(sql)
        result=cur.fetchall()
        for row in result:
            if m==row[0] and n==row[2]:
                c=c+1
        if c==1:
            return render_template("add.html")
        else:
            return "invalid"

    return render_template("home.html")

app.run(port=3486,debug=True)