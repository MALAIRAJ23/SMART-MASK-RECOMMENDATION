from flask import Flask, render_template, request, jsonify
import sys
import os
from http.server import BaseHTTPRequestHandler
import json

# Add the parent directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model import train_model

# Global variable to store the trained hypothesis
trained_hypothesis = []

def initialize_model():
    global trained_hypothesis
    try:
        trained_hypothesis = train_model()
        print(f"Trained hypothesis: {trained_hypothesis}")
    except Exception as e:
        print(f"Error training model: {e}")
        trained_hypothesis = ["High", "Outdoor", "Dry", "Asthma", "High"]

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            initialize_model()
            
            if self.path == '/get_hypothesis':
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                response = json.dumps({'hypothesis': trained_hypothesis})
                self.wfile.write(response.encode())
                return
            
            # Serve the main page
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            # Read and serve the HTML template
            template_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'templates', 'index.html')
            with open(template_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            self.wfile.write(html_content.encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({'error': str(e)})
            self.wfile.write(response.encode())
    
    def do_POST(self):
        try:
            initialize_model()
            
            if self.path == '/recommend':
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                
                # Parse form data
                form_data = {}
                for item in post_data.decode().split('&'):
                    if '=' in item:
                        key, value = item.split('=', 1)
                        form_data[key] = value.replace('+', ' ')
                
                input_data = [
                    form_data.get('pollution', ''),
                    form_data.get('location', ''),
                    form_data.get('weather', ''),
                    form_data.get('health', ''),
                    form_data.get('crowd', '')
                ]
                
                # Predict based on trained hypothesis
                is_match = all(h == '?' or h == a for h, a in zip(trained_hypothesis, input_data))
                result = "N95" if is_match else "Cloth or Surgical"
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                
                response = json.dumps({
                    'recommendation': result,
                    'is_n95': is_match,
                    'input_data': input_data,
                    'hypothesis': trained_hypothesis
                })
                self.wfile.write(response.encode())
                return
            
            self.send_response(404)
            self.end_headers()
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({'error': str(e)})
            self.wfile.write(response.encode())
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers() 