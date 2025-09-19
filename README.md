# Emotional Friend 🎭

**AI-Powered Mood Recognition & Emotional Support Platform**

An intelligent web application that uses computer vision and machine learning to detect user emotions in real-time, then provides personalized emotional support and guidance through an intuitive interface.

![HTML](https://img.shields.io/badge/HTML-75.7%25-orange)
![Python](https://img.shields.io/badge/Python-24.3%25-blue)
![Stars](https://img.shields.io/github/stars/yash-goyal-0910/Emotional_Friend)
![Forks](https://img.shields.io/github/forks/yash-goyal-0910/Emotional_Friend)

## 🌟 Features

- **Real-time Emotion Detection**: Uses Google Teachable Machine for accurate mood recognition
- **AI-powered Analysis**: Computer vision model trained for emotion classification
- **Personalized Support**: Mood-specific guidance and resources
- **Web-based Interface**: Easy-to-use browser application
- **Future AI Integration**: Planned Gemini API for conversational emotional support
- **Cross-platform Compatibility**: Works on any modern web browser

## 🛠️ Technology Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python
- **AI/ML**: Google Teachable Machine (Computer Vision Model)
- **Model Type**: Image Classification for emotion detection
- **Future**: Google Gemini API integration

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Modern web browser with camera access
- Internet connection for model loading

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yash-goyal-0910/Emotional_Friend.git
   cd Emotional_Friend
   ```

2. **Install dependencies** (if any)
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```
   *Or simply open `index.html` in your browser if it's a static web app*

4. **Open in browser**
   - Navigate to `localhost:5000` (if using Python server)
   - Allow camera permissions when prompted

## 🤖 Model Training & Development

### Google Teachable Machine Integration

This project utilizes **Google Teachable Machine** for emotion recognition:

- **Training Dataset**: Custom emotion dataset with multiple images per emotion class
- **Model Type**: Image Classification Model
- **Emotions Detected**: Happy, Sad, Angry, Neutral, Surprised, Fear, Disgust
- **Export Format**: TensorFlow.js for seamless web deployment
- **Real-time Processing**: Live webcam feed analysis

### Model Architecture
- **Base Model**: MobileNet (via Teachable Machine)
- **Input**: Real-time webcam feed (224x224 pixels)
- **Output**: Emotion classification with confidence scores
- **Deployment**: Browser-based TensorFlow.js

## 📖 How to Use

1. **Launch Application**: Open the web interface in your browser
2. **Camera Setup**: Allow camera access when prompted
3. **Position Face**: Center your face in the camera view
4. **Emotion Detection**: The AI model analyzes your facial expression
5. **View Results**: See detected emotion with confidence score
6. **Get Support**: Receive personalized emotional guidance based on your mood
7. **Future Feature**: Chat with AI assistant (Gemini integration coming soon)

## 📁 Project Structure

```
Emotional_Friend/
├── index.html              # Main web interface
├── static/
│   ├── css/               # Stylesheets
│   ├── js/                # JavaScript files
│   └── models/            # Teachable Machine model files
├── templates/             # HTML templates (if using Flask)
├── app.py                # Python server (if applicable)
├── model_handler.py      # ML model integration
├── requirements.txt      # Python dependencies
└── README.md            # Project documentation
```

## 🔮 Roadmap & Future Enhancements

- **🎯 Priority**: **Gemini API Integration** for mood-aware conversational support
- **📊 Analytics**: Emotion history tracking and mood pattern analysis
- **🎨 UI/UX**: Enhanced user interface and mobile responsiveness
- **🌍 Accessibility**: Multi-language support and accessibility features
- **📱 Mobile App**: Native mobile application development
- **🔒 Privacy**: Local processing options for sensitive applications

## 🤝 Contributing

We welcome contributions! Here are areas where help is especially needed:

- **🚀 High Priority**: Gemini API integration for conversational support
- **🎯 Model Improvements**: Enhance emotion detection accuracy
- **🎨 UI/UX**: Design improvements and mobile responsiveness
- **🔧 Features**: Additional emotion categories and support resources
- **📚 Documentation**: Code comments and user guides

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Don't hesitate to send a PR if you want to help implement the Gemini API or any other improvements!

## ⚡ Performance & Specifications

- **Model Size**: Optimized for web deployment
- **Inference Time**: Real-time processing (< 100ms per prediction)
- **Supported Browsers**: Chrome, Firefox, Safari, Edge
- **Camera Requirements**: 480p minimum resolution recommended
- **Platform**: Cross-platform web application

## 🎯 Use Cases

- **Mental Health**: Mood tracking and emotional awareness
- **Education**: Emotion recognition learning tool
- **Healthcare**: Patient mood assessment support
- **Research**: Emotion analysis for behavioral studies
- **Personal**: Daily mood monitoring and self-care

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- **Google Teachable Machine** for making machine learning accessible
- **TensorFlow.js** for seamless web-based AI deployment
- **Open Source Community** for inspiration and best practices
- **Contributors** who help improve this project

## 📧 Contact

**Yash Goyal** - [@yash-goyal-0910](https://github.com/yash-goyal-0910)
- Email: yashgoyal09102005@gmail.com
- GitHub: [https://github.com/yash-goyal-0910](https://github.com/yash-goyal-0910)

---

⭐ **Star this repository if you found it helpful!**

🔗 **Project Link**: [https://github.com/yash-goyal-0910/Emotional_Friend](https://github.com/yash-goyal-0910/Emotional_Friend)
