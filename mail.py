import streamlit as st
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Email function
def send_email(to_email, name, insurance_category):
    from_email = "insuaranceai@gmail.com"
    password = "hkpb pwvb suja ubtb"  # Use the generated App Password here

    # Email setup
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "You're Eligible for Multiple Insurance Packages – Explore Your Options!"

    body = f"""
    Dear {name},

    We are pleased to inform you that you are eligible for the following insurance packages with AiInsurance:

    Eligible Insurance Packages: {insurance_category}

     Should you need more information about the coverage details, pricing, or any other inquiries, please do not hesitate to reach out to us. Our team is happy to assist you with any additional questions and ensure that you receive the best possible insurance solution tailored to your needs.

    To learn more about this package or discuss pricing and further options, feel free to contact our support team via email or phone.

    Best regards,
    The AiInsurance Team

    ---
    AiInsurance | Your Trusted Insurance Partner
    Email: insuaranceai@gmail.com | Phone: (123) 456-7890
    """

    msg.attach(MIMEText(body, 'plain'))


    # SMTP server configuration (for Gmail)
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        st.success(f"Insurance package sent to {to_email}")
    except Exception as e:
        st.error(f"Error sending email: {e}")
        print(e)
