# 🛡️ Smart Mask Recommendation System

A modern, AI-powered web application that provides personalized face mask recommendations based on environmental conditions and health factors. Built with Flask, machine learning, and a beautiful responsive UI.

## ✨ Features

- **🤖 AI-Powered Recommendations**: Uses the Find-S machine learning algorithm for intelligent mask suggestions
- **🎨 Modern UI/UX**: Beautiful, responsive design with smooth animations and intuitive interface
- **📱 Mobile-Friendly**: Optimized for all device sizes
- **⚡ Real-time Analysis**: Instant recommendations based on current conditions
- **🏥 Health-Focused**: Considers health conditions like asthma and allergies
- **🌍 Environment-Aware**: Analyzes pollution levels, weather, and location factors

## 🧠 How It Works

The system uses the **Find-S Algorithm**, a concept learning algorithm that:

1. **Learns from Training Data**: Analyzes 50+ real-world scenarios with mask recommendations
2. **Identifies Patterns**: Finds the most specific hypothesis for when N95 masks are needed
3. **Makes Predictions**: Compares user input against learned patterns
4. **Provides Recommendations**: Suggests N95, Surgical, or Cloth masks based on risk level

### Input Factors Analyzed:
- 🌫️ **Air Pollution Level** (Low/Medium/High)
- 🏠 **Location Type** (Indoor/Outdoor)
- 🌤️ **Weather Condition** (Dry/Humid/Rainy)
- ❤️ **Health Condition** (None/Asthma/Allergy)
- 👥 **Crowd Density** (Low/Medium/High)

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd smart-mask-recommendation
```

### Step 2: Install Dependencies
```bash
pip install flask
```

### Step 3: Run the Application
```bash
python app_flask_mask.py
```

### Step 4: Access the Application
Open your web browser and navigate to:
```
http://localhost:5000
```

## 📁 Project Structure

```
smart-mask-recommendation/
├── app_flask_mask.py      # Main Flask application
├── model.py              # Machine learning model (Find-S algorithm)
├── templates/
│   └── index.html        # Modern web interface
└── README.md             # Project documentation
```

## 🎯 Usage

1. **Open the Application**: Navigate to the web interface
2. **Fill the Form**: Select your current conditions from the dropdown menus
3. **Get Recommendation**: Click "Get Recommendation" to receive your personalized mask suggestion
4. **View Results**: See detailed explanations and mask type information

## 🔬 Technical Details

### Machine Learning Algorithm
- **Algorithm**: Find-S (Find-Specific) Algorithm
- **Type**: Concept Learning
- **Training Data**: 50+ comprehensive scenarios
- **Output**: Binary classification (N95 vs. Other masks)

### Web Technologies
- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Custom CSS with gradients and animations
- **Icons**: Font Awesome 6.0
- **Fonts**: Inter (Google Fonts)

### API Endpoints
- `GET /` - Main application page
- `GET /get_hypothesis` - Returns trained model hypothesis
- `POST /recommend` - Processes mask recommendations

## 🎨 UI/UX Features

- **Gradient Backgrounds**: Beautiful purple-blue gradients
- **Glass Morphism**: Modern glass-like card design
- **Smooth Animations**: Fade-in effects and hover animations
- **Responsive Design**: Works perfectly on all screen sizes
- **Interactive Elements**: Hover effects and visual feedback
- **Loading States**: Animated spinner during processing
- **Color-coded Results**: Different colors for different mask types

## 🧪 Testing the Model

You can test the machine learning model independently:

```bash
python model.py
```

This will:
- Train the model with the provided data
- Display the learned hypothesis
- Run test predictions on sample inputs

## 📊 Training Data

The system is trained on comprehensive data including:
- **CDC Guidelines** for mask usage
- **WHO Recommendations** for different environments
- **Medical Research** on respiratory protection
- **Real-world Scenarios** and conditions

## 🔧 Customization

### Adding New Training Data
Edit the `get_training_data()` function in `model.py` to add more scenarios.

### Modifying the UI
The interface is built with modern CSS and can be easily customized by editing the styles in `templates/index.html`.

### Extending the Algorithm
The Find-S algorithm can be extended or replaced with other machine learning approaches in `model.py`.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## 🆘 Support

If you encounter any issues or have questions:
1. Check the console for error messages
2. Ensure all dependencies are installed
3. Verify Python version compatibility
4. Check that the Flask server is running

## 🔮 Future Enhancements

- [ ] Integration with real-time air quality APIs
- [ ] Weather API integration
- [ ] User accounts and recommendation history
- [ ] Mobile app version
- [ ] More sophisticated ML algorithms
- [ ] Multi-language support

---

**Built with ❤️ for public health and safety** "# smart-mask-recommendation" 
"# SMART-MASK-RECOMMENDATION" 
