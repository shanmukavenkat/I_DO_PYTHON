import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Sender and receiver
sender_email = "algotech.hr.team@gmail.com"   # Replace with a Gmail you control
receiver_email = "shanmukavenkatkomal@gmail.com"

# Email subject and body
subject = "Invitation to Group Discussion – Frontend Developer Role at Algo Tech"
body = """
Dear Komal,

Greetings from Algo Tech!

We are pleased to inform you that you have been shortlisted for the Frontend Developer – Group Discussion Round. 
This discussion is designed to evaluate your technical knowledge, problem-solving skills, and collaborative approach.

📌 Details of the Group Discussion:
- Date: Tomorrow
- Time: 10:00 AM – 12:00 PM
- Mode: Offline (In-person)
- Venue: Vasireddy Venkatadri Institute of Technology (VVIT), Guntur

 What you need to prepare:
- Strong understanding of HTML, CSS, JavaScript, React.js
- Awareness of latest frontend trends and best practices
- Ability to present your ideas clearly and work in a team discussion

Please confirm your participation by replying to this email at the earliest. 
Once confirmed, we will share any further instructions.

We look forward to seeing you in the discussion and wish you the very best for this round.

Best Regards,
Recruitment Team
Algo Tech
"""

# Setup MIME
msg = MIMEMultipart()
msg["From"] = "Algo Tech <algotech.hr.team@gmail.com>"
msg["To"] = receiver_email
msg["Subject"] = subject

msg.attach(MIMEText(body, "plain"))

# Send email via Gmail SMTP
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, "21bq1a4208")  # Replace with your Gmail App Password
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print("✅ Email sent successfully to", receiver_email)
except Exception as e:
    print("❌ Error:", e)
