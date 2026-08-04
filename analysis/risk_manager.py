"""
Risk Manager
Version 1.0
"""


class RiskManager:

    def calculate(
        self,
        ai_score,
        confidence,
        risk,
    ):

        # Base Position Size

        if ai_score >= 80:
            position = 10

        elif ai_score >= 65:
            position = 5

        elif ai_score >= 45:
            position = 2

        else:
            position = 0

        # Confidence Adjustment

        if confidence < 50:
            position *= 0.5

        # Risk Adjustment

        if risk == "HIGH":
            position *= 0.5

        elif risk == "LOW":
            position *= 1.2

        position = round(position, 2)

        return {

            "position_size": position,

            "max_open_trades": 3,

            "max_portfolio_risk": 20,

            "stop_loss_percent": 3,

            "take_profit_percent": 10,

        }