from flask import Flask, render_template, request, redirect
from flask.helpers import flash, send_file, send_from_directory
from werkzeug.utils import secure_filename
from functions.object_detect import draw_bounding_boxes
import os


# Constants
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
UPLOAD_FOLDER = './uploads'


# Create the application
app = Flask(__name__)
app.secret_key = os.urandom(64).hex()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Create the routes
@app.route('/')
def welcome_page():
    """The welcome page for the website"""
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_img_page():
    """The page for the user to upload their images"""

    # Redirect to mainpage if the method is get
    if request.method == 'GET':
        return redirect('/')

    # Check if any file is uploaded
    if 'file' not in request.files:
        flash('File uploaded is invalid','Error')
        return redirect('/')

    # Get the file
    file = request.files['file']

    # Check if the files uploaded is not empty
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    # Check if the extension of the file is correct
    for ext in ALLOWED_EXTENSIONS:
        if ext in file.filename:
            curr_ext = ext
            break
    else:
        flash(f"File extension is not allowed. We only allow {', '.join(ALLOWED_EXTENSIONS)}.")
        return redirect('/')

    # Save the file to a path
    print(f'Valid file received: {file}')

    # Get the filepath
    filename = secure_filename(f'temp.{curr_ext}')
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Save the file at path
    file.save(filepath)

    # Pass the file_path to the object detection code and let the user download the file
    response_filepath = draw_bounding_boxes(filepath, curr_ext)
    return send_file(response_filepath)


# If the file is run as main
if __name__ == "__main__":

    # Constants
    host = 'localhost'
    port = 80

    # Run the application with the constants
    app.run(host, port, debug=False)
