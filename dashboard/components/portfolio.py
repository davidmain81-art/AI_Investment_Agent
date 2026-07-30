import streamlit as st


def render_portfolio(ctx):

    portfolio = ctx["portfolio"]

    st.subheader("💼 AI Portfolio Allocation")

    capital = st.number_input(

        "Investment Capital",

        value=1_000_000_000,

        step=100_000_000,

    )

    for item in portfolio:

        amount = capital * item["allocation"] / 100

        st.progress(item["allocation"] / 100)

        col1, col2 = st.columns([2, 1])

        with col1:

            st.metric(

                item["market"],

                f'{item["allocation"]}%',

                f'Confidence {item["confidence"]}%',

            )

        with col2:

            st.write("Suggested")

            st.write(f"{amount:,.0f}")

            st.caption(

                f"Final Score: {item['final_score']}"

            )

    # ---------- خارج از حلقه ----------

    st.divider()

    st.success(

        f"Total Capital: {capital:,.0f}"

    )

    best = max(

        portfolio,

        key=lambda x: x["allocation"]

    )

    st.info(

        f"AI suggests focusing on {best['market']} "

        f"({best['allocation']}%)"

    )