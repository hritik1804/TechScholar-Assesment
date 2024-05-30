from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from cryptography.fernet import Fernet
import os
import secrets  # Recommended for secure key generation
import base64

app = Flask(__name__)


key = secrets.token_bytes(32)  # Generate 32 bytes of random data

encoded_key = base64.urlsafe_b64encode(key).decode()

# Use the encoded key with Fernet
fernet = Fernet(encoded_key.encode())

# Secure directory for storing encrypted files (outside public path)
ENCRYPTED_DIR = 'uploads/encrypted_files'  # Create a subfolder for encrypted files


@app.route('/uploads', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # Get the file object from the request
        file = request.files['file']

        # Validate filename (optional, add additional checks as needed)
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        # Secure filename (prevent path traversal attacks)
        filename = secure_filename(file.filename)

        # Generate a unique identifier for the encrypted file
        import uuid
        encrypted_filename = f'{uuid.uuid4()}.{filename.split(".")[1]}'

        try:
            # Read file content
            file_content = file.read()

            # Encrypt the file content
            encrypted_content = fernet.encrypt(file_content)

            # Create the secure directory (uploads/encrypted_files) if it doesn't exist
            os.makedirs(ENCRYPTED_DIR, exist_ok=True)  # Handle existing directory cases

            # Save the encrypted file
            with open(os.path.join(ENCRYPTED_DIR, encrypted_filename), 'wb') as f:
                f.write(encrypted_content)

            # Construct a public path for reference (replace with your actual URL structure)
            # Avoid using file ID or direct information leakage
            public_path = f'/static/{encrypted_filename}'  # Use the encrypted filename

            return jsonify({'message': 'File uploaded successfully!', 'public_path': public_path}), 201
        except Exception as e:
            print(f'Error uploading file: {e}')
            return jsonify({'error': 'An error occurred during upload'}), 500

    return jsonify({'error': 'Method not allowed'}), 405

if __name__ == '__main__':
    app.run(debug=True)