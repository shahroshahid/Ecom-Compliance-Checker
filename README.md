# Ecom-Compiance-Checker
Automated compliance engine to audit financial communication logs against regulatory frameworks.
An automated Python and SQL compliance tracking system designed to audit digital communication logs (such as corporate chat applications) against financial regulatory frameworks. 

## Key Features
* **Automated Data Processing:** Utilizes SQLite and Pandas to parse system metadata logs.
* **Risk Mitigation Logic:** Automatically flags communication over unapproved off-channels (e.g., WhatsApp) to mitigate regulatory risks.
* **Insider Trading Detection:** Scans log text for phrases indicating potential market abuse or insider trading risks.
* **Executive Reporting:** Generates structured Excel audit reports formatted directly for ECOM Board review.

## Tech Stack
* **Language:** Python 3
* **Libraries:** Pandas, OpenPyXL
* **Database:** SQLite3

## How to Run
1. Install dependencies: `pip install pandas openpyxl`
2. Run the application: `python compliance_checker.py
