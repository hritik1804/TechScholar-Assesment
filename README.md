# This Flask application requires the following:
------------------------------------------------


*Python 3*: Ensure you have Python 3 installed on your system. You can download it from https://www.python.org/downloads/.

*Flask*: Flask is a lightweight web framework for Python. Install it using pip:

````pip install Flask````

*Werkzeug*: Flask uses Werkzeug internally. It's usually installed with Flask, but you can verify it with:

````pip show Werkzeug````

*cryptography*: This library provides cryptographic functions for encryption and decryption. Install it using pip:

````pip install cryptography````

*secrets* (Optional): This module from the Python standard library is used for secure key generation (recommended). Ensure you have Python 3.6 or later.




## Running the Application
-------------------------


*Save the code*: Create a Python file (e.g., upload_server.py) and paste the provided code into it.

*Create the directory*: Make sure the directory uploads/encrypted_files exists within your project directory. The application will create it if necessary, but it's cleaner to have it beforehand. You can create it manually or run the script once to let it create it automatically.

*Run the script*: Open a terminal or command prompt, navigate to the directory where you saved the Python file, and run the following command:

````python upload_server.py````


*Test the upload*: Using a tool like Postman or a browser extension for sending POST requests, make a POST request to http://127.0.0.1:5000/uploads with a file attached in the file field. The server should respond with a JSON message indicating successful upload and the public path (relative URL) to access the uploaded file (although the file is actually encrypted).
