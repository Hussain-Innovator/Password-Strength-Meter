# Password Strength Meter

A simple and interactive **Streamlit web application** that evaluates the strength of user-entered passwords in real time.  
It checks key security criteria and provides instant feedback: **Weak**, **Medium**, or **Strong**.

Built to demonstrate practical string manipulation, conditional logic, scoring algorithms, and modern UI development with Streamlit.

## Features

- Real-time password strength evaluation as you type
- Checks password length (minimum recommended length)
- Detects presence of:
  - Uppercase letters (A–Z)
  - Lowercase letters (a–z)
  - Numbers (0–9)
  - Special characters (!@#$%^&*()_+-=[]{}|;:'",.<>?/~`)
- Calculates an overall strength score
- Clearly displays result: **Weak**, **Medium**, or **Strong**
- Clean, minimal, and user-friendly Streamlit interface

## How Strength Is Calculated

The app awards points based on the following criteria:

- Length ≥ 8 characters  
- Length ≥ 12 characters (bonus)  
- Contains uppercase letters  
- Contains lowercase letters  
- Contains numbers  
- Contains special characters  

Final strength levels:
- **Weak**: 0–3 points  
- **Medium**: 4–5 points  
- **Strong**: 6+ points  

## Technologies Used

- Python 3
- Streamlit – for the interactive web interface

## Installation

### Prerequisites
- Python 3.8+
- pip

### Steps

1. Clone the repository

   ```bash
   git clone https://github.com/Hussain-lnnovator/Password-Strength-Meter.git
   cd Password-Strength-Meter

2. Project Structure
Password-Strength-Meter/
├── app.py                # Main Streamlit application
├── requirements.txt      # Project dependencies
└── README.md

Author
Hussain
hussainsamdani5686@gmail.com