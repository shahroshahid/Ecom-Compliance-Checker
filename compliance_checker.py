import sqlite3
import pandas as pd
from datetime import datetime

# 1. Initialize Mock Database of Communication Logs
def setup_database():
    conn = sqlite3.connect('ecom_communications.db')
    cursor = conn.cursor()
    
    # Create the communications table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chat_logs (
            log_id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            employee_email TEXT,
            platform TEXT,
            message_text TEXT
        )
    ''')
    
    # Mock data capturing standard interactions and clear policy violations
    mock_data = [
        ('2026-08-10 09:15:00', 'j.smith@db.com', 'MS Teams', 'Let us schedule the project kick-off for 2 PM today.'),
        ('2026-08-10 10:22:00', 'a.jones@db.com', 'WhatsApp', 'Hey, I am sending the client portfolio data here instead of email.'),
        ('2026-08-10 11:05:00', 'r.taylor@db.com', 'MS Teams', 'The corporate earnings report looks great for next week.'),
        ('2026-08-10 14:30:00', 'm.shahzor@db.com', 'Symphony', 'Please review the attached data retention policy updates.'),
        ('2026-08-10 16:12:00', 'a.jones@db.com', 'MS Teams', 'Buy shares in Company X before the press release drops tomorrow morning.')
    ]
    
    cursor.executemany('''
        INSERT INTO chat_logs (timestamp, employee_email, platform, message_text)
        VALUES (?, ?, ?, ?)
    ''', mock_data)
    
    conn.commit()
    conn.close()
    print("[INFO] Database initialized with communication logs.")

# 2. Compliance Evaluation Business Logic
def evaluate_compliance(message, platform):
    # Rule A: Unapproved off-channel communications (Regulatory Breach)
    unapproved_platforms = ['WhatsApp', 'WeChat', 'Signal']
    if platform in unapproved_platforms:
        return "FAIL", "Unapproved Communication Channel Used"
        
    # Rule B: Insider Trading Risk Keywords
    risk_keywords = ['buy shares', 'insider', 'press release drops', 'confidential data', 'off the record']
    if any(keyword in message.lower() for keyword in risk_keywords):
        return "FAIL", "Potential Market Abuse / Insider Trading Risk"
        
    return "PASS", "Compliant"

# 3. Process Logs and Generate the Board Audit Report
def generate_ecom_report():
    conn = sqlite3.connect('ecom_communications.db')
    
    # Query database records using Pandas
    df = pd.read_sql_query("SELECT * FROM chat_logs", conn)
    
    # Apply compliance rules
    evaluation_results = df.apply(lambda row: evaluate_compliance(row['message_text'], row['platform']), axis=1)
    
    # Split results into distinct status and reason columns
    df['ECOM_Status'] = [res[0] for res in evaluation_results]
    df['Flag_Reason'] = [res[1] for res in evaluation_results]
    
    # Add metadata for audit tracking
    df['Review_Timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    df['Reviewed_By'] = 'M. Shahzor (ECOM Analyst)'
    
    # Export to Excel optimized for board review
    report_filename = 'ECOM_Compliance_Audit_Report.xlsx'
    df.to_excel(report_filename, index=False, sheet_name='Audit Log Summary')
    
    conn.close()
    print(f"[SUCCESS] ECOM Audit Report generated successfully: {report_filename}")

if __name__ == "__main__":
    setup_database()
    generate_ecom_report()
