from flask import Flask, render_template, request, jsonify
from model import train_model  # Importing the model training logic
import os

app = Flask(__name__)
trained_hypothesis = []

# Train the model when the app starts
def initialize_model():
    global trained_hypothesis
    try:
        trained_hypothesis = train_model()
        print(f"Trained hypothesis: {trained_hypothesis}")
    except Exception as e:
        print(f"Error training model: {e}")
        # Fallback hypothesis
        trained_hypothesis = ["High", "Outdoor", "Dry", "Asthma", "High"]

@app.route('/')
def index():
    try:
        initialize_model()  # Train the model when the app loads
        return render_template('index.html')
    except Exception as e:
        return f"Error loading page: {str(e)}", 500

@app.route('/get_hypothesis')
def get_hypothesis():
    """API endpoint to get the trained hypothesis"""
    global trained_hypothesis
    try:
        if not trained_hypothesis:
            initialize_model()
        return jsonify({'hypothesis': trained_hypothesis})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/recommend', methods=['POST'])
def recommend():
    global trained_hypothesis
    try:
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
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    initialize_model()  # Initialize model on startup
    # Use environment variables for port and host
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
