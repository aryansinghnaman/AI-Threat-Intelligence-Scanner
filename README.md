# AI Threat Intelligence Scanner

## Overview

AI Threat Intelligence Scanner is an AI-powered cybersecurity platform designed to detect phishing and malicious websites using machine learning, URL security analysis, and threat intelligence techniques.

The system analyzes website URLs using multiple detection layers such as HTTPS verification, suspicious keyword analysis, URL structure inspection, and machine learning-based risk prediction to generate a detailed security report with confidence scores and explainable AI insights.

This project was developed to improve cybersecurity awareness and provide automated phishing website detection for educational and research purposes.

---

# Features

* AI-powered phishing website detection
* Machine Learning based risk prediction
* URL security analysis
* HTTPS verification
* Suspicious keyword detection
* Threat intelligence scanning
* Explainable AI security reports
* Confidence score generation
* Risk level classification
* Cybersecurity dashboard UI
* Scan history tracking

---

# Example Detection Result

## Scan Result: PHISHING WEBSITE

| Parameter           | Result                     |
| ------------------- | -------------------------- |
| Confidence Score    | 91%                        |
| Risk Level          | HIGH                       |
| HTTPS Status        | Not Secure                 |
| URL Length          | Suspicious                 |
| Threat Intelligence | Malicious Indicators Found |

### AI Security Explanation

> This website was classified as HIGH RISK because it contains suspicious phishing-related keywords, lacks HTTPS encryption, and uses an unusually long URL structure commonly associated with fraudulent websites.

---

# Problem Statement

Phishing websites are designed to steal sensitive information such as passwords, banking credentials, and personal data. Many users cannot easily identify malicious websites manually.

This project aims to provide an automated AI-driven solution that detects potentially dangerous websites using machine learning and cybersecurity analysis techniques.

---

# Solution

The platform analyzes URLs using multiple security layers including:

* Machine Learning prediction
* URL feature extraction
* HTTPS security verification
* Suspicious keyword analysis
* URL structure inspection
* Threat intelligence checks

The system then generates a detailed security report explaining the detected risks and classification reasons.

---

# Detection Parameters

The scanner evaluates websites using several security indicators:

* HTTPS verification
* URL length analysis
* Suspicious keyword detection
* Special character analysis
* Domain structure inspection
* Phishing pattern recognition
* Machine learning risk prediction
* Threat intelligence analysis

---

# Technology Stack

## Backend

* Python
* Flask

## Machine Learning

* Scikit-learn
* Random Forest Classifier

## Frontend

* HTML
* CSS

## Security Analysis

* URL Feature Extraction
* HTTPS Verification
* Keyword Detection
* Threat Intelligence Checks

---

# System Architecture

```text
User Interface
      ↓
Flask Backend
      ↓
URL Feature Extraction
      ↓
Machine Learning Model
      ↓
Threat Intelligence Analysis
      ↓
Security Report Generation
```

---

# Project Structure

```bash
AI-Threat-Intelligence-Scanner/
│
├── app.py
├── dataset.csv
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── uploads/
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/aryansinghnaman/AI-Threat-Intelligence-Scanner.git
```

## Navigate to Project Directory

```bash
cd AI-Threat-Intelligence-Scanner
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python app.py
```

## Open in Browser

```text
http://127.0.0.1:5000
```

---

# Future Improvements

* VirusTotal API integration
* Real-time threat intelligence feeds
* Browser extension for automatic phishing detection
* Larger phishing datasets for improved accuracy
* Deep learning based URL analysis
* Real-time domain reputation analysis
* WHOIS and SSL certificate analysis
* Dark web threat intelligence integration

---

# Use Cases

* Phishing website detection
* Cybersecurity awareness
* Educational cybersecurity demonstrations
* Threat intelligence research
* Security analysis projects
* Hackathon cybersecurity projects

---

# Screenshots

Add screenshots of:

* Dashboard UI
* URL scan result
* Risk analysis report
* AI explanation section

---

# GitHub Topics

```text
cybersecurity
machine-learning
phishing-detection
threat-intelligence
python
flask
scikit-learn
ai
fraud-detection
url-analysis
```

---

# Author

## Aryan Singh

Developed as an AI-powered cybersecurity and machine learning project focused on phishing website detection and threat intelligence analysis.

GitHub:
https://github.com/aryansinghnaman

---

# License

This project is intended for educational and research purposes only.
ct phishing attacks and malicious URLs.
