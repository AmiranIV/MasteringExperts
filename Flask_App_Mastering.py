from flask import Flask, render_template, request, send_file
import matchering as mg

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
    return send_file(processed_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
