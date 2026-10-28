from flask import Flask, render_template

app = Flask(__name__)

# 1. Home Page Route
@app.route('/')
def home():
    return render_template('home.html')

# 2. Services & Pricing Route
@app.route('/services')
def services():
    # Your real nail menu passed directly to the webpage
    nail_services = [
        {"name": "Gel Application", "price": "KSh 400", "desc": "Long-lasting, high-shine gel polish cured under LED light."},
        {"name": "Classic French Tips", "price": "KSh 600", "desc": "Timeless, elegant white or colored tips on natural nails."},
        {"name": "Massage Manicure", "price": "KSh 2,000", "desc": "Nail shaping, cuticle care, exfoliating scrub, and a relaxing hand massage."},
        {"name": "Deluxe Pedicure", "price": "KSh 2,500", "desc": "Foot soak, scrub, callus removal, massage, and professional toe polishing."},
        {"name": "Custom Nail Art", "price": "From KSh 100/nail", "desc": "Hand-painted designs, gems, chrome, or abstract line art tailored to you."}
    ]
    return render_template('services.html', services=nail_services)

if __name__ == '__main__':
    app.run(debug=True)
