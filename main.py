# Personal Finance Health Analyzer
# Formula-based financial assessment with calculation formulas and simple rules.

import sys

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from backend import run_financial_analysis

# ---------------------------------------------------------------------------
# Streamlit page configuration
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="Personal Finance Health Analyzer",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Personal Finance Health Analyzer")
st.markdown("*Formula-based financial assessment using proven algorithms*")

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def create_financial_overview_chart(monthly_income: float, monthly_expenses: float,
                                  current_savings: float, monthly_debt_payments: float) -> go.Figure:
    """
    Algorithm: Financial Flow Visualization
    Creates a waterfall chart showing income flow through expenses and debt

    Data Flow:
    1. Gross Income
    2. After Expenses (Gross Income - Monthly Expenses)
    3. After Debt Payments (After Expenses - Monthly Debt Payments)
    4. Current Savings (overlay line)
    """
    disposable_income = monthly_income - monthly_expenses
    net_income = disposable_income - monthly_debt_payments

    fig = go.Figure()

    # Income breakdown bars
    fig.add_trace(go.Bar(
        name='Income Flow',
        x=['Gross Income', 'After Expenses', 'After Debt Payments'],
        y=[monthly_income, disposable_income, net_income],
        marker_color=['#2d5a87', '#68d391', '#38a169'],
        text=[f"${v:,.0f}" for v in [monthly_income, disposable_income, net_income]],
        textposition="outside",
        hovertemplate="Amount: $%{y:,.0f}<extra></extra>"
    ))

    # Savings overlay line
    fig.add_trace(go.Scatter(
        name='Current Savings',
        x=['Gross Income', 'After Expenses', 'After Debt Payments'],
        y=[current_savings, current_savings, current_savings],
        mode='lines+markers',
        line=dict(color='#e53e3e', width=3),
        marker=dict(size=8),
        hovertemplate="Savings: $%{y:,.0f}<extra></extra>"
    ))

    fig.update_layout(
        title='💰 Financial Flow Analysis<br><sup>Shows how your income flows through expenses and debt payments</sup>',
        xaxis_title='Cash Flow Stages',
        yaxis_title='Amount ($)',
        yaxis_tickprefix='$',
        template='plotly_white',
        height=400,
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        )
    )

    return fig

# ---------------------------------------------------------------------------
# Main UI Code
# ---------------------------------------------------------------------------

# ============================================================================
# SIDEBAR INPUTS
# ============================================================================

with st.sidebar:
    st.header("📊 Financial Data Input")

    st.markdown("**Enter your monthly financial details:**")

    monthly_income = st.number_input(
        "Monthly Income ($)",
        min_value=0.0,
        value=5000.0,
        step=100.0,
        help="Your total monthly income before taxes and deductions",
        format="%.2f"
    )

    monthly_expenses = st.number_input(
        "Monthly Expenses ($)",
        min_value=0.0,
        value=3500.0,
        step=50.0,
        help="Total monthly spending on necessities, bills, and discretionary items",
        format="%.2f"
    )

    current_savings = st.number_input(
        "Current Savings ($)",
        min_value=0.0,
        value=15000.0,
        step=500.0,
        help="Total savings, emergency funds, and liquid assets",
        format="%.2f"
    )

    monthly_debt_payments = st.number_input(
        "Monthly Debt Payments ($)",
        min_value=0.0,
        value=800.0,
        step=50.0,
        help="Monthly payments for loans, credit cards, and other debts",
        format="%.2f"
    )

    total_debt = st.number_input(
        "Total Debt ($)",
        min_value=0.0,
        value=25000.0,
        step=500.0,
        help="Total outstanding debt across all accounts",
        format="%.2f"
    )

    credit_card_spending = st.number_input(
        "Credit Card Balance ($)",
        min_value=0.0,
        value=2000.0,
        step=100.0,
        help="Current balance on all credit cards",
        format="%.2f"
    )

    total_credit_limit = st.number_input(
        "Credit Card Limit ($)",
        min_value=0.0,
        value=5000.0,
        step=500.0,
        help="Total credit limit across all credit cards",
        format="%.2f"
    )

    # Input validation
    if total_credit_limit == 0 and credit_card_spending > 0:
        st.warning("⚠️ Credit card limit cannot be zero if you have a balance")

