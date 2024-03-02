from flask import Flask, render_template, request
import mongopark

app = Flask(__name__)
mongopark.setup()

@app.route('/')
def home():      
    return render_template('index.html')

@app.route('/handle_click', methods=["POST"])
def handle_click(): 
    add = request.form.get('button_add')
    remove = request.form.get('button_remove')
    
    if add == 'true':
        mongopark.addVehicle(request.form.get("license"), request.form.get("phone"))

if __name__ == "__main__":
    app.run(debug=True)