from flask import Flask, render_template, request, url_for, redirect
import os


app = Flask(__name__)



#port=int(os.getenv('PORT'))
port=os.environ['PORT']
print("port===",port)
data=os.environ['CHANNEL_DATA']


@app.route('/')
@app.route('/index')
def index():
    return render_template("test.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        selection = request.form.get("cars", None)
        if selection!=None:
            return render_template("test.html", rlink = data[selection],selection=selection)
        #else:
        #    return render_template("test.html", selection="Select Region")
    return render_template("test.html")

if __name__ == '__main__':
    #app.run(threaded=True,port=port,host='0.0.0.0')
    app.run(threaded=True,port=port)

    
    
