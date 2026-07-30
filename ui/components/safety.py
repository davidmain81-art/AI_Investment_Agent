import streamlit as st


def safety_panel(safety):

    st.subheader("🛡️ EXECUTION SAFETY")


    if safety["allowed"]:

        st.success(
            safety["status"]
        )


    else:

        st.error(
            safety["status"]
        )


        if safety["reasons"]:

            st.write("Reasons:")

            for reason in safety["reasons"]:

                st.write(
                    f"• {reason}"
                )