# ============================================================================
# CALCULATIONS USING BACKEND
# ============================================================================

# Initialize variables
savings_rate = debt_to_income = credit_utilization = emergency_fund_ratio = 0.0
debt_to_asset_ratio = health_score = disposable_income = net_income = 0.0
risk_category = risk_emoji = ""
recommendations = []

# Run button to trigger analysis
if st.sidebar.button("🚀 Run Financial Analysis", type="primary", use_container_width=True):
    with st.spinner("Analyzing your financial data..."):
        results = run_financial_analysis(
            monthly_income, monthly_expenses, current_savings,
            monthly_debt_payments, total_debt, credit_card_spending, total_credit_limit
        )

        # Extract results
        savings_rate = results["savings_rate"]
        debt_to_income = results["debt_to_income_ratio"]
        credit_utilization = results["credit_utilization"]
        emergency_fund_ratio = results["emergency_fund_ratio"]
        debt_to_asset_ratio = results["debt_to_asset_ratio"]
        health_score = results["health_score"]
        risk_category = results["risk_category"]
        risk_emoji = results["risk_emoji"]
        recommendations = results["recommendations"]
        disposable_income = results["disposable_income"]
        net_income = results["net_income"]

        analysis_run = True
else:
    # Show placeholder when analysis not run
    st.info("👆 Enter your financial data in the sidebar and click 'Run Financial Analysis' to see your results.")
    analysis_run = False

# ============================================================================
# DISPLAY RESULTS (only if analysis has been run)
# ============================================================================

