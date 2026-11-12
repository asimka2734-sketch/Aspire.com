# Aspire College Taunsa Website & Student/Admin Portal

This project contains the official website and student/admin portal for **Aspire College Taunsa**, organized to run seamlessly on localhost.

## Quick Start (Run on Localhost)

### Option 1: Double-Click (Windows)
Double-click `start-server.bat` in this folder. It will start the server and immediately open the website in your default browser.

### Option 2: Using Python (Recommended)
Run the included python server:
```bash
python server.py
```
Or standard Python HTTP server:
```bash
python -m http.server 8000
```
Then visit:
- **Main Institutional Website:** [http://localhost:8000/](http://localhost:8000/)
- **Student & Admin Portal:** [http://localhost:8000/portal.html](http://localhost:8000/portal.html)

### Option 3: Using Node.js
```bash
node server.js
```
Then open [http://localhost:8000/](http://localhost:8000/).

---

## Project Structure
```
aspire_college_taunsa/
├── index.html            # Main Flagship Institutional Website
├── portal.html           # Student & Admin Management Portal
├── assets/
│   └── images/           # High-resolution local branding and campus images
│       ├── logo.png
│       ├── campus.png
│       ├── computer-lab.png
│       └── science-lab.png
├── server.py             # Python localhost development server
├── server.js             # Node.js localhost server
├── start-server.bat      # Windows one-click launcher
└── README.md             # Instructions
```
