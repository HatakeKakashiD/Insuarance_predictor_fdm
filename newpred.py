import joblib
import pandas as pd

# Load the saved decision tree model and the MinMaxScaler used during training
model = joblib.load('xgb_model.joblib')
scaler = joblib.load('scaler.joblib')  # Load the scaler used in training

# Define a function to preprocess the input data
def preprocess_input(data):
    # Convert the input data to a DataFrame (assuming single input)
    input_df = pd.DataFrame([data])

    # Handle capital gain/loss to generate boolean columns
    input_df["capital_val"] = input_df["capital-gain"] - input_df["capital-loss"]
    input_df["capital_loss"] = input_df["capital_val"] < 0
    input_df["capital_neither"] = input_df["capital_val"] == 0
    input_df["capital_gain"] = input_df["capital_val"] > 0

    # Drop unused columns to match the model's input (as done during training)
    columns_to_drop = ["fnlwgt", "workclass", "race", "native-country", "gender", 
                       "capital-gain", "capital-loss", "capital_val"]

    # Only drop columns that are in the DataFrame
    input_df = input_df.drop(columns=[col for col in columns_to_drop if col in input_df.columns], axis=1)

    # One-hot encoding of categorical columns
    marital_status_dummies = pd.get_dummies(input_df["marital-status"], prefix='marital-status', drop_first=True)
    occupation_dummies = pd.get_dummies(input_df["occupation"], prefix='occupation', drop_first=True)
    relationship_dummies = pd.get_dummies(input_df["relationship"], prefix='relationship', drop_first=True)

    # Concatenate one-hot encoded columns with the input DataFrame
    input_df = pd.concat([input_df, marital_status_dummies, occupation_dummies, relationship_dummies], axis=1)

    # Drop original categorical columns
    input_df = input_df.drop(["marital-status", "occupation", "relationship"], axis=1)

    

    # Ensure the DataFrame has all the columns required by the scaler
    expected_columns = scaler.get_feature_names_out()
    
    # Reindex input_df to include all expected columns with default values of 0
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0  # Or np.nan if you want to use that
    
    # Reorder the columns to match the order used in fitting
    input_df = input_df[expected_columns]

    # Apply scaling (using the pre-fitted MinMaxScaler loaded earlier)
    scaled_input = scaler.transform(input_df)

    # Ensure the scaled input is returned as a DataFrame with correct column names
    scaled_input_df = pd.DataFrame(scaled_input, columns=expected_columns)
    scaled_input_df.info()
    return scaled_input_df

# Example input data (make sure it matches the expected format)
input_data = {
    "age": 20,
    "education": "Bachelors",
    "educational-num": 13,  # Correct educational numeric value
    "marital-status": "married",
    "occupation": "Others",
    "relationship": "Not-in-family",
    "capital-gain": 0,
    "capital-loss": 40000,
    "hours-per-week": 40
}

def get_prediction(data):
    # Preprocess the input data
    processed_input = preprocess_input(data)

    # Make prediction using the loaded model
    prediction = model.predict(processed_input)

    # Determine the income category based on the prediction
    income_prediction = "<=50K" if prediction[0] == 0 else ">50K"

    # Return the prediction result as a string
    return income_prediction

# Get the predicted income
predicted_income = get_prediction(input_data)
print(f"The predicted income is: {predicted_income}")
