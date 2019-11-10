import model
from flask import *
app = Flask(__name__)

brain = None

def load_brain():
    global brain
    brain = model.load_model()

keys = ["q{}".format(x) for x in range(1,30)]


@app.route('/')
def intro_page():
   return render_template("index.html")

@app.route('/app')
def app_page():
   return render_template("app.html")

@app.route('/predict',methods =["POST"])
def predict_page():
    if request.method == 'POST':
        result = request.form
        all_answered = True
        for key in keys:
            if not (key in result):
                all_answered = False
                break                    
        if not all_answered:
            return render_template("predict.html",can_proceed = False)
        else:
            answers = []
            for key in keys:
                answers.append(int(result[key]))
            predicted_val = brain.predict([answers])
            if predicted_val == -1:
                return render_template("predict.html",can_proceed = True,result="Phishing")
            else:
                return render_template("predict.html",can_proceed = True,result="Legimate")





if __name__ == '__main__':
    load_brain()
    app.run(host="0.0.0.0",port=4567,debug=True)