# Customer Segmentation Using K-Means Clustering

This project demonstrates the use of the K-Means clustering algorithm to segment customers based on their annual income and spending scores. The goal is to categorize customers into distinct groups that share similar spending habits and income levels.

## Project Overview

- **Algorithm**: K-Means Clustering
- **Language**: Python
- **Framework**: Flask (for web deployment)
- **Tools/Libraries**: 
  - Numpy
  - Pandas
  - Matplotlib
  - Seaborn
  - Scikit-learn
  - Flask

## Project Structure

- **app.py**: Contains the Flask web application code to handle user input, predict customer segments, and render the results on a webpage.
- **index.html**: The front-end template where users can input their annual income and spending score to get a prediction of their customer segment.
- **customer_segmentation_kmeans_model.pkl**: The saved K-Means model used to predict customer segments.
- **README.md**: Documentation and overview of the project (this file).

## Dataset

The dataset used in this project is the [Mall Customers Dataset](https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python), which contains information on customers' annual income and spending scores. The dataset has been used to train a K-Means model to identify different customer segments.

## K-Means Clustering

K-Means clustering is an unsupervised machine learning algorithm that groups similar data points into clusters. The goal is to partition the dataset into K clusters, where each data point belongs to the cluster with the nearest mean.

## Elbow Method for Optimal K

The Elbow method was used to determine the optimal number of clusters (K) by plotting the Within-Cluster Sum of Squares (WCSS) against the number of clusters. The "elbow point" on the graph indicates the optimal K value, which was found to be 5 in this case.

## Web Application

A simple web interface was created using Flask, allowing users to input their annual income and spending score to predict their customer segment. The prediction is based on the trained K-Means model.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Pahinithi/Customer-Segmentation-Using-K-Means-Clustering-Machine-Learning
   cd Customer-Segmentation
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Open your browser and go to `http://127.0.0.1:5000/`.

## Usage

1. Enter the customer's annual income (in k$).
2. Enter the customer's spending score (1-100).
3. Click "Predict Segment" to see which customer segment the individual belongs to.

## Clusters

- **Cluster 1**: Low Income, Low Spending
- **Cluster 2**: Low Income, High Spending
- **Cluster 3**: Average Income, Average Spending
- **Cluster 4**: High Income, Low Spending
- **Cluster 5**: High Income, High Spending

## License

This project is licensed under the MIT License

## Acknowledgments

- Special thanks to [Kaggle](https://www.kaggle.com/) for providing the dataset.
