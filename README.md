# 📰 Fake News Detection System

A machine learning-based web application that detects whether a news article is **Real** or **Fake** using Natural Language Processing (NLP) and a Passive Aggressive Classifier.

## 🎯 Project Overview

This project consists of:
- **Streamlit Web App**: User-friendly interface for real-time fake news prediction
- **Machine Learning Model**: Trained using TF-IDF vectorization and Passive Aggressive Classifier
- **Jupyter Notebook**: Complete model training pipeline with visualizations

## 📁 Project Structure

```
samiullah/
├── app.py                    # Streamlit web application
├── model_file.ipynb          # Model training notebook (LSTM + sklearn models)
├── train.csv                 # Training dataset
├── fake_news_model.pkl       # Pre-trained classifier model
├── tfidf_vectorizer.pkl      # TF-IDF vectorizer
├── venv/                     # Virtual environment
└── README.md                 # This file
```

## 🛠️ Requirements

### Python Version
- Python 3.8 or higher

### Dependencies
```
streamlit
joblib
pandas
numpy
scikit-learn
tensorflow
nltk
matplotlib
seaborn
tqdm
```

## 🚀 Installation & Setup

### Step 1: Clone/Navigate to Project Directory
```bash
cd "samiullah"
```

### Step 2: Create Virtual Environment (Optional but Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install streamlit joblib pandas numpy scikit-learn tensorflow nltk matplotlib seaborn tqdm
```

Or install all at once:
```bash
pip install streamlit joblib pandas numpy scikit-learn tensorflow nltk matplotlib seaborn tqdm
```

## ▶️ Running the Application

### Option 1: Run the Streamlit Web App (Recommended)
```bash
streamlit run app.py
```

This will:
- Start a local web server
- Open your browser automatically at `http://localhost:8501`
- Display the Fake News Detection interface

### Option 2: Re-train the Model
If you want to train the model from scratch:

1. Open `model_file.ipynb` in Jupyter Notebook or VS Code
2. Run all cells sequentially
3. This will generate new `fake_news_model.pkl` and `tfidf_vectorizer.pkl` files

```bash
# To run Jupyter Notebook
jupyter notebook model_file.ipynb
```

## 📖 How to Use

1. **Start the application** using `streamlit run app.py`
2. **Enter news text** in the text area provided
3. **Click "Predict"** button
4. **View result**:
   - 🔴 **"This is Fake News!"** - The article is likely fake
   - 🟢 **"This is Real News!"** - The article is likely real

## 🔬 Model Details

### Training Pipeline
1. **Data Loading**: Load `train.csv` dataset
2. **Text Preprocessing**:
   - Convert to lowercase
   - Remove URLs and special characters
   - Remove stopwords
   - Apply stemming (Porter Stemmer)
3. **Feature Extraction**: TF-IDF Vectorization
4. **Model Training**: 
   - LSTM Neural Network (for deep learning approach)
   - Passive Aggressive Classifier (for production app)
5. **Model Saving**: Export as `.pkl` files using joblib

### Libraries Used
| Library | Purpose |
|---------|---------|
| TensorFlow/Keras | LSTM neural network |
| Scikit-learn | TF-IDF, Passive Aggressive Classifier |
| NLTK | Text preprocessing, stemming |
| Pandas | Data manipulation |
| Streamlit | Web interface |
| Matplotlib/Seaborn | Visualizations |

## ⚠️ Troubleshooting

### Common Issues

1. **"Model file not found" error**
   - Ensure `fake_news_model.pkl` and `tfidf_vectorizer.pkl` are in the same directory as `app.py`
   - Re-run the notebook to generate these files

2. **Port already in use**
   ```bash
   streamlit run app.py --server.port 8502
   ```

3. **Module not found**
   ```bash
   pip install <missing-module-name>
   ```

4. **Virtual environment not activated**
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

## 📊 Dataset

The `train.csv` file contains news articles with the following columns:
- `id`: Unique identifier
- `title`: Title of the news article
- `author`: Author of the article
- `text`: Full text content
- `label`: 0 = Real News, 1 = Fake News

## 🧪 Test Samples

Use these sample texts to test the application. Copy the entire text (including Title and Author) and paste it into the text area.

---

### 🔴 Fake News Samples (Expected: "This is Fake News!")

#### Sample A: Sensationalist Conspiracy
```
Title: BREAKING: Secret Memo Leaked Showing Global Elite Planning New Lockdown Next Month
Author: TruthSeeker2024
Text: A high-level whistleblower from an unnamed international organization has come forward with documents proving a coordinated effort to shut down all major cities starting next Tuesday. Sources say this is part of a "Great Reset" strategy to control small businesses. Major media outlets are being paid to remain silent. Share this before it gets taken down by the censors!
```

#### Sample B: Political Misinformation
```
Title: Federal Agents Caught Destroying Thousands of Ballots in Swing State Warehouse
Author: PatriotNewsNetwork
Text: Massive fraud has been uncovered in a rural county where witnesses claim they saw government vans loading bags of ballots into an industrial shredder. Local police were reportedly told to stand down by federal authorities. This explosive discovery could flip the entire election result, yet the mainstream media refuses to cover the story.
```

---

### 🟢 Real News Samples (Expected: "This is Real News!")

#### Sample C: Standard Political Reporting
```
Title: Senate Committee Convenes to Discuss New Infrastructure Bill Amendments
Author: Reuters Politics
Text: Members of the Senate Budget Committee met on Wednesday to debate the latest round of amendments to the proposed $1.2 trillion infrastructure legislation. The session focused on funding for rural broadband initiatives and bridge repairs in the Midwest. Both parties expressed a desire to reach a compromise before the holiday recess, though disagreements remain regarding tax adjustments.
```

#### Sample D: Health/Science Reporting
```
Title: CDC Updates Guidelines on Seasonal Flu Vaccinations for Elderly Patients
Author: Associated Press
Text: The Centers for Disease Control and Prevention issued updated guidance today regarding the timing of annual flu shots for adults over the age of 65. Health officials recommend receiving the vaccine by the end of October for maximum effectiveness during the winter months. The update comes after a clinical review suggested that early vaccination provides a more robust immune response for high-risk demographics.
```

---

### 📋 How to Test

1. **Copy** the entire sample text (Title + Author + Text)
2. **Paste** into the text area in your Streamlit app
3. **Click** the "Predict" button
4. **Compare** the result with the expected output

> **Note:** The model was trained on political news content, so it performs best on similar topics. Results may vary for other domains.

---

## 📝 License

This project is for educational purposes.

## 👤 Author

Developed as a Machine Learning project for Fake News Detection.

---

**Quick Start Command:**
```bash
streamlit run app.py
```
