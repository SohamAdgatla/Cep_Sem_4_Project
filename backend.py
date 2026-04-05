import numpy as np
from typing import Dict, List, Union


def calculate_savings_rate(monthly_income: float, monthly_expenses: float) -> float:
    """Calculate the savings rate as a percentage."""
    if monthly_income <= 0:
        return 0.0
    return max(0.0, ((monthly_income - monthly_expenses) / monthly_income) * 100.0)


def calculate_debt_to_income_ratio(monthly_debt_payments: float, monthly_income: float) -> float:
    """Calculate the debt-to-income ratio as a percentage."""
    if monthly_income <= 0:
        return float('inf')
    return (monthly_debt_payments / monthly_income) * 100.0


def calculate_credit_utilization(credit_card_spending: float, total_credit_limit: float) -> float:
    """Calculate credit utilization as a percentage."""
    if total_credit_limit <= 0:
        return 100.0
    return min(100.0, max(0.0, (credit_card_spending / total_credit_limit) * 100.0))


def calculate_emergency_fund_ratio(current_savings: float, monthly_expenses: float) -> float:
    """Calculate emergency fund coverage in months."""
    if monthly_expenses <= 0:
        return float('inf')
    return current_savings / monthly_expenses


def calculate_debt_to_asset_ratio(total_debt: float, current_savings: float) -> float:
    """Calculate debt-to-asset ratio as a percentage."""
    total_assets = total_debt + current_savings
    if total_assets <= 0:
        return 100.0
    return (total_debt / total_assets) * 100.0


def calculate_financial_health_score(savings_rate: float, debt_to_income_ratio: float,
                                     credit_utilization: float, emergency_fund_ratio: float,
                                     debt_to_asset_ratio: float) -> float:
    """Calculate a weighted composite financial health score."""
    sr_score = min(100.0, max(0.0, savings_rate * 2.0))
    dti_score = max(0.0, 100.0 - (debt_to_income_ratio - 36.0) * 2.0)
    cu_score = max(0.0, 100.0 - (credit_utilization - 30.0) * 2.0)
    ef_score = min(100.0, emergency_fund_ratio * 20.0)
    dar_score = max(0.0, 100.0 - debt_to_asset_ratio)
    return min(100.0, max(0.0, (sr_score * 0.30) + (dti_score * 0.25) + (cu_score * 0.20) + (ef_score * 0.15) + (dar_score * 0.10)))


def get_risk_category(score: float) -> tuple[str, str]:
    """Map the health score to a risk category and emoji."""
    thresholds = np.array([35.0, 50.0, 65.0, 80.0])
    categories = np.array(["Critical", "Poor", "Fair", "Good", "Excellent"], dtype=object)
    emojis = np.array(["🔴", "🔴", "🟠", "🟡", "🟢"], dtype=object)
    return categories[np.searchsorted(thresholds, score, side="right")], emojis[np.searchsorted(thresholds, score, side="right")]


def get_recommendations(savings_rate: float, debt_to_income_ratio: float,
                       credit_utilization: float, emergency_fund_ratio: float,
                       debt_to_asset_ratio: float) -> list[str]:
    """Generate recommendation messages based on formula-driven gaps."""
    gaps = np.array([
        max(0.0, 20.0 - savings_rate),
        max(0.0, debt_to_income_ratio - 36.0),
        max(0.0, credit_utilization - 30.0),
        max(0.0, 3.0 - emergency_fund_ratio),
        max(0.0, debt_to_asset_ratio - 50.0),
    ])
    messages = np.array([
        "💰 Increase your savings rate to reach 20% of income.",
        "💳 Lower your debt-to-income ratio below 36%.",
        "💳 Reduce credit utilization to stay under 30%.",
        "🛡️ Build at least 3 months of emergency savings.",
        "📊 Lower debt versus savings to improve stability.",
    ], dtype=object)
    selected = [msg for msg, gap in zip(messages, gaps) if gap > 0.0]
    return selected or ["✅ Your finances look good. Maintain these formula-based habits."]


def run_financial_analysis(monthly_income: float, monthly_expenses: float,
                           current_savings: float, monthly_debt_payments: float,
                           total_debt: float, credit_card_spending: float,
                           total_credit_limit: float) -> Dict[str, Union[float, str, List[str]]]:
    """Run all backend calculations and return the results."""
    savings_rate = calculate_savings_rate(monthly_income, monthly_expenses)
    debt_to_income_ratio = calculate_debt_to_income_ratio(monthly_debt_payments, monthly_income)
    credit_utilization = calculate_credit_utilization(credit_card_spending, total_credit_limit)
    emergency_fund_ratio = calculate_emergency_fund_ratio(current_savings, monthly_expenses)
    debt_to_asset_ratio = calculate_debt_to_asset_ratio(total_debt, current_savings)
    health_score = calculate_financial_health_score(
        savings_rate, debt_to_income_ratio, credit_utilization,
        emergency_fund_ratio, debt_to_asset_ratio
    )
    risk_category, risk_emoji = get_risk_category(health_score)
    recommendations = get_recommendations(
        savings_rate, debt_to_income_ratio, credit_utilization,
        emergency_fund_ratio, debt_to_asset_ratio
    )
    disposable_income = monthly_income - monthly_expenses
    net_income = disposable_income - monthly_debt_payments
    return {
        "savings_rate": savings_rate,
        "debt_to_income_ratio": debt_to_income_ratio,
        "credit_utilization": credit_utilization,
        "emergency_fund_ratio": emergency_fund_ratio,
        "debt_to_asset_ratio": debt_to_asset_ratio,
        "health_score": health_score,
        "risk_category": risk_category,
        "risk_emoji": risk_emoji,
        "recommendations": recommendations,
        "disposable_income": disposable_income,
        "net_income": net_income,
    }