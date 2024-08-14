from flask import Flask, request, render_template
import pickle
import numpy as np

# Create a Flask application instance
app = Flask(__name__, template_folder='.')

# Load the trained K-Means model
with open("customer_segmentation_kmeans_model.pkl", "rb") as file:
    model = pickle.load(file)

# Define a route for the homepage
@app.route("/")
def home():
    return render_template("index.html")  # Render the index.html template

# Define a route for making predictions
@app.route("/predict", methods=["POST"])
def predict():
    # Get input data from the form
    annual_income = float(request.form["annual_income"])
    spending_score = float(request.form["spending_score"])

    # Combine inputs into a single list
    input_data = np.asarray([[annual_income, spending_score]])

    # Make a prediction using the model
    cluster_prediction = model.predict(input_data)[0]

    # Define cluster names
    cluster_names = {
        0: "Low Income, Low Spending",
        1: "Low Income, High Spending",
        2: "Average Income, Average Spending",
        3: "High Income, Low Spending",
        4: "High Income, High Spending"
    }

    # Get the name of the predicted cluster
    predicted_cluster_name = cluster_names.get(cluster_prediction, "Unknown Cluster")

    # Pass the prediction value to the template
    return render_template("index.html", prediction=predicted_cluster_name)

# Start the Flask application
if __name__ == "__main__":
    app.run(debug=True)  # Run the application in debug mode for development
