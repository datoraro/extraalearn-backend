
import os
import joblib
import pandas as pd
from flask import Flask, request, jsonify

# Initialize Flask application
learn_api = Flask("ExtraaLearn")

# Locate and load the trained model
model_path = os.path.join(
    os.path.dirname(__file__),
    "learn_model.joblib"
)

model = joblib.load(model_path)


# Home endpoint
@learn_api.get("/")
def home():
    return "Welcome to the ExtraaLearn Lead Prediction System"


# Prediction endpoint
@learn_api.post("/v1/predict")
def predict_sales():

    # Get JSON data from request
    data = request.get_json()

    # Extract lead features
    sample = {
        "age": data["age"],
        "current_occupation": data["current_occupation"],
        "first_interaction": data["first_interaction"],
        "profile_completed": data["profile_completed"],
        "website_visits": data["website_visits"],
        "time_spent_on_website": data["time_spent_on_website"],
        "page_views_per_visit": data["page_views_per_visit"],
        "last_activity": data["last_activity"],
        "print_media_type1": data["print_media_type1"],
        "print_media_type2": data["print_media_type2"],
        "digital_media": data["digital_media"],
        "educational_channels": data["educational_channels"],
        "referral": data["referral"],
    }

    # Convert input data to DataFrame
    input_data = pd.DataFrame([sample])

    # Generate prediction
    prediction = int(model.predict(input_data)[0])

    # Return prediction
    return jsonify({
        "Lead": prediction
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    learn_api.run(
        host="0.0.0.0",
        port=port
    )
