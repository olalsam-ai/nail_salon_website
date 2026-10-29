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
        {"name": "Gel Application", "price": "KSh 300", "image": "gel_application.jpeg", "desc": "Long-lasting, high-shine gel polish cured under LED light."},
        {"name": "Classic Stick on plus French Tips", "price": "KSh 600", "image":"nail2_art.jpeg", "desc": "Timeless, elegant white or colored tips on natural nails."},
        {"name": "Deluxe Manicure", "price": "KSh 500", "image": "deluxe_manicure.jpeg", "desc": "Nail shaping, cuticle care, exfoliating scrub, and a relaxing hand massage."},
        {"name": "Deluxe Pedicure", "price": "KSh 700", "image": "deluxe_pedicure.jpeg", "desc": "Foot soak, scrub, callus removal, massage, and professional toe polishing."},
        {"name": "Custom Nail Art", "price": "From KSh 50/nail", "image": "custom_nail3_art.jpeg", "desc": "Hand-painted designs, gems, chrome, or abstract line art tailored to you."},
        {"name": "Gumgel", "price": "KSh 1200", "image": "gumgel.jpeg", "desc": "A durable, flexible gel for nail extensions"},
        {"name": "Builder Gel", "price": "KSh 800", "image": "frenchtip2.jpeg", "desc": "A strong gel for sculpting and extending nails"},
        {"name": "Overlay", "price": "KSh 1100", "image": "overlay.jpeg", "desc": "A protective layer of gel or acrylic over natural nails for added strength and shine"},
        {"name": "Lashes", "price": "KSh 500", "image": "lashes.jpeg", "desc": "Enhance your eyes with our professional lash extensions"}

        
    ]
    return render_template('services.html', services=nail_services)

if __name__ == '__main__':
    app.run(debug=True)