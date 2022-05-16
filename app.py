from flask import Flask,escape, request, render_template
import pickle
#Load model
vector=pickle.load(open("vectorizer.pkl",'rb'))
model=pickle.load(open("finalized_model.pkl",'rb'))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/prediction', methods=['GET','POST'])
def prediction():
    if request.method == "POST":
        news=str(request.form['news'])  #id of input data
        predict=model.predict(vector.transform([news]))[0]
        print(predict)
        if(predict==0):
            predict="REAL NEWS"
        else:
            predict="Fake NEWS"
        print(predict)    
        return render_template("prediction.html",prediction_text="The given News is -> {}".format(predict))
    else:
        return render_template("prediction.html")

@app.route("/work")
def work():
    return render_template("work.html")

if __name__=='__main__':
    app.run()