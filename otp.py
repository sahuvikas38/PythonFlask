import pymysql
import random
from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():

    if request.method=="POST":
        mob=request.form["m"]
        r=random.randint(1000,9999)
        msg="OTP:"+str(r)
        return render_template("sms.html",m=mob,n=msg)
    return render_template("index.html")
app.run(port=3489,debug=True)