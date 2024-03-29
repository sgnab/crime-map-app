
from flask import Flask,render_template,request
import dbconfig
if dbconfig.test==True:
    from mockdbhelper import MockDBHelper as DBhelper
else:
    from dbhelper import DBhelper

app=Flask(__name__)

DB=DBhelper()


@app.route('/',methods=["GET"])
def home():
    try:
        data=DB.get_all_inputs()
    except Exception as e:
        print e
        data=None
    return render_template('home.html',data=data)


@app.route('/add',methods=["GET","POST"])
def addinput():
    try:
        data=request.form.get('userinput')
        DB.add_input(data)

    except Exception as e:
        print e

    return home()

@app.route('/clear',methods=["GET",'POST'])
def clearinput():
    try:
        DB.clear_input()
    except Exception as e:
        print e

    return home()

if __name__=="__main__":
    app.run(debug=True)