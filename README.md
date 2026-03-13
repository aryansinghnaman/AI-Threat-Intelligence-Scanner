<<<<<<< HEAD
# AI Threat Intelligence Scanner

AI Threat Intelligence Scanner is a machine learning based cybersecurity tool that detects phishing or malicious websites by analyzing URLs. The system combines machine learning, URL security analysis, and threat intelligence techniques to generate a detailed security report.

Problem  
Phishing websites are designed to steal sensitive information such as passwords, banking details, and personal data. Many users cannot easily identify malicious websites. This project aims to detect phishing websites automatically using machine learning and security analysis.

Solution  
The system analyzes a website URL using multiple security layers including machine learning prediction, URL structure analysis, suspicious keyword detection, and threat intelligence checks. It generates a security report explaining the risk level and possible reasons for classification.

Features
- Machine learning phishing detection
- URL security analysis
- Explainable AI predictions
- Threat intelligence scanning
- Scan history dashboard
- Cybersecurity dashboard UI

Example Output
Result: PHISHING WEBSITE  
Confidence: 91%  
Risk Level: HIGH  

Reasons
- URL length unusually long  
- Suspicious keyword detected  
- Website not using HTTPS  

Technology Stack

Backend
Python  
Flask  

Machine Learning
Scikit-learn  
Random Forest Classifier  

Frontend
HTML  
CSS  

Security Analysis
URL feature analysis  
Keyword detection  
HTTPS verification  
Threat intelligence checks  

System Architecture

User Interface  
↓  
Flask Backend  
↓  
URL Feature Extraction  
↓  
Machine Learning Model  
↓  
Threat Intelligence Check  
↓  
Security Report  

Project Structure

fraud_website_detector
│
├── app.py
├── dataset.csv
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
│
├── templates
│     └── index.html
│
├── uploads

Installation

Clone the repository

git clone <repository-url>

Install dependencies

pip install -r requirements.txt

Run the application

python app.py

Open in browser

http://127.0.0.1:5000

Future Improvements

- Integration with VirusTotal API  
- Real-time threat intelligence scanning  
- Browser extension for automatic website detection  
- Training with larger phishing datasets  

Use Cases

- Detect phishing websites  
- Improve cybersecurity awareness  
- Educational cybersecurity demonstrations  
- Hackathon cybersecurity project  

Author

=======
# AI Threat Intelligence Scanner

AI Threat Intelligence Scanner is a machine learning based cybersecurity tool that detects phishing or malicious websites by analyzing URLs. The system combines machine learning, URL security analysis, and threat intelligence techniques to generate a detailed security report.

Problem  
Phishing websites are designed to steal sensitive information such as passwords, banking details, and personal data. Many users cannot easily identify malicious websites. This project aims to detect phishing websites automatically using machine learning and security analysis.

Solution  
The system analyzes a website URL using multiple security layers including machine learning prediction, URL structure analysis, suspicious keyword detection, and threat intelligence checks. It generates a security report explaining the risk level and possible reasons for classification.

Features
- Machine learning phishing detection
- URL security analysis
- Explainable AI predictions
- Threat intelligence scanning
- Scan history dashboard
- Cybersecurity dashboard UI

Example Output
Result: PHISHING WEBSITE  
Confidence: 91%  
Risk Level: HIGH  

Reasons
- URL length unusually long  
- Suspicious keyword detected  
- Website not using HTTPS  

Technology Stack

Backend
Python  
Flask  

Machine Learning
Scikit-learn  
Random Forest Classifier  

Frontend
HTML  
CSS  

Security Analysis
URL feature analysis  
Keyword detection  
HTTPS verification  
Threat intelligence checks  

System Architecture

User Interface  
↓  
Flask Backend  
↓  
URL Feature Extraction  
↓  
Machine Learning Model  
↓  
Threat Intelligence Check  
↓  
Security Report  

Project Structure

fraud_website_detector
│
├── app.py
├── dataset.csv
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
│
├── templates
│     └── index.html
│
├── uploads

Installation

Clone the repository

git clone <repository-url>

Install dependencies

pip install -r requirements.txt

Run the application

python app.py

Open in browser

http://127.0.0.1:5000

Future Improvements

- Integration with VirusTotal API  
- Real-time threat intelligence scanning  
- Browser extension for automatic website detection  
- Training with larger phishing datasets  

Use Cases

- Detect phishing websites  
- Improve cybersecurity awareness  
- Educational cybersecurity demonstrations  
- Hackathon cybersecurity project  

Author

>>>>>>> 1e26db98da7558578a738fb043c92bf2966e0683
Developed as a machine learning cybersecurity project to detect phishing attacks and malicious URLs.