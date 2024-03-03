from flask import Flask, render_template, request
import mongopark

app = Flask(__name__)
mongopark.setup()

empty = "parking-spot"
full = "parking-spot-taken"

@app.route('/')
def home():   
    return render_template('index.html')

@app.route('/', methods=["POST"])
def get_value():
    global empty
    global full
    global grid
    license = request.form["license"]
    number = request.form["phone"]
    add = request.form["button_add"]
    
    
    print(add)
    #this causes me physical pain to do
    if add == 'true':
        grid = mongopark.addVehicle(int(license), int(number))
        if grid=='1,1':
            return render_template('index.html', r11=full)
        elif grid=='1,2':
            return render_template('index.html', r12=full)
        elif grid=='1,3':
            return render_template("index.html", r13=full)
        elif grid=='1,4':
            return render_template("index.html", r14=full)
        elif grid=='1,5':
            return render_template("index.html", r15=full)
        elif grid=='1,6':
            return render_template("index.html", r16=full)
        elif grid=='1,7':
            return render_template("index.html", r17=full)
        elif grid=='1,8':
            return render_template("index.html", r18=full)
        elif grid=='2,1':
            return render_template('index.html', r21=full)
        elif grid=='2,2':
            return render_template('index.html', r22=full)
        elif grid=='2,3':
            return render_template("index.html", r23=full)
        elif grid=='2,4':
            return render_template("index.html", r24=full)
        elif grid=='2,5':
            return render_template("index.html", r25=full)
        elif grid=='2,6':
            return render_template("index.html", r26=full)
        elif grid=='2,7':
            return render_template("index.html", r27=full)
        elif grid=='2,8':
            return render_template("index.html", r28=full)
        elif grid=='3,1':
            return render_template('index.html', r31=full)
        elif grid=='3,2':
            return render_template('index.html', r32=full)
        elif grid=='3,3':
            return render_template("index.html", r33=full)
        elif grid=='3,4':
            return render_template("index.html", r34=full)
        elif grid=='3,5':
            return render_template("index.html", r35=full)
        elif grid=='3,6':
            return render_template("index.html", r36=full)
        elif grid=='3,7':
            return render_template("index.html", r37=full)
        elif grid=='3,8':
            return render_template("index.html", r28=full)
        elif grid=='4,1':
            return render_template('index.html', r41=full)
        elif grid=='4,2':
            return render_template('index.html', r42=full)
        elif grid=='4,3':
            return render_template("index.html", r43=full)
        elif grid=='4,4':
            return render_template("index.html", r44=full)
        elif grid=='4,5':
            return render_template("index.html", r45=full)
        elif grid=='4,6':
            return render_template("index.html", r46=full)
        elif grid=='4,7':
            return render_template("index.html", r47=full)
        elif grid=='4,8':
            return render_template("index.html", r48=full)
        elif grid=='5,1':
            return render_template('index.html', r51=full)
        elif grid=='5,2':
            return render_template('index.html', r52=full)
        elif grid=='5,3':
            return render_template("index.html", r53=full)
        elif grid=='5,4':
            return render_template("index.html", r54=full)
        elif grid=='5,5':
            return render_template("index.html", r55=full)
        elif grid=='5,6':
            return render_template("index.html", r56=full)
        elif grid=='5,7':
            return render_template("index.html", r57=full)
        elif grid=='5,8':
            return render_template("index.html", r58=full)
        elif grid=='6,1':
            return render_template('index.html', r61=full)
        elif grid=='6,2':
            return render_template('index.html', r62=full)
        elif grid=='6,3':
            return render_template("index.html", r63=full)
        elif grid=='6,4':
            return render_template("index.html", r64=full)
        elif grid=='6,5':
            return render_template("index.html", r65=full)
        elif grid=='6,6':
            return render_template("index.html", r66=full)
        elif grid=='6,7':
            return render_template("index.html", r67=full)
        elif grid=='6,8':
            return render_template("index.html", r68=full)
    return render_template('index.html')
    
 
    
if __name__ == "__main__":
    app.run(debug=True)