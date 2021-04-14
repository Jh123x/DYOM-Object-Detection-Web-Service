from flask import Flask, render_template

# Create the application
app = Flask(__name__)


# Create the routes
@app.route('/')
def welcome_page():
    """The welcome page for the website"""
    return render_template('index.html')


@app.route('/upload')
def upload_img_page():
    """The page for the user to upload their images"""
    pass


@app.route('/result', methods=['POST'])
def results():
    """The page where the results will be shown"""
    pass


# If the file is run as main
if __name__ == "__main__":

    # Constants
    host = 'localhost'
    port = 80

    # Run the application with the constants
    app.run(host, port, debug=False)
