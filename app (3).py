from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials, storage
from datetime import timedelta


# Configurar Firebase
cred = credentials.Certificate('esp32-fb6da-firebase-adminsdk-ko1ku-2923577eaa.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'esp32-fb6da.appspot.com'
})

app = Flask(__name__)

@app.route('/interior', methods=['GET'])
def list_images():
    bucket = storage.bucket()
    interior = []
    blobs = bucket.list_blobs(prefix='Interior/')
    for blob in blobs:
        interior.append({
            'name': blob.name,
            'url': blob.generate_signed_url(timedelta(seconds=604800))
        })
    return jsonify(interior)
    
@app.route('/exterior', methods=['GET'])
def list_images():
    bucket = storage.bucket()
    exterior = []
    blobs = bucket.list_blobs(prefix='Exterior/')
    for blob in blobs:
        exterior.append({
            'name': blob.name,
            'url': blob.generate_signed_url(timedelta(seconds=604800))
        })
    return jsonify(exterior)
    


if __name__ == '__main__':
    app.run(debug=True)