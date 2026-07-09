# AI Product Ops Research Agent

An automated AI-powered pipeline to search, scrape, and audit developer API indicators for **100 SaaS applications** across 10 distinct categories. Built with Python, Google Serper, and Gemini 2.5 Flash.

This project enables Product Operations teams to quickly audit partner ecosystems and determine API capabilities: **Authentication Protocols**, **Self-Serve Access Models**, **API Surfaces (REST/GraphQL)**, **Model Context Protocol (MCP) Support**, and **Buildability Blockers**.

---

## 🚀 Key Features

- 🔍 **Automated Documentation Search:** Programmatically queries Google Serper API to target official developer portals.
- 🌐 **Rich Web Crawler:** Downloads and parses web page DOMs utilizing `BeautifulSoup` to feed full-context documentation text (up to 25k characters) directly into the model.
- 🧠 **Structured Schema Extraction:** Enforces JSON schema structure on Gemini 2.5 Flash outputs to classify API rules and output evidence links without guessing.
- 📊 **Automated Metrics & Visualizations:** Computes categories distribution and outputs Matplotlib visualizations (auth, category, self-serve access).
- 🛡️ **Verification Audit Engine:** Evaluates a random sample of 20 applications (80 total checks) and outputs exact accuracy statistics (achieving **95.0% accuracy**) and mistake logs.
- 📋 **Dynamic HTML Compilation:** Incorporates a template engine that compiles metrics, mistake reviews, and a 10-record preview into a simple, professional, light-themed HTML report.

---

## 🛠️ Pipeline Workflow Architecture

```
  data/apps.csv (100 Apps)
           ↓
     src/main.py (Pipeline Orchestrator)
           ↓
     src/search_agent.py (Serper Search API)
           ↓
     src/research_agent.py (BeautifulSoup Web Scraper)
           ↓
     Google Gemini 2.5 Flash (Structured JSON Schema)
           ↓
     output/results.csv (Full Dataset)
           ↓
     ┌───────────────────────┴───────────────────────┐
     ↓                                               ↓
src/analyzer.py                              src/verifier.py
     ↓                                               ↓
output/summary.json                      output/verification_template.csv
report/assets/*.png (Plots)                          ↓
     ↓                                       (Manual Review)
     │                                               ↓
     │                                    src/calculate_accuracy.py
     │                                               ↓
     │                                   output/verification_summary.json
     │                                   output/errors.csv
     └───────────────────────┬───────────────────────┘
                             ↓
                 src/generate_report.py
                             ↓
                  report/index.html (HTML Report)
                  report/style.css (Clean Stylesheet)
```

---

## 📂 Project Directory Structure

```
.
├── data/
│   └── apps.csv                 # Target 100 SaaS applications and URLs
├── output/
│   ├── results.csv              # Researched dataset for 100 applications
│   ├── summary.json             # Aggregate metrics (total, self-serve, auth)
│   ├── errors.csv               # Log of mismatches found during quality check
│   ├── verification_template.csv# Sample sheet populated with manual audits
│   └── verification_summary.json# Sample verification statistics & accuracy
├── report/
│   ├── index.html               # Compiled HTML dashboard report
│   ├── style.css                # Minimal layout stylesheet (Inter font)
│   ├── auth.png                 # Chart: Authentication distribution
│   ├── category.png             # Chart: Category distribution
│   └── selfserve.png            # Chart: Self-serve vs Gated model distribution
├── src/
│   ├── main.py                  # Auditing loop orchestrator
│   ├── search_agent.py          # Queries Serper API for documentation URLs
│   ├── research_agent.py        # Web scraper & Gemini Flash crawler interface
│   ├── analyzer.py              # Compiles summary stats and plots charts
│   ├── verifier.py              # Selects 20 random apps for manual review
│   ├── calculate_accuracy.py    # Computes pipeline validation metrics
│   └── generate_report.py       # Automatically compiles the report/ HTML
└── requirements.txt             # Project Python dependencies
```

---

## ⚙️ Environment Setup & Configuration

### 1. Prerequisite Installations
Ensure you have **Python 3.10+** installed on your system.

### 2. Configure Virtual Environment
Create and activate a virtual environment to manage dependencies:
```powershell
# Create venv
python -m venv venv

# Activate on Windows (PowerShell)
venv\Scripts\Activate.ps1

# Activate on Linux/macOS
source venv/bin/activate
```

### 3. Install Dependencies
Install all required libraries:
```bash
pip install -r requirements.txt
```

### 4. Setup Credentials
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_google_gemini_api_key_here
SERPER_API_KEY=your_serper_search_api_key_here
```

---

## 🏃 How to Run (Reproduce the Pipeline)

### Step 1: Run Research Crawler
Executes searches, extracts page text, and runs the Gemini research loop:
```bash
python src/main.py
```
*Outputs: `output/results.csv`*

### Step 2: Generate Statistics & Visualizations
Aggregates categories and exports plots:
```bash
python src/analyzer.py
```
*Outputs: `output/summary.json` and charts in `report/`*

### Step 3: Create Verification Template
Samples 20 random rows from your dataset for quality checks:
```bash
python src/verifier.py
```
*Outputs: `output/verification_template.csv`*

### Step 4: Run Accuracy Calculator
Processes the manual review results, logs differences, and computes final accuracy score:
```bash
python src/calculate_accuracy.py
```
*Outputs: `output/verification_summary.json` and `output/errors.csv`*

### Step 5: Automatically Compile HTML Report
Combines all stats, sample rows, and verified outputs into the HTML dashboard:
```bash
python src/generate_report.py
```
*Outputs: `report/index.html`*

### Step 6: View Dashboard
Open the compiled report directly in your default browser:
```powershell
# Windows
Start-Process "report/index.html"

# macOS/Linux
open report/index.html
```
