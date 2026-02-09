# Unit Converter Web App

A simple, beginner-friendly web application that converts between different units of measurement. Built with Python and Flask.

## Features

- **Length Converter** - Convert between millimeter, centimeter, meter, kilometer, inch, foot, yard, and mile
- **Weight Converter** - Convert between milligram, gram, kilogram, ounce, and pound
- **Temperature Converter** - Convert between Celsius, Fahrenheit, and Kelvin
- Clean, minimal interface with easy navigation
- Real-time conversion with instant results
- No database required

## Tech Stack

- **Backend:** Python 3, Flask
- **Frontend:** HTML5, CSS3
- **Template Engine:** Jinja2

## Installation

1. Clone the repository:
```bash
git clone https://github.com/akanjiolayinka/Unit-Converter-Web-App.git
cd Unit-Converter-Web-App
```

2. Install Flask:
```bash
pip install flask
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and visit:
```
http://127.0.0.1:5000/length
```

## Usage

1. Choose a converter type from the navigation menu (Length, Weight, or Temperature)
2. Enter the value you want to convert
3. Select the unit you're converting FROM
4. Select the unit you're converting TO
5. Click "Convert" to see the result

## Project Structure

```
Unit-Converter-Web-App/
├── app.py                  # Flask backend with conversion logic
├── templates/
│   ├── length.html        # Length converter page
│   ├── weight.html        # Weight converter page
│   └── temperature.html   # Temperature converter page
├── static/
│   └── style.css          # CSS styling
└── README.md
```

## How It Works

The app uses Flask routes to handle form submissions. When you submit a conversion:
1. The form sends a POST request to the current page
2. Flask reads the input value and selected units
3. Python performs the conversion calculation
4. The result is displayed below the form

All conversions use a base unit approach:
- **Length:** Converts through meters
- **Weight:** Converts through grams
- **Temperature:** Uses direct formulas (not ratios)

## License

This project is open source and available under the MIT License.
https://roadmap.sh/projects/unit-converter
