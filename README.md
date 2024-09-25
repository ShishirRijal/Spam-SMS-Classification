## SMS-Spam-Classification Project

## Introduction
This project aims to classify SMS messages as either spam or ham (non-spam) using machine learning techniques. Built with Streamlit, it encompasses comprehensive preprocessing, exploratory data analysis (EDA), and visualization. The application trains multiple models, including Naive Bayes, Random Forest, Support Vector Machine (SVM), Gradient Boosting algorithms. The project structure consists of the following components:

- **Preprocessing:** Data cleaning and transformation.
- **EDA and Visualization:** Insights and trends in the data.
- **Model Training:** Implementation of various machine learning algorithms.

The code is structured modularly, enhancing readability and maintainability. 

You can explore the deployed application at [Deployed Link](http://20.197.17.192:8501/).

---

Feel free to fill in the deployed link, and let me know if you need any further adjustments!


### Project Overview

This project aims to classify SMS messages as either spam or ham (non-spam) using machine learning techniques. The project structure consists of the following components:

**Project Structure:**

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

**Description of Files:**

* `.gitignore`: Specifies files and directories that should be excluded from Git version control.
* `app.py`: Contains the main application logic for the SMS spam classification model.
* `dataset/spam.csv`: The CSV file containing the SMS messages and their corresponding labels (spam or ham).
* `model/model.pkl`: The pickled machine learning model used for classification.
* `model/vectorizer.pkl`: The pickled vectorizer used for converting text data into numerical features.
* `requirements.txt`: A list of Python packages required for the project.
* `sms-spam-classification.ipynb`: A Jupyter Notebook containing the code for data preprocessing, model training, and evaluation.
* `utils/preprocess.py`: A Python module containing utility functions for preprocessing text data.

### Running the Application
1. **Clone the repository:**
  ```bash
  git clone https://github.com/ShishirRijal/Spam-SMS-Classification.git
  cd Spam-SMS-Classification
  ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
   
3. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Streamlit app:**
  ```bash
  streamlit run app.py
  ```
5. **Access the application:**
   
  Open your web browser and go to `http://localhost:8501`


## Snaps:

<img width="1472" alt="Screenshot 2024-09-25 at 2 11 16 PM" src="https://github.com/user-attachments/assets/0274f32e-e054-40c0-a34b-41aadf35ceb3">
<img width="1465" alt="Screenshot 2024-09-25 at 2 11 38 PM" src="https://github.com/user-attachments/assets/572f6cfa-9851-4e19-ac41-8909a36fd8e1">
<img width="1472" alt="Screenshot 2024-09-25 at 2 11 59 PM" src="https://github.com/user-attachments/assets/70fa1d30-9dd4-4ecc-b94f-53e3df327922">


