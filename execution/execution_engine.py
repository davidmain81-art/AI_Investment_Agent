from execution.paper_trading import PaperTrading


class ExecutionEngine:

    def build_order(

        self,

        asset,

        signal,

        entry,

        risk,

    ):

        if signal == "BUY":

            stop_loss = entry * (
                1
                - risk["stop_loss_percent"] / 100
            )

            take_profit = entry * (
                1
                + risk["take_profit_percent"] / 100
            )

        else:

            stop_loss = entry * (
                1
                + risk["stop_loss_percent"] / 100
            )

            take_profit = entry * (
                1
                - risk["take_profit_percent"] / 100
            )

        order = {

            "asset": asset,

            "signal": signal,

            "entry": entry,

            "position_size":
                risk["position_size"],

            "stop_loss":
                round(stop_loss, 2),

            "take_profit":
                round(take_profit, 2),

            "status":
                "READY",

        }

        return order


    def execute_paper_trade(

        self,

        order,

    ):

        result = PaperTrading().execute(order)

        return result