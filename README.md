# Phishing Awareness & Risk Simulation Dashboard

#### Overview

This project is a Flask-based cybersecurity awareness simulator designed to demonstrate how phishing attacks are delivered, how users commonly interact with them, and how those interactions can be analyzed to assess security risk.  
The application simulates a realistic email inbox, tracks user behavior when interacting with phishing content, assigns behavioral risk scores, and provides educational feedback to improve user awareness.

Phishing remains one of the most effective attack vectors in real-world breaches, largely due to human factors rather than technical vulnerabilities.  
Organizations often rely on phishing simulations and awareness training to reduce risk by identifying unsafe behavior patterns and educating users.
This project was built to:
- Understand how phishing simulations are structured
- Model how user interactions translate into security risk
- Practice clean application architecture for security-oriented systems
- Create a portfolio project aligned with cybersecurity, not just web development

#### Application Architecture
The project is intentionally structured to reflect real-world security tooling design:
- **Routes**  
  Observe user actions and orchestrate application flow
- **Email data layer**  
  Email templates and phishing metadata are separated from routes
- **Risk engine**  
  Pure logic module that evaluates events and assigns risk scores
- **Session-based user profile**  
  Models cumulative user behavior across the session without real authentication
- **Templates (Jinja2)**  
  Handle presentation only, using template inheritance for consistency
This separation ensures the system is explainable, testable, and aligned with security engineering best practices.

#### Security Awareness Report
After interacting with a phishing email, users are shown a security awareness report that explains:
- What actions they performed
- Why the email was suspicious (red flags)
- A concrete tip to improve phishing awareness
This mirrors how enterprise phishing training platforms provide feedback rather than punishment.

#### Tech Stack
- Python
- Flask
- Jinja2
- HTML
- Bootstrap (for UI styling)

#### Future Improvements
- Persistent storage for event logs (database)
- Analyst / SOC dashboard with authentication
- Expanded phishing templates with difficulty levels
- More granular risk scoring heuristics
- Aggregated metrics for awareness effectiveness

#### How to Run the Project Locally

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <project-folder>
2. **Create a virtual Environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate
4. **Install Flask**
   ```bash
   pip install flask
6. **Run the program**
   ```bash
   python app.py
