from dbhelper import DBhelper
from flask import Flask,render_template,request

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
        data=request.args.get('userinput')
        DB.addinput(data)

    except Exception as e:
        print e

    return home()

@app.route('/clear',methods=["GET",'POST'])
def clearinput():
    try:
        DB.clearinput()
    except Exception as e:
        print e

    return home()

if __name__=="__main__":
    app.run(debug=True)