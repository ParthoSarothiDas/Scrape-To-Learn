# 🌐 world-explorer-app    – Powered by Streamlit & BeautifulSoup
[🌐Visit Website](https://world-explorer.streamlit.app/)

An interactive learning and quiz platform where users can explore and test their knowledge of countries through flags, capitals, globe locations, and fun facts. This project combines **web scraping**, **data wrangling**, and **Streamlit** to deliver a rich educational experience.

---

## 🛠️ Project Overview

This app was built by:
- 📥 Scraping data from **Wikipedia** using `BeautifulSoup`
- 🏗️ Structuring the data into a **Pandas DataFrame**
- 🎨 Creating an interactive **Streamlit** web app for learning and quizzing

---

## 🔍 Scraped Data Includes

- **Flag Image**
- **Globe Image (location map)**
- **Short Wikipedia-style Description**

All scraped data was cleaned, verified, and converted into a DataFrame to power the app.

---

## 🧠 App Features

### ✅ 1: Learn About Countries
- Select a country and view:
  - Its capital, continent
  - Flag and globe location image
  - Introductory paragraph from Wikipedia

### 🌍 2: Identify Country from Globe
- Guess the country from its globe map
- Scoring:
  - +5 points for each correct answer
  - Game ends after 3 consecutive wrong answers

### 🚩 3: Guess the Flag
- Identify the correct country based on the flag shown
- Includes scoring and game-over logic

### 🌐 4: Continent Challenge
- Given a country and flag, select its continent
- Tracks your score, ends game after 3 wrong answers

### 🎌 5: Capital Quiz
- Given a country and its flag, guess the correct capital city

---

## 🧰 Tech Stack

- **Python 3**
- **BeautifulSoup** – Web scraping
- **Pandas** – Data manipulation
- **Streamlit** – App interface

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/world-quiz-app-streamlit.git
cd world-quiz-app-streamlit
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> *Required packages: `streamlit`, `pandas`, `beautifulsoup4`, `requests`*

### 3. Run the App

```bash
streamlit run app.py
```

### 4. Folder Structure

```
├── data/
│   └── df_country_info.csv     # Final dataset
|   └── Other Datasets
├── flags/                      # Downloaded flag images
│   └── *.png
├── globe_image/                # Downloaded globe images
│   └── *.png
├── 1_globe_image_scraping_processing.ipynb      Optional: scripts for scraping
│
├── 2_flag_image_scraping_processing.ipynb
│
├── 3_country_info_scraping_processing.ipynb
│
├── 4_merge_all_scraped_data_processing.ipynb
|
├── world-explorer-app
|
├── README.md
```

---

## ✨ Potential Future Features

* Leaderboard and scoring history
* Randomized quiz modes (timed, streak, etc.)
* Text-to-speech for younger learners
* Mobile responsive version

---

## ✍️ Author

**Partho Sarothi Das**
📍 Dhaka, Bangladesh
🎯 Data Science Enthusiast | Aspiring ML Developer
🧒 Inspired by my child to make learning fun through technology

---

## 🪪 License

This project is licensed under the **MIT License** – feel free to use and extend!

---

## 🙌 Acknowledgements

* Wikipedia for open content
* Streamlit for its developer-friendly web framework
