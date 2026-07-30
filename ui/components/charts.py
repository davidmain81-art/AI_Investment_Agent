import plotly.graph_objects as go


def equity_curve():

    pnl = [0, 2, 4, 3, 5, 8, 7, 9, 12]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            y=pnl,
            mode="lines",
            name="Equity",
            line=dict(
                width=3
            )
        )
    )

    fig.update_layout(

        template="plotly_dark",

        height=350,

        margin=dict(
            l=20,
            r=20,
            t=40,
            b=20
        ),

        title="Equity Curve",

        xaxis_title="Trades",

        yaxis_title="PnL %"

    )

    return fig