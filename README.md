# 📊 ANOVA Analysis Web App (Streamlit)

This project is an interactive **Statistical Analysis Web App** built using **Streamlit**. It allows users to perform:

* Two-way ANOVA (with and without interaction)
* Tukey HSD post-hoc test
* Independent T-test between selected groups

---

## 🚀 Features

* 📂 Upload your own dataset (CSV)
* 🧹 Automatic data cleaning (handles missing + non-numeric values)
* 📊 ANOVA analysis:

  * Without interaction
  * With interaction
* 🔍 Tukey HSD multiple comparison test
* ⚖️ T-test between custom groups
* 📈 Clean and interactive UI

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Pandas
* Statsmodels
* SciPy
* Matplotlib

---

## 📁 Project Structure

```
anova-app/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation (Local Setup)

1. Clone the repository:

```
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

2. Create virtual environment:

```
python -m venv venv
```

3. Activate environment:

**Windows:**

```
venv\Scripts\activate
```

4. Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Run the App

```
streamlit run app.py
```

---

## 🌐 Deployment

This app can be deployed using **Streamlit Community Cloud**:

1. Push code to GitHub
2. Connect repository to Streamlit Cloud
3. Select `app.py`
4. Deploy 🚀

---

## 📌 How to Use

1. Upload a CSV file (e.g., Auto dataset)
2. Click:

   * "Run ANOVA (No Interaction)"
   * "Run ANOVA (With Interaction)"
   * "Run Tukey HSD"
3. Enter group labels for T-test (e.g., `1 8`, `3 4`)
4. View results instantly

---

## ⚠️ Notes

* Ensure your dataset contains:

  * `horsepower`
  * `origin`
  * `cylinders`
* Missing values are automatically handled

---

## 📷 Example Use Case

Analyze how **car origin** and **number of cylinders** affect horsepower using ANOVA and post-hoc tests.

---

## 👨‍💻 Author

* Your Name

---

## 📄 License

This project is for educational purposes.
