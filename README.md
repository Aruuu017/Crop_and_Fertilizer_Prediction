# Smart Farming Assistant

## Overview
The **Smart Farming Assistant** is a Streamlit-based web application that helps farmers predict the best crop to grow and recommends the most suitable fertilizer based on soil and weather conditions. The app leverages machine learning models to provide accurate and data-driven recommendations.

## Features
- **Crop Recommendation System**: Predicts the most suitable crop based on soil nutrients, temperature, humidity, pH, and rainfall.
- **Fertilizer Recommendation System**: Suggests the optimal fertilizer based on soil properties and environmental conditions.
- **User-Friendly Interface**: Simple input sliders and number fields for easy data entry.
- **Fast Predictions**: Uses pre-trained machine learning models to deliver quick recommendations.

## Technologies Used
- **Python** (Backend and ML Model Processing)
- **Streamlit** (Frontend UI)
- **Scikit-learn** (Machine Learning)
- **Joblib** (Model Serialization)
- **NumPy** (Data Processing)

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/smart-farming-assistant.git
   cd smart-farming-assistant
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Ensure that the trained models (`decision_tree_model.pkl` and `fertilizer_model.pkl`) are present in the project directory.

5. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Open the app in your browser.
2. Use the **Crop Recommendation System** tab to input soil and climate data.
3. Click **Predict Crop** to get the recommended crop.
4. Switch to the **Fertilizer Recommendation System** tab to input soil and environmental data.
5. Click **Recommend Fertilizer** to receive fertilizer suggestions.

## Folder Structure
```
📂 smart-farming-assistant/
├── 📄 app.py                # Main Streamlit app
├── 📄 decision_tree_model.pkl  # Crop prediction model
├── 📄 fertilizer_model.pkl  # Fertilizer recommendation model
├── 📄 requirements.txt      # Dependencies
├── 📄 README.md             # Documentation
```

## Future Enhancements
- Add more advanced machine learning models.
- Expand the dataset for better predictions.
- Integrate weather APIs for real-time data updates.

## Developed by
**Aryan Zende**

📧 Contact: aryanzende017@gmail.com

