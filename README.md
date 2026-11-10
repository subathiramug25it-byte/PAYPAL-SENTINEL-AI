# 🚀 PAYPAL SENTINEL AI

### Explainable Payment Intelligence, Investigation & Recovery Platform
**Tagline:** *Detect. Investigate. Recover. Verify.*

---

## 🌟 Executive Overview
**PayPal Sentinel AI** is an enterprise-grade fintech SaaS platform built to detect inconsistencies between authoritative PayPal payment ledgers and merchant order databases, explain findings with verifiable evidence, recommend safe recovery actions, and provide an immutable audit trail.

---

## 🎯 Key Differentiators
1. **Cross-System Integrity Engine:** Real-time correlation between PayPal REST captures/refunds and internal merchant order states.
2. **Explainable AI Investigation Center:** Evidence-grounded root-cause analysis distinguishing confirmed facts from technical inferences.
3. **Verified Safe Auto-Remediation:** Idempotent state synchronization with pre- and post-action verification (no accidental double-charges).
4. **Live Webhook Ingestion & Idempotency Defense:** Bounded retries and cryptographic duplicate prevention (`DUPLICATE_IGNORED`).
5. **OCR Payment Proof Guard:** Authoritative verification of customer checkout screenshots against PayPal ledger records.
6. **Multi-Language Support:** Instant client-side localization for English, தமிழ் (Tamil), and हिन्दी (Hindi).
7. **Premium Fintech UX:** Dark Navy / Light / System themes, customizable accent colors, Chart.js analytics, and mobile-responsive layouts.

---

## 🏗️ Project Architecture
```text
PAYPAL_SENTINEL_AI/
│
├── app.py                     # Primary Application Runner
├── requirements.txt           # Project Dependencies
├── .env                       # Environment Variables (Local)
├── .env.example               # Safe Template Credentials
├── README.md                  # Documentation
│
├── backend/
│   ├── main.py                # FastAPI Application Factory & Lifespan
│   ├── config.py              # Environment Configuration
│   │
│   ├── api/                   # Modular API Route Controllers
│   │   ├── auth.py            # Login, Session Tokens, User Roles
│   │   ├── dashboard.py       # Metrics, Charts, Operational Activity
│   │   ├── transactions.py    # Ledger Explorer & In-depth Inspection
│   │   ├── investigations.py  # AI Root Cause & Safe Auto-Remediation
│   │   ├── webhooks.py        # PayPal Ingestion & Idempotency Guard
│   │   ├── fraud.py           # Anomaly Scoring & OCR Receipt Cross-Check
│   │   ├── reconciliation.py  # Smart Merchant vs PayPal Comparison
│   │   ├── disputes.py        # Dispute Copilot & Evidence Checklists
│   │   ├── reports.py         # CSV Compliance Exports & Metrics
│   │   ├── notifications.py   # Real-Time Operational Incident Alerts
│   │   ├── settings.py        # Appearance, Locale, PayPal Credentials
│   │   ├── help.py            # 15+ Interactive Documentation Guides
│   │   ├── simulator.py       # Chaos Simulator Injection Endpoints
│   │   └── integrity.py       # Background Ledger Scan Trigger
│   │
│   ├── database/
│   │   ├── db.py              # SQLAlchemy Engine & SessionLocal
│   │   ├── models.py          # Relational Database Models
│   │   └── seed_data.py       # Realistic Fintech Demo Dataset
│   │
│   └── security/
│       ├── authentication.py  # PBKDF2-HMAC-SHA256 Password Hashing
│       ├── authorization.py   # RBAC: Admin, Analyst, Viewer
│       └── secrets.py         # Credential Masking & Safe Display
│
├── templates/                 # Jinja2 Modern UI Templates
│   ├── base.html              # Master Sidebar & Topbar Shell
│   ├── login.html             # Sleek Auth Portal with Quick Demo Roles
│   ├── dashboard.html         # Live Operations Hub & Chart.js Visuals
│   ├── transactions.html      # Cross-Ledger Transaction Explorer
│   ├── transaction_detail.html# Deep Multi-Ledger Inspector
│   ├── investigations.html    # AI Root-Cause Center & Stepper
│   ├── investigation_detail.html
│   ├── webhook_monitor.html   # Real-Time Event Pipeline & Retry Controls
│   ├── fraud_analysis.html    # OCR Receipt & Anomaly Guard
│   ├── reconciliation.html    # Merchant vs PayPal Ledger Matcher
│   ├── disputes.html          # Dispute Evidence Packager
│   ├── reports.html           # Analytics & CSV Export
│   ├── notifications.html     # Alert Incident Feed
│   ├── profile.html           # Operator Profile & Security Credentials
│   ├── settings.html          # All 7 SaaS Settings Modules
│   └── help.html              # Complete 15-Section Documentation
│
├── static/
│   ├── css/
│   │   ├── themes.css         # Dark Navy, Light, Accent Color Tokens
│   │   ├── style.css          # Fintech Layout, Chips, Cards, Badges
│   │   └── responsive.css     # Tablet & Mobile Drawer Styling
│   └── js/
│       ├── app.js             # Toasts, Shortcuts, Global Scan Controller
│       ├── theme.js           # Theme Manager (Dark / Light / System)
│       └── language.js        # Instant Client-Side I18n Engine
│
├── locales/                   # Complete Translation Dictionaries
│   ├── en.json                # English (Default)
│   ├── ta.json                # தமிழ் (Tamil)
│   └── hi.json                # हिन्दी (Hindi)
│
└── tests/
    └── test_phase1.py         # Pytest Verification Suite (100% Pass)
```

---

## ⚡ Quick Start & Installation

### 1. Prerequisites
- Python 3.10+ (Tested on Python 3.14.7)
- Windows / macOS / Linux

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch Sentinel AI
```bash
python app.py
```
Open your browser at: **`http://127.0.0.1:8000`**

### 4. Default Demo Accounts
| Role | Email | Password | Privileges |
| :--- | :--- | :--- | :--- |
| **Admin (Lead SecOps)** | `admin@sentinel.ai` | `admin123` | Full Access, Remediation, Keys |
| **Analyst (Fintech Ops)**| `analyst@sentinel.ai`| `analyst123`| Scans, Evidence Review, Reconcile |

---

## 🧪 Running the Automated Test Suite
```bash
python -m pytest tests/test_phase1.py -v
```
All unit tests verify database seeding, password hashing, route rendering, safe auto-remediation, webhook idempotency, and CSV streaming.
