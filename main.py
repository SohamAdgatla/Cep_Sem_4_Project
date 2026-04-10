# Personal Finance Health Analyzer
#X
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from backend import run_financial_analysis

# ---------------------------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="Personal Finance Health Analyzer",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Personal Finance Health Analyzer")
st.markdown("*Formula-based financial assessment using proven algorithms*")

# ---------------------------------------------------------------------------
# HELPER FUNCTION
# ---------------------------------------------------------------------------

def create_financial_overview_chart(monthly_income, monthly_expenses, current_savings, monthly_debt_payments):
    disposable_income = monthly_income - monthly_expenses
    net_income = disposable_income - monthly_debt_payments

    fig = go.Figure()

    fig.add_trace(go.Bar(
        name='Income Flow',
        x=['Gross Income', 'After Expenses', 'After Debt Payments'],
        y=[monthly_income, disposable_income, net_income],
    ))

    fig.add_trace(go.Scatter(
        name='Savings',
        x=['Gross Income', 'After Expenses', 'After Debt Payments'],
        y=[current_savings]*3,
        mode='lines+markers'
    ))

    return fig

# ---------------------------------------------------------------------------
# SIDEBAR INPUTS
# ---------------------------------------------------------------------------

with st.sidebar:
    st.header("📊 Financial Data Input")

    monthly_income = st.number_input("Monthly Income ($)", min_value=0.0, value=5000.0)
    monthly_expenses = st.number_input("Monthly Expenses ($)", min_value=0.0, value=3500.0)
    current_savings = st.number_input("Current Savings ($)", min_value=0.0, value=15000.0)
    monthly_debt_payments = st.number_input("Monthly Debt Payments ($)", min_value=0.0, value=800.0)
    total_debt = st.number_input("Total Debt ($)", min_value=0.0, value=25000.0)

    credit_card_spending = st.number_input("Credit Card Balance ($)", min_value=0.0, value=2000.0)
    total_credit_limit = st.number_input("Credit Card Limit ($)", min_value=0.0, value=5000.0)

    # ---------------- VALIDATION ----------------
    if total_credit_limit == 0 and credit_card_spending > 0:
        st.warning("⚠️ Credit card limit cannot be zero if you have a balance")

    if credit_card_spending > total_credit_limit:
        st.error("❌ Limit exceeded! Please check the value.")

# ---------------------------------------------------------------------------
# CALCULATIONS
# ---------------------------------------------------------------------------

analysis_run = False

if st.sidebar.button("🚀 Run Financial Analysis", type="primary", use_container_width=True):

    if credit_card_spending > total_credit_limit:
        st.error("❌ Cannot run analysis: Credit card balance exceeds limit.")
    else:
        with st.spinner("Analyzing your financial data..."):

            results = run_financial_analysis(
                monthly_income, monthly_expenses, current_savings,
                monthly_debt_payments, total_debt,
                credit_card_spending, total_credit_limit
            )

            savings_rate = results["savings_rate"]
            debt_to_income = results["debt_to_income_ratio"]
            credit_utilization = results["credit_utilization"]
            emergency_fund_ratio = results["emergency_fund_ratio"]
            health_score = results["health_score"]
            risk_category = results["risk_category"]
            risk_emoji = results["risk_emoji"]
            recommendations = results["recommendations"]
            disposable_income = results["disposable_income"]
            net_income = results["net_income"]

            # Remaining Purse (salary-based)
            remaining_purse = net_income

            # Remaining Monthly Purse (after all spending)
            remaining_monthly_purse = monthly_income - (
                monthly_expenses + monthly_debt_payments + credit_card_spending
            )

            analysis_run = True

# ---------------------------------------------------------------------------
# SIDEBAR RESULT
# ---------------------------------------------------------------------------

with st.sidebar:
    if analysis_run:
        st.markdown("---")
        st.subheader("💰 Remaining Monthly Purse")

        if remaining_monthly_purse > 0:
            st.success(f"${remaining_monthly_purse:,.0f} (Available)")
        elif remaining_monthly_purse == 0:
            st.warning("₹0 (No money left)")
        else:
            st.error(f"-${abs(remaining_monthly_purse):,.0f} (Overspending!)")

# ---------------------------------------------------------------------------
# DISPLAY RESULTS
# ---------------------------------------------------------------------------

if analysis_run:

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Health Score", f"{health_score:.1f}/100")
        st.subheader(f"{risk_emoji} {risk_category}")

    with col2:
        st.metric("Savings Rate", f"{savings_rate:.1f}%")
        st.metric("Debt-to-Income", f"{debt_to_income:.1f}%")

    with col3:
        st.metric("Credit Utilization", f"{credit_utilization:.1f}%")
        st.metric("Emergency Fund", f"{emergency_fund_ratio:.1f} months")

    st.divider()

    # Chart
    st.subheader("📈 Financial Overview")
    chart = create_financial_overview_chart(
        monthly_income, monthly_expenses, current_savings, monthly_debt_payments
    )
    st.plotly_chart(chart, use_container_width=True)

    # Cash Flow
    st.subheader("📊 Cash Flow")

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"• Savings Rate: {savings_rate:.1f}%")
        st.write(f"• Debt-to-Income: {debt_to_income:.1f}%")

    with col2:
        st.write(f"• Disposable Income: ${disposable_income:,.0f}")
        st.write(f"• Net Income: ${net_income:,.0f}")
        st.write(f"• Remaining Purse: ${remaining_purse:,.0f}")
        st.write(f"• Remaining Monthly Purse: ${remaining_monthly_purse:,.0f}")

    # Recommendations
    st.subheader("🎯 Recommendations")
    for rec in recommendations:
        st.write(rec)

    # -----------------------------------------------------------------------
    # FINANCIAL SUMMARY TABLE
    # -----------------------------------------------------------------------

    st.subheader("📋 Financial Summary")

    summary_data = {
        "Metric": [
            "Monthly Income", "Monthly Expenses", "Monthly Debt Payments",
            "Credit Card Balance", "Credit Card Limit", "Current Savings",
            "Remaining Purse", "Remaining Monthly Purse",
            "Savings Rate", "Debt-to-Income Ratio",
            "Credit Utilization", "Health Score"
        ],
        "Value": [
            f"${monthly_income:,.0f}",
            f"${monthly_expenses:,.0f}",
            f"${monthly_debt_payments:,.0f}",
            f"${credit_card_spending:,.0f}",
            f"${total_credit_limit:,.0f}",
            f"${current_savings:,.0f}",
            f"${remaining_purse:,.0f}",
            f"${remaining_monthly_purse:,.0f}",
            f"{savings_rate:.1f}%",
            f"{debt_to_income:.1f}%",
            f"{credit_utilization:.1f}%",
            f"{health_score:.1f}/100"
        ],
        "Status": [
            "✅" if monthly_income > 0 else "❌",
            "✅" if monthly_expenses < monthly_income else "❌",
            "✅" if monthly_debt_payments < monthly_income else "⚠️",
            "✅" if credit_card_spending <= total_credit_limit else "❌",
            "✅" if total_credit_limit > 0 else "❌",
            "✅" if current_savings > 0 else "❌",
            "✅" if remaining_purse > 0 else "⚠️",
            "✅" if remaining_monthly_purse > 0 else "⚠️",
            "✅" if savings_rate >= 20 else "⚠️",
            "✅" if debt_to_income <= 36 else "⚠️",
            "✅" if credit_utilization <= 30 else "⚠️",
            "⭐" if health_score > 70 else "⚠️"
        ]
    }

    st.table(pd.DataFrame(summary_data))    