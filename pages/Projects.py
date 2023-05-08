import streamlit as st

if not st.session_state.is_logged_in:
    st.write("Please Log in")
else:
    st.title("Projects")
    # st.write("You have entered: ", st.session_state["my_input"])