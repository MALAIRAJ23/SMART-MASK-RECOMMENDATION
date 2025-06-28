from flask import Flask, render_template, request, jsonify
from model import train_model  # Importing the model training logic

app = Flask(__name__)
trained_hypothesis = []

# Train the model when the app starts
def initialize_model():
    global trained_hypothesis
    trained_hypothesis = train_model()
    print(f"Trained hypothesis: {trained_hypothesis}")

@app.route('/')
def index():
    initialize_model()  # Train the model when the app loads
    return render_template('index.html')

@app.route('/get_hypothesis')
def get_hypothesis():
    """API endpoint to get the trained hypothesis"""
    global trained_hypothesis
    if not trained_hypothesis:
        initialize_model()
    return jsonify({'hypothesis': trained_hypothesis})

@app.route('/recommend', methods=['POST'])
def recommend():
    global trained_hypothesis
    if not trained_hypothesis:
        initialize_model()
    
    input_data = [
        request.form['pollution'],
        request.form['location'],
        request.form['weather'],
        request.form['health'],
        request.form['crowd']
    ]

    # Predict based on trained hypothesis
    is_match = all(h == '?' or h == a for h, a in zip(trained_hypothesis, input_data))
    result = "N95" if is_match else "Cloth or Surgical"
    
    return jsonify({
        'recommendation': result,
        'is_n95': is_match,
        'input_data': input_data,
        'hypothesis': trained_hypothesis
    })

if __name__ == '__main__':
    initialize_model()  # Initialize model on startup
    app.run(debug=True, host='0.0.0.0', port=5000)