if analysis_run:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Financial Health Score", f"{health_score:.1f}/100")
        st.subheader(f"{risk_emoji} {risk_category}")

    with col2:
        st.metric("Savings Rate", f"{savings_rate:.1f}%")
        st.metric("Debt-to-Income Ratio", f"{debt_to_income:.1f}%")

    with col3:
        st.metric("Credit Utilization", f"{credit_utilization:.1f}%")
        st.metric("Emergency Fund (Months)", f"{emergency_fund_ratio:.1f}")

    st.divider()

    # ============================================================================
    # FINANCIAL OVERVIEW CHART
    # ============================================================================

    st.subheader("📈 Financial Overview")
    chart = create_financial_overview_chart(
        monthly_income, monthly_expenses, current_savings, monthly_debt_payments
    )
    st.plotly_chart(chart, use_container_width=True)

    # ============================================================================
    # DETAILED ANALYSIS
    # ============================================================================

    st.subheader("📊 Detailed Financial Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**💰 Key Financial Ratios:**")
        st.write(f"• Savings Rate: {savings_rate:.1f}%")
        st.write(f"• Debt-to-Income Ratio: {debt_to_income:.1f}%")
        st.write(f"• Credit Utilization: {credit_utilization:.1f}%")
        st.write(f"• Emergency Fund Ratio: {emergency_fund_ratio:.1f} months")
        st.write(f"• Debt-to-Asset Ratio: {debt_to_asset_ratio:.1f}%")

    with col2:
        st.markdown("**📈 Cash Flow Analysis:**")
        st.write(f"• Monthly Disposable Income: ${disposable_income:,.0f}")
        st.write(f"• Net Income After Debt: ${net_income:,.0f}")
        st.write(f"• Current Savings: ${current_savings:,.0f}")
        st.write(f"• Total Debt: ${total_debt:,.0f}")

    # ============================================================================
    # RECOMMENDATIONS
    # ============================================================================

    st.subheader("🎯 Personalized Recommendations")
    for rec in recommendations:
        st.write(rec)

    # ============================================================================
    # FORMULA EXPLANATIONS
    # ============================================================================

    with st.expander("📚 How Calculations Work - Formula Details"):
        st.markdown("""
    ### 🔢 Core Financial Formulas Used

    **1. Savings Rate**
    ```
    Formula: SR = ((Monthly Income - Monthly Expenses) / Monthly Income) × 100
    Purpose: Measures percentage of income saved after expenses
    Example: ($5,000 - $3,500) / $5,000 × 100 = 30%
    ```

    **2. Debt-to-Income Ratio**
    ```
    Formula: DTI = (Monthly Debt Payments / Monthly Income) × 100
    Purpose: Measures debt burden relative to income
    Example: $800 / $5,000 × 100 = 16%
    Target: ≤ 36% for healthy finances
    ```

    **3. Credit Utilization**
    ```
    Formula: CU = (Credit Card Balance / Credit Card Limit) × 100
    Purpose: Measures credit card usage vs available credit
    Example: $2,000 / $5,000 × 100 = 40%
    Target: ≤ 30% for good credit health
    ```

    **4. Emergency Fund Ratio**
    ```
    Formula: EF = Current Savings / Monthly Expenses
    Purpose: Measures months of expenses covered by savings
    Example: $15,000 / $3,500 = 4.3 months
    Target: 3-6 months for financial security
    ```

    **5. Debt-to-Asset Ratio**
    ```
    Formula: DAR = (Total Debt / (Total Debt + Current Savings)) × 100
    Purpose: Measures debt burden relative to total assets
    Example: $25,000 / ($25,000 + $15,000) × 100 = 62.5%
    Target: ≤ 50% for balanced position
    ```

    **6. Financial Health Score (Composite Algorithm)**
    ```
    Formula: Score = (SR_score × 0.30) + (DTI_score × 0.25) + (CU_score × 0.20) + (EF_score × 0.15) + (DAR_score × 0.10)

    Component Scores:
    • SR_score = min(100, max(0, Savings Rate × 2))
    • DTI_score = max(0, 100 - (DTI - 36) × 2)
    • CU_score = max(0, 100 - (CU - 30) × 2)
    • EF_score = min(100, Emergency Fund Ratio × 20)
    • DAR_score = max(0, 100 - Debt-to-Asset Ratio)
    ```
    """)

    # ============================================================================
    # SUMMARY TABLE
    # ============================================================================

    st.subheader("📋 Financial Summary")

    summary_data = {
        "Metric": [
            "Monthly Income", "Monthly Expenses", "Monthly Debt Payments",
            "Current Savings", "Total Debt", "Credit Card Balance",
            "Credit Card Limit", "Savings Rate", "Debt-to-Income Ratio",
            "Credit Utilization", "Emergency Fund (Months)", "Health Score"
        ],
        "Value": [
            f"${monthly_income:,.0f}", f"${monthly_expenses:,.0f}", f"${monthly_debt_payments:,.0f}",
            f"${current_savings:,.0f}", f"${total_debt:,.0f}", f"${credit_card_spending:,.0f}",
            f"${total_credit_limit:,.0f}", f"{savings_rate:.1f}%", f"{debt_to_income:.1f}%",
            f"{credit_utilization:.1f}%", f"{emergency_fund_ratio:.1f}", f"{health_score:.1f}/100"
        ],
        "Status": [
            "✅" if monthly_income > 0 else "❌",
            "✅" if monthly_expenses < monthly_income else "❌",
            "✅" if debt_to_income <= 36 else "⚠️",
            "✅" if current_savings > 0 else "❌",
            "✅" if total_debt < current_savings else "⚠️",
            "✅" if credit_utilization <= 30 else "⚠️",
            "✅" if total_credit_limit > 0 else "❌",
            "✅" if savings_rate >= 20 else "⚠️",
            "✅" if debt_to_income <= 36 else "❌",
            "✅" if credit_utilization <= 30 else "⚠️",
            "✅" if emergency_fund_ratio >= 3 else "⚠️",
            f"{risk_emoji}"
        ]
    }

    st.table(pd.DataFrame(summary_data))

    st.markdown("---")
    st.caption("💡 *This analyzer uses industry-standard financial formulas and algorithms to assess your financial health. All calculations are performed in real-time based on your inputs.*")
