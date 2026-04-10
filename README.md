# 💰 Personal Finance Health Analyzer

A smart and interactive web application built using **Streamlit** that analyzes your financial health using real-world financial formulas and rule-based algorithms.

---

## 🚀 Overview

The **Personal Finance Health Analyzer** helps users understand their financial condition by evaluating income, expenses, savings, and debt. It provides a **financial health score**, **risk level**, and **actionable recommendations**.

---

## ⚙️ How It Works

1. Enter your financial details:

   * Monthly Income
   * Monthly Expenses
   * Savings
   * Debt Payments
   * Total Debt
   * Credit Card Usage

2. Click **"Run Financial Analysis"**

3. The system:

   * Validates inputs
   * Applies financial formulas
   * Runs analysis logic

4. Output includes:

   * 📊 Financial metrics
   * 📈 Graphs
   * 💡 Recommendations
   * ⭐ Health score

---

## 🔥 Key Features

* ✅ Real-time financial analysis
* ✅ Financial Health Score (0–100)
* ✅ Risk Classification (Low / Medium / High)
* ✅ Remaining Monthly Purse calculation
* ✅ Credit limit validation system
* ✅ Interactive charts (Plotly)
* ✅ Personalized recommendations
* ✅ Financial summary table with status indicators

---

## 📊 Financial Metrics & Formulas

### 1. Savings Rate

**Formula:**

```
Savings Rate = (Income − Expenses) / Income × 100
```

**Why used:**
Measures how much income is saved. Higher is better.

---

### 2. Debt-to-Income Ratio (DTI)

**Formula:**

```
DTI = (Monthly Debt Payments / Income) × 100
```

**Why used:**
Shows how much income goes toward debt. Lower is better.

---

### 3. Credit Utilization

**Formula:**

```
Credit Utilization = (Credit Used / Credit Limit) × 100
```

**Why used:**
Indicates how much credit you are using. Above 30% is risky.

---

### 4. Emergency Fund Ratio

**Formula:**

```
Emergency Fund = Savings / Monthly Expenses
```

**Why used:**
Shows how many months you can survive without income.

---

### 5. Debt-to-Asset Ratio

**Formula:**

```
Debt-to-Asset Ratio = (Total Debt / (Total Debt + Savings)) × 100
```

**Why used:**
Measures overall financial burden.

---

### 6. Disposable Income

**Formula:**

```
Disposable Income = Income − Expenses
```

**Why used:**
Money left after expenses.

---

### 7. Net Income

**Formula:**

```
Net Income = Disposable Income − Debt Payments
```

**Why used:**
Actual usable money after obligations.

---

### 8. Remaining Monthly Purse

**Formula:**

```
Remaining Purse = Income − (Expenses + Debt Payments + Credit Spending)
```

**Why used:**
Shows real leftover money and detects overspending.

---

## 🧠 Algorithm Logic

1. Take user inputs
2. Validate inputs (credit limit check)
3. Calculate all financial metrics
4. Apply financial rules:

   * Savings Rate ≥ 20% → Good
   * DTI ≤ 36% → Healthy
   * Credit Utilization ≤ 30% → Safe
5. Generate **Health Score (0–100)**
6. Classify risk:

   * 🟢 Low Risk
   * 🟡 Medium Risk
   * 🔴 High Risk
7. Provide personalized recommendations

---

## 📈 Output

* Financial Health Score
* Risk Category
* Savings & Debt Metrics
* Interactive Financial Graph
* Personalized Recommendations
* Financial Summary Table

---

## 🛠️ Installation & Setup

```bash
git clone https://github.com/SohamAdgatla/Cep_Sem_4_Project
cd Cep_Sem_4_Project
pip install -r requirements.txt
streamlit run main.py
```

---

## 🧪 Tech Stack

* Python
* Streamlit
* Pandas
* Plotly

---

## 🎯 Use Cases

* Students learning finance
* Individuals tracking money
* Beginners understanding financial ratios
* Academic projects

---

## 🔮 Future Enhancements

* AI-based financial prediction
* Budget planner system
* Expense tracking
* Mobile-friendly UI

---

## 🤝 Contributing

Contributions are welcome! Feel free to submit a pull request.

---

## 📜 License

This project is open source under the MIT License.
