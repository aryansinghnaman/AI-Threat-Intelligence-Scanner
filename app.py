from flask import Flask, render_template, request
import pickle
import requests
import whois
import tldextract

app = Flask(__name__)

# Load ML model
model = pickle.load(open("model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

scan_history = []

# -----------------------------
# URL SECURITY ANALYSIS
# -----------------------------

def analyze_url(url):

    checks = {}

    if url.startswith("https"):
        checks["HTTPS"] = "Secure"
    else:
        checks["HTTPS"] = "Not Secure"

    if len(url) > 30:
        checks["URL Length"] = "Suspicious"
    else:
        checks["URL Length"] = "Normal"

    suspicious_words = [
        "login","verify","update","bank",
        "secure","account","billing",
        "confirm","password","payment"
    ]

    if any(word in url.lower() for word in suspicious_words):
        checks["Keyword Check"] = "Suspicious"
    else:
        checks["Keyword Check"] = "Clean"

    checks["Hyphen Pattern"] = "Suspicious" if url.count("-") >= 2 else "Normal"

    bad_domains = [".xyz",".ru",".top",".click",".info",".site"]

    if any(domain in url for domain in bad_domains):
        checks["Domain Reputation"] = "Suspicious"
    else:
        checks["Domain Reputation"] = "Normal"

    return checks


# -----------------------------
# DOMAIN INTELLIGENCE
# -----------------------------

def domain_intelligence(url):

    info = {}

    try:

        ext = tldextract.extract(url)
        domain = ext.domain + "." + ext.suffix

        w = whois.whois(domain)

        if w.creation_date:
            info["Domain Creation"] = str(w.creation_date)
        else:
            info["Domain Creation"] = "Unknown"

    except:

        info["Domain Creation"] = "Lookup Failed"

    return info


# -----------------------------
# EXPLAINABLE AI
# -----------------------------

def explain_prediction(url):

    reasons = []

    if len(url) > 30:
        reasons.append("URL length unusually long")

    if "login" in url:
        reasons.append("Login keyword detected")

    if "verify" in url:
        reasons.append("Verification keyword detected")

    if "billing" in url:
        reasons.append("Billing keyword detected")

    if not url.startswith("https"):
        reasons.append("Website not using HTTPS")

    if not reasons:
        reasons.append("No suspicious patterns detected")

    return reasons


# -----------------------------
# THREAT INTELLIGENCE
# -----------------------------

def check_phishtank(url):

    try:

        api = "https://checkurl.phishtank.com/checkurl/"

        response = requests.post(api,data={"url":url})

        if "phish_id" in response.text:
            return "Listed in PhishTank database"
        else:
            return "Not found in phishing database"

    except:

        return "Threat database unavailable"


# -----------------------------
# HOME
# -----------------------------

@app.route("/")
def home():

    return render_template("index.html", history=scan_history)


# -----------------------------
# SCAN URL
# -----------------------------

@app.route("/predict_url", methods=["POST"])
def predict_url():

    url = request.form["url"]

    vector = vectorizer.transform([url])

    result = model.predict(vector)

    probability = model.predict_proba(vector)

    confidence = round(max(probability[0]) * 100,2)

    checks = analyze_url(url)

    reasons = explain_prediction(url)

    threat_result = check_phishtank(url)

    domain_info = domain_intelligence(url)

    suspicious_count = sum(
        1 for v in checks.values()
        if v == "Suspicious" or v == "Not Secure"
    )

    # Risk Score
    risk_score = suspicious_count * 20

    if result[0] == 1:
        risk_score += 40

    if risk_score > 100:
        risk_score = 100

    if risk_score >= 70:
        prediction = "PHISHING WEBSITE"
        color = "red"
        risk = "HIGH RISK"

    elif risk_score >= 40:
        prediction = "SUSPICIOUS WEBSITE"
        color = "orange"
        risk = "MEDIUM RISK"

    else:
        prediction = "SAFE WEBSITE"
        color = "green"
        risk = "LOW RISK"

    scan_history.insert(0,{
        "url":url,
        "result":prediction,
        "confidence":confidence
    })

    return render_template(
        "index.html",
        prediction_text=prediction,
        confidence=confidence,
        risk=risk,
        color=color,
        checks=checks,
        reasons=reasons,
        threat_result=threat_result,
        domain_info=domain_info,
        risk_score=risk_score,
        history=scan_history
    )


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


