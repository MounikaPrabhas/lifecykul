# from flask import Flask, render_template, request, session, redirect, url_for
# from otpGenerationValidation import generateOTP, sendOTPviaSMS, verifyOTP
#
# app = Flask(__name__)
# app.secret_key = 'your-secret-key'  # used for session encryption
#
# users = {
#
#     'Mounika': {'password': 'Mounika@2000'},
#     'Vahini': {'password': 'Vahini1234'},
#     '1': {'password': '1'}
# }
#
#
# @app.route('/haha')
# def home():
#     if 'username' in session:
#         # check for autentication in db
#         return redirect(url_for('like'))
#     return render_template('login')
#
#
# @app.route('/login', methods = ['POST', 'GET'])
#
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#
#         if username in users and users[username]['password'] == password:
#             return redirect(url_for('verify'))
#         else:
#             return 'Invalid username or password. Please try again.'
#
#     return render_template('login.html')
#
#
# @app.route('/verify', methods=["POST", 'GET'])
# def verify():
#     if request.method == 'POST':
#         mobile = '+91-' + request.form["mobile"]
#
#         print(mobile, type(mobile))
#
#         otp = generateOTP()
#
#         print(otp)
#
#         sendOTPviaSMS(otp, mobile)
#
#         session['current_otp'] = otp
#         return redirect(url_for('validate'))
#
#     return render_template('index.html')
#
#
# @app.route('/validate', methods=["POST", 'GET'])
# def validate():
#     if request.method == 'POST':
#
#         current_user_otp = session['current_otp']
#
#         user_otp = request.form['otp']
#
#         if int(current_user_otp) == int(user_otp):
#
#             return "<h3 text-align:center> Your OTP has been successfully verified! </h3>"
#         else:
#             return "<h3> Oops! OTP Verification Failure, OTP does not match. </h3>"
#
#     return render_template('otpVerifiaction.html')
#
#
# @app.route('/qrcode')
# def qrcode():
#     if 'username' not in session:
#         return redirect(url_for('home'))
#     return render_template('like.html')
# @app.route('/generate', methods=['POST', 'GET'])
# def generate():
#     # Get the link and number of times from the form data
#     link = request.form['link']
#     num_times = int(request.form['num_times'])
#
#     # Create a PDF file to save the QR codes
#     pdf_filename = "qrcodes.pdf"
#     images = []
#
#     # Generate the QR code for the link multiple times
#     for i in range(num_times):
#         # Generate the QR code
#         qr = qrr.QRCode(version=1, box_size=10, border=5)
#         qr.add_data(link)
#         qr.make(fit=True)
#
#         # Create an image from the QR code
#         img = qr.make_image(fill_color="black", back_color="white")
#
#         # Convert the image to PNG and save it in a BytesIO object
#         buffer = BytesIO()
#         img.save(buffer, format="PNG")
#         buffer.seek(0)
#
#         # Add the PNG image to the list of images for the PDF file
#         images.append(Image.open(buffer))
#
#     # Save all the images as a single PDF file
#     if images:
#         images[0].save(pdf_filename, save_all=True, append_images=images[1:])
#
#     # Serve the PDF file for download
#     return send_file(pdf_filename, as_attachment=True)
#
#
#
# @app.route('/logout')
# def logout():
#     session.pop('username', None)
#     return redirect(url_for('home'))
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request, session, redirect, url_for, send_file
# from otpvalid import generateOTP, sendOTPviaSMS, verifyOTP
# from io import BytesIO
# import qrcode as qrr
#
# app = Flask(__name__)
# app.secret_key = 'your-secret-key'  # used for session encryption
#
# users = {
#     'Mounika': {'password': 'Mounika@2000'},
#     'Vahini': {'password': 'Vahini1234'},
#     '1': {'password': '1'}
# }
#
#
# @app.route('/')
# def home():
#     if 'username' in session:
#         # check for authentication in db
#         return redirect(url_for('like'))
#     return render_template('login.html')
#
#
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#
#         if username in users and users[username]['password'] == password:
#             return redirect(url_for('verify'))
#         else:
#             return 'Invalid username or password. Please try again.'
#
#     return render_template('otplogin.html')
#
#
# @app.route('/verify', methods=["POST", 'GET'])
# def verify():
#     if request.method == 'POST':
#         mobile = '+91-' + request.form["mobile"]
#
#         print(mobile, type(mobile))
#
#         otp = generateOTP()
#
#         print(otp)
#
#         sendOTPviaSMS(otp, mobile)
#
#         session['current_otp'] = otp
#         return redirect(url_for('validate'))
#
#     return render_template('otp index.html')
#
#
# @app.route('/validate', methods=["POST", 'GET'])
# def validate():
#     if request.method == 'POST':
#
#         current_user_otp = session['current_otp']
#
#         user_otp = request.form['otp']
#
#         if int(current_user_otp) == int(user_otp):
#
#             return redirect(url_for('qrcode'))
#         else:
#             return "<h3> Oops! OTP Verification Failure, OTP does not match. </h3>"
#
#     return render_template('otpverification.html')
#
#
# @app.route('/qrcode')
# def index():
#     return render_template('index.html')
#
# @app.route('/generate', methods=['POST', 'GET'])
# def generate():
#     # Get the link and number of times from the form data
#     link = request.form['link']
#     num_times = int(request.form['num_times'])
#
#     # Create a PDF file to save the QR codes
#     pdf_filename = "qrcodes.pdf"
#     images = []
#
#     # Generate the QR code for the link multiple times
#     for i in range(num_times):
#         # Generate the QR code
#         qr = qrr.QRCode(version=1, box_size=10, border=5)
#         qr.add_data(link)
#         qr.make(fit=True)
#
#         # Create an image from the QR code
#         img = qr.make_image(fill_color="black", back_color="white")
#
#         # Convert the image to PNG and save it in a BytesIO object
#         buffer = BytesIO()
#         img.save(buffer, format="PNG")
#         buffer.seek(0)
#
#         # Add the PNG image to the list of images for the PDF file
#         images.append(Image.open(buffer))
#
#     # Save all the images as a single PDF file
#     if images:
#         images[0].save(pdf_filename, save_all=True, append_images=images[1:])
#
#     # Serve the PDF file for download
#     return send_file(pdf_filename, as_attachment=True)
#
#
#  @app.route('/logout')
#  def logout():
#      session.pop('username', None)
#      return redirect(url_for('home'))
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

