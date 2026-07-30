import plotly.graph_objects as go


def ai_gauge(score):

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=score,

            title={"text": "AI SCORE"},

            gauge={

                "axis": {"range": [0, 100]},

                "bar": {"color": "#22C55E"},

                "steps": [

                    {"range": [0, 40], "color": "#7F1D1D"},

                    {"range": [40, 70], "color": "#78350F"},

                    {"range": [70, 100], "color": "#14532D"},

                ],

            },

        )

    )

    fig.update_layout(

        height=300,

        paper_bgcolor="#0F172A",

        font={"color": "white"},

    )

    return fig