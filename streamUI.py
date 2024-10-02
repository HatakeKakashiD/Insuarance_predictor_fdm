import streamlit as st
from PIL import Image
import base64
from insuarancedecider import get_insurance_types
from newpred import get_prediction
from mail import send_email
import time

# Function to set the background image
def set_background_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    background_css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_string}");
        background-size: cover;
    }}
    div[data-testid="stForm"] {{
        background-color: black;
        padding: 20px;
        border-radius: 10px;
        color: white;
    }}
    </style>
    """
    st.markdown(background_css, unsafe_allow_html=True)

# Set the background image
set_background_image(r"https://github.com/HatakeKakashiD/Insuarance_predictor_fdm/blob/main/6803.jpeg")

# Create a header bar with custom styling
header_css = """
    <style>
    .header-bar {
        background-color: #1e2645;  /* Change to your preferred color */
        padding: 10px;
        text-align: center;
        border-radius: 8px;
        border-width: 100px;  /* Full viewport width */
        color: white;
        font-size: 30px;
        font-weight: bold;
        margin-bottom: 25px;
    }
    </style>
"""
st.markdown(header_css, unsafe_allow_html=True)
st.markdown('<div class="header-bar">Insurance Package Selector</div>', unsafe_allow_html=True)


# Initialize session state variables
if 'email' not in st.session_state:
    st.session_state.email = None
if 'first_name' not in st.session_state:
    st.session_state.first_name = None
if 'insurance_category' not in st.session_state:
    st.session_state.insurance_category = None
if 'button_pressed' not in st.session_state:
    st.session_state.button_pressed = False

# Streamlit form for user input
# Streamlit form for user input
with st.form(key="user_info_form"):
    first_name = st.text_input("Name:")
    gender = st.radio("Gender:", ["Male", "Female"])
    marital_status = st.selectbox("Marital Status:", [" ", "Married", "Un-Married", "Divorced"], index=0)
    age = st.number_input("Age:", min_value=0, max_value=120, step=1)
    relationship = st.selectbox("Relationship(Specific Role):", ["", "Wife", "Own-child(child in the household (biologically or adopted))", "Husband", "Not-in-family(lives alone)", "Other-relative(relavtive to the head of the household)", "Unmarried"], index=0)
    relationship_mapping = {
        "Wife":"Wife","Own-child(child in the household (biologically or adopted))":"own-child","Husband":"Husband","Not-in-family(lives alone)":"Not-in-family", "Other-relative(relavtive to the head of the household)":"Other-relative","Unmarried":"Unmarried"
    }
    
    education = st.selectbox("Education Qualification:", [
        " ", "Preschool", "1st-4th Grade", "5th-6th Grade", "7th-8th Grade",
        "9th Grade", "10th Grade", "11th Grade", "12th Grade", "High School Graduate",
        "Some College", "Associate's Degree (Vocational)", "Associate's Degree (Academic)",
        "Master's Degree", "Professional School", "Doctorate Degree"
    ], index=0)

    education_mapping = {
        "Preschool": 1, "1st-4th Grade": 2, "5th-6th Grade": 3, "7th-8th Grade": 4,
        "9th Grade": 5, "10th Grade": 6, "11th Grade": 7, "12th Grade": 8,
        "High School Graduate": 9, "Some College": 10, "Associate's Degree (Vocational)": 11,
        "Associate's Degree (Academic)": 12, "Master's Degree": 14,
        "Professional School": 15, "Doctorate Degree": 16
    }

    email = st.text_input("Email:")
    phone = st.text_input("Phone:")
    
    workclass = st.selectbox("Workclass:", [
        " ", "Private Sector Employee", "Self-Employed (Not Incorporated)", 
        "Self-Employed (Incorporated)", "Federal Government Employee",
        "Local Government Employee", "State Government Employee", 
        "Unpaid Worker", "Never Worked"
    ], index=0)

    # Add occupation field
    occupation = st.selectbox("Occupation:", [
        " ", "Craftsman", "Executive", "Service Worker", 
        "Other Occupation", "Healthcare Professional", "Sales Representative"
    ], index=0)

    occupation_mapping = {
    "Craftsman": "Craft-repair", 
    "Executive": "Exec-managerial", 
    "Service Worker": "Other-service", 
    "Other Occupation": "Others", 
    "Healthcare Professional": "Prof-specialty", 
    "Sales Representative": "Sales"
     }

    hours_per_week = st.number_input("Hours working within a week:", min_value=0, max_value=168, step=1)
    income_gain = st.number_input("Capital Gain( profit made from selling an asset):", min_value=0, max_value=1000000, step=1)
    income_loss = st.number_input("Capital Loss(financial loss from selling assets):", min_value=0, max_value=1000000, step=1)

    # Submit button
    submit_button = st.form_submit_button(label="Submit")


# Capture input from form and store in session state
if submit_button:
    # Validation
    if not first_name:
        st.error("Name is required.")
    elif not marital_status:
        st.error("Marital Status is required.")
    elif not relationship:
        st.error("Relationship is required.")
    elif not education:
        st.error("Education Qualification is required.")
    elif not age:
        st.error("Age is required.")
    elif not occupation:
        st.error("occupation is required.")    
    elif not workclass:
        st.error("Workclass is required.")
    elif not email or "@" not in email or "." not in email:
        st.error("Invalid email address.")
    elif not phone or not (10 <= len(phone) <= 11) or not phone.isdigit():
        st.error("Invalid phone number.")
    else:
        # Prepare input data for prediction
        input_data = {
            "age": age,
            "workclass": workclass,
            "fnlwgt": 77516,
            "education": education,
            "educational-num": education_mapping[education],
            "marital-status": marital_status,
            "occupation": occupation_mapping[occupation],
            "relationship": relationship_mapping[relationship],
            "race": "white",
            "gender": gender,
            "capital-gain": income_gain,
            "capital-loss": income_loss,
            "hours-per-week": hours_per_week,
            "native-country": "United"
        }

        # Call the prediction function and get the result
        income_category = get_prediction(input_data)  # Replace with your prediction logic
        insurance_category = get_insurance_types(income_category, age, workclass)  # Replace with your insurance logic

        # Store the results in session state
        st.session_state.email = email
        st.session_state.first_name = first_name
        st.session_state.insurance_category = insurance_category
                        
        if income_category == '>50K':
            income_message = "Income is greater than 50K."
        else:
            income_message = "Income is less than or equal to 50K."
        
            # Create a container for the prediction results and insurance options
        with st.container():
            # Define a common CSS class for the text
            st.markdown("""
                <style>
                .prediction-text {
                    font-size: 22px; /* Default font size */
                    color: yellow; /* Correct property for text color */
                }
                .prediction-large {
                    font-size: 32px; /* Larger font size */
                }
                </style>
            """, unsafe_allow_html=True)
            
            # Display the prediction label with increased font size
            st.markdown("<div class='prediction-large'><strong>Predicted Income category:</strong></div>", unsafe_allow_html=True)
            
            # Display the predicted income category with increased font size
            st.markdown(f"<div class='prediction-text'><strong>{income_message}</strong></div>", unsafe_allow_html=True)
            
            # Display the prediction label for insurance category
            st.markdown("<div class='prediction-large'><strong>Predicted Insurance Category:</strong></div>", unsafe_allow_html=True)
            
            # Display the predicted insurance category with default font size
            st.markdown(f"<div class='prediction-text'><strong>{insurance_category}</strong></div>", unsafe_allow_html=True)


            



if st.session_state.insurance_category and st.button("Send Email") and not st.session_state.button_pressed:
    try:
        # Initialize progress bar
        progress_bar = st.progress(0)
        
        # Simulate preparation steps for email sending with progress updates
        progress_bar.progress(20)  # 20%: Initial preparation
        time.sleep(0.5)  # Simulate step delay
        
        # Step 1: Prepare email content
        progress_bar.progress(40)  # 40%: Email content prepared
        time.sleep(0.5)
        
        # Step 2: Establish connection to email server (for example)
        progress_bar.progress(60)  # 60%: Connection established
        time.sleep(0.5)
        
        # Step 3: Send email
        send_email(st.session_state.email, st.session_state.first_name, st.session_state.insurance_category)
        progress_bar.progress(80)  # 80%: Email sent
        
        # Step 4: Finalizing process
        time.sleep(0.5)
        progress_bar.progress(100)  # 100%: Process complete
        
        st.session_state.button_pressed = True
        st.success("Email sent successfully!")
    except Exception as e:
        st.error(f"Error sending email: {e}")

# Display the message based on the button state
if st.session_state.button_pressed:
    st.write("Email already sent.")