from PIL import Image
from flask import Flask, render_template, request, session, redirect, url_for, send_file
from otpGenerationValidation import generateOTP, sendOTPviaSMS, verifyOTP
from io import BytesIO
import qrcode as qrr

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # used for session encryption

users = {
    'Mounika': {'password': 'Mounika@2000'},
    'Vahini': {'password': 'Vahini1234'},
    '1': {'password': '1'}
}


@app.route('/')
def home():
    if 'username' in session:
        # check for authentication in db
        return redirect(url_for('like'))
    return render_template('login.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username]['password'] == password:
            return redirect(url_for('verify'))
        else:
            return 'Invalid username or password. Please try again.'

    return render_template('login.html')


@app.route('/verify', methods=["POST", 'GET'])
def verify():
    if request.method == 'POST':
        mobile = '+91-' + request.form["mobile"]

        print(mobile, type(mobile))

        otp = generateOTP()

        print(otp)

        sendOTPviaSMS(otp, mobile)

        session['current_otp'] = otp
        return redirect(url_for('validate'))

    return render_template('index.html')


@app.route('/validate', methods=["POST", 'GET'])
def validate():
    if request.method == 'POST':

        current_user_otp = session['current_otp']

        user_otp = request.form['otp']

        if int(current_user_otp) == int(user_otp):

            return redirect(url_for('qrcode'))
        else:
            return "<h3> Oops! OTP Verification Failure, OTP does not match. </h3>"

    return render_template('otpVerifiaction.html')


@app.route('/qrcode')
def qrcode():
     return render_template('qrcode.html')

@app.route('/generate', methods=['POST', 'GET'])
def generate():
    # Get the link and number of times from the form data
    link = request.form['link']
    num_times = int(request.form['num_times'])

    # Create a PDF file to save the QR codes
    pdf_filename = "qrcodes.pdf"
    images = []

    # Generate the QR code for the link multiple times
    for i in range(num_times):
        # Generate the QR code
        qr = qrr.QRCode(version=1, box_size=10, border=5)
        qr.add_data(link)
        qr.make(fit=True)

        # Create an image from the QR code
        img = qr.make_image(fill_color="black", back_color="white")

        # Convert the image to PNG and save it in a BytesIO object
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        # Add the PNG image to the list of images for the PDF file
        images.append(Image.open(buffer))

    # Save all the images as a single PDF file
    if images:
        images[0].save(pdf_filename, save_all=True, append_images=images[1:])

    # Serve the PDF file for download
    return send_file(pdf_filename, as_attachment=True)
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)