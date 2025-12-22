from flask import Flask, render_template, request

app = Flask(__name__)

# Length conversion - everything to meters first
def convert_length(value, from_unit, to_unit):
    # Convert to meters
    to_meters = {
        'millimeter': 0.001,
        'centimeter': 0.01,
        'meter': 1,
        'kilometer': 1000,
        'inch': 0.0254,
        'foot': 0.3048,
        'yard': 0.9144,
        'mile': 1609.34
    }
    
    # Convert input to meters, then to target unit
    meters = value * to_meters[from_unit]
    result = meters / to_meters[to_unit]
    return result

# Weight conversion - everything to grams first
def convert_weight(value, from_unit, to_unit):
    # Convert to grams
    to_grams = {
        'milligram': 0.001,
        'gram': 1,
        'kilogram': 1000,
        'ounce': 28.3495,
        'pound': 453.592
    }
    
    # Convert input to grams, then to target unit
    grams = value * to_grams[from_unit]
    result = grams / to_grams[to_unit]
    return result

# Temperature conversion - direct formulas
def convert_temperature(value, from_unit, to_unit):
    # Convert to Celsius first
    if from_unit == 'Celsius':
        celsius = value
    elif from_unit == 'Fahrenheit':
        celsius = (value - 32) * 5/9
    else:  # Kelvin
        celsius = value - 273.15
    
    # Convert from Celsius to target unit
    if to_unit == 'Celsius':
        return celsius
    elif to_unit == 'Fahrenheit':
        return (celsius * 9/5) + 32
    else:  # Kelvin
        return celsius + 273.15

@app.route('/')
def home():
    return render_template('length.html')

@app.route('/length', methods=['GET', 'POST'])
def length():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = convert_length(value, from_unit, to_unit)
    
    return render_template('length.html', result=result)

@app.route('/weight', methods=['GET', 'POST'])
def weight():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = convert_weight(value, from_unit, to_unit)
    
    return render_template('weight.html', result=result)

@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = convert_temperature(value, from_unit, to_unit)
    
    return render_template('temperature.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
