#!/usr/bin/env python3
"""
PAYPAL SENTINEL AI - Entry Point Launcher
Run with: python app.py
"""

import uvicorn
from backend.config import settings

def main():
    print("=" * 65)
    print(" 🚀 PAYPAL SENTINEL AI — Payment Intelligence & Recovery Platform")
    print(" Tagline: Detect. Investigate. Recover. Verify.")
    print("=" * 65)
    print(f" Environment : {settings.PAYPAL_MODE.upper()}")
    print(f" Server URL  : http://127.0.0.1:{settings.APP_PORT}")
    print(f" Default User: admin@sentinel.ai / admin123")
    print("=" * 65)

    uvicorn.run(
        "backend.main:app",
        host="127.0.0.1",
        port=settings.APP_PORT,
        reload=True
    )

if __name__ == "__main__":
    main()
