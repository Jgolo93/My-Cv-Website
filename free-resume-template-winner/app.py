from flask import Flask, render_template
from flask import Flask, request, render_template, jsonify
from flask_mail import Mail, Message
from flask import render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Configure Flask-Mail with your email settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Replace with your email provider's SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'jason.goliath.1992@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'fpcxrmsyhhyajbbd'  # Replace with your email password
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@gmail.com'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')  # Your HTML file

@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        name = request.form['name']
        email = request.form['email']
        message_body = request.form['message']


        # Construct email
        msg = Message("New Contact Form Submission",
                      sender=email,
                      recipients=['jason.goliath.1992@gmail.com'])  # Replace with recipient email

        msg.body = f"Name: {name}\nEmail: {email}\nMessage:\n{message_body}"
        
        mail.send(msg)

        return jsonify({'success': True, 'message': 'Email sent successfully!'})
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})


if __name__ == "__main__":
    app.run(debug=True)



