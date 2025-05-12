# 📦 Inventory Management System

This is a web-based Inventory Management System built with [Streamlit](https://streamlit.io/). It allows users to manage products like Electronics, Groceries, and Clothing with easy-to-use forms and persistent data storage using JSON files.

---

## 🚀 Features

- Add products (Electronics, Grocery, Clothing)
- View all current inventory items
- Sell products (decrease stock)
- Restock products (increase stock)
- Save inventory data to a file
- Load inventory data from a file
- Intuitive, responsive UI using Streamlit

---

## 🧱 Tech Stack

- **Frontend/UI**: [Streamlit](https://streamlit.io/)
- **Backend Logic**: Python OOP with custom models
- **Persistence**: JSON-based file storage
- **Typing & Safety**: Fully type-annotated, compatible with [MyPy](http://mypy-lang.org/)

---


bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
If you don't have requirements.txt, use:

bash
Copy
Edit
pip install streamlit
Run the app

bash
Copy
Edit
streamlit run app.py
🧪 Testing & Type Checking
To check type safety with MyPy:

bash
Copy
Edit
mypy app.py models/
💾 Saving & Loading Data
Default file path for saving and loading inventory is data/main.json.

You can change the file name in the Save/Load section of the UI.

🧑‍💻 Author
Developed by Sarwat Majeed
Feel free to contribute or fork the project!

📜 License
This project is open-source under the MIT License.

yaml
Copy
Edit

---

### 📎 Next Steps (Optional Enhancements)

- Add product search/filtering
- Export inventory to CSV or Excel
- User login system for role-based access
- Switch to a database (SQLite/PostgreSQL) for larger-scale usage

---

Let me know if you'd like a `requirements.txt` generated too, or a sample dataset for testing!



