# SMS-Spam-Classification Project

![SMS Spam Classification](https://img.shields.io/badge/Project-SMS%20Spam%20Classification-blue?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0yMCA0SDRjLTEuMSAwLTEuOTkuOS0xLjk5IDJMMiAxOGMwIDEuMS45IDIgMiAyaDE2YzEuMSAwIDItLjkgMi0yVjZjMC0xLjEtLjktMi0yLTJ6bTAgNGwtOCA1LTgtNVY2bDggNSA4LTV2MnoiLz48L3N2Zz4=)
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-FF4B4B?style=flat-square&logo=streamlit)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

## 📌 Introduction

This project aims to classify SMS messages as either spam or ham (non-spam) using advanced machine learning techniques. Built with Streamlit, it encompasses comprehensive preprocessing, exploratory data analysis (EDA), and visualization. The application trains multiple models, including Naive Bayes, Random Forest, Support Vector Machine (SVM), and Gradient Boosting algorithms.

🔗 [Explore the Deployed Application](http://20.197.17.192:8501/)

## 🚀 Features

- **Preprocessing:** Robust data cleaning and transformation
- **EDA and Visualization:** In-depth insights and trends analysis
- **Model Training:** Implementation of various state-of-the-art machine learning algorithms
- **User-friendly Interface:** Built with Streamlit for easy interaction and result interpretation

## 🏗️ Project Structure

```
SMS-Spam-Classification
├── .gitignore
├── app.py
├── dataset
│   └── spam.csv
├── model
│   ├── model.pkl
│   └── vectorizer.pkl
├── requirements.txt
├── sms-spam-classification.ipynb
└── utils
    └── preprocess.py
```

### 📂 File Descriptions

- `.gitignore`: Specifies excluded files from Git version control
- `app.py`: Main application logic for the SMS spam classification model
- `dataset/spam.csv`: Dataset containing SMS messages and their labels
- `model/model.pkl`: Pickled machine learning model for classification
- `model/vectorizer.pkl`: Pickled vectorizer for text-to-numerical feature conversion
- `requirements.txt`: List of required Python packages
- `sms-spam-classification.ipynb`: Jupyter Notebook with data preprocessing, model training, and evaluation code
- `utils/preprocess.py`: Utility functions for text data preprocessing

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ShishirRijal/Spam-SMS-Classification.git
   cd Spam-SMS-Classification
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

5. **Access the application:**
   Open your web browser and navigate to `http://localhost:8501`

## 📸 Application Screenshots

<div align="center">
  <img src="https://github.com/user-attachments/assets/0274f32e-e054-40c0-a34b-41aadf35ceb3" alt="Screenshot 1" width="80%">
  <br><br>
  <img src="https://github.com/user-attachments/assets/572f6cfa-9851-4e19-ac41-8909a36fd8e1" alt="Screenshot 2" width="80%">
  <br><br>
  <img src="https://github.com/user-attachments/assets/70fa1d30-9dd4-4ecc-b94f-53e3df327922" alt="Screenshot 3" width="80%">
</div>

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/ShishirRijal/Spam-SMS-Classification/issues) if you want to contribute.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

Shishir Rijal - [@ShishirRijal](https://github.com/ShishirRijal)

Project Link: [https://github.com/ShishirRijal/Spam-SMS-Classification](https://github.com/ShishirRijal/Spam-SMS-Classification)

---

<div align="center">
  Made with ❤️ by Shishir Rijal
</div>
