import os
from flask import Flask, render_template, request, send_file
import matchering as mg
import boto3
#Don't forget to preform AWS CONIGURE!!! 
#Don't UPLOAD SENSITIVE DATA OR AWS credentials 
# Replace with your own bucket name
bucket_name = 'YOUR BUCKET NAME'
# Initialize the S3 client
s3 = boto3.client('s3')
# Specify the file to upload and the S3 key (path/filename)
s3_key = 'Master.wav' #OR other path /Masters/Master.wav

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    target_file = request.files['target_file']
    reference_file = request.files['reference_file']

    # Process the files using Matchering
    results = [
        mg.pcm24("my_song_master_24bit.wav"),
    ]
    mg.process(
        target=target_file,
        reference=reference_file,
        results=results
    )

    # Provide download link for the processed file
    processed_file = 'my_song_master_24bit.wav'
    s3.upload_file('my_song_master_24bit.wav', bucket_name, s3_key)
    return send_file(processed_file, as_attachment=True)

# Upload the file

if __name__ == '__main__':
    app.run(debug=True)
