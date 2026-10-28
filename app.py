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
        {"name": "Gel Application", "price": "KSh 300", "desc": "Long-lasting, high-shine gel polish cured under LED light."},
        {"name": "Classic  Stick on plus French Tips", "price": "KSh 600", "desc": "Timeless, elegant white or colored tips on natural nails."},
        {"name": "DeluxeManicure", "price": "KSh 700", "desc": "Nail shaping, cuticle care, exfoliating scrub, and a relaxing hand massage."},
        {"name": "Deluxe Pedicure", "price": "KSh 700", "desc": "Foot soak, scrub, callus removal, massage, and professional toe polishing."},
        {"name": "Custom Nail Art", "price": "From KSh 50/nail", "desc": "Hand-painted designs, gems, chrome, or abstract line art tailored to you."},
        {"name": "Gumgel", "price": "KSh 1200", "desc": "A durable, flexible gel for nail extensions"},
        {"name": "Buider gel", "price": "KSh 800", "desc": "A strong gel for sculpting and extending nails"},
        {"name": "Overlay", "price": "KSh 1200", "desc": "A protective layer of gel or acrylic over natural nails for added strength and shine"},
        {"name": "lashes", "price": "KSh 500", "desc": "enhane your eyes with our proffesional lash extensions"}
        
        
    ]
    return render_template('home.html', services=nail_services)

if __name__ == '__main__':
    app.run(debug=True)