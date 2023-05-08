import streamlit as st
from streamlit.report_thread import get_report_ctx
from streamlit.hashing import _CodeHasher
from SessionState import get_state as get_session

# define the login page
def login():
    # get the current session state
    session_state = get_session()

    # create input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # create login button
    if st.button("Login"):
        if username == "your_username" and password == "your_password":
            st.success("Logged in as {}".format(username))

            # set session state to redirect to the new page
            session_state.redirect = True
        else:
            st.error("Invalid username or password")

# define the new page
def new_page():
    st.write("Welcome to the new page!")

# main function
def main():
    # create session state
    session_state = get_session()

    # check if redirect is needed
    if hasattr(session_state, "redirect") and session_state.redirect:
        # clear the redirect flag
        session_state.redirect = False

        # redirect to the new page
        new_page()
    else:
        # display the login page
        login()

# run the app
if __name__ == "__main__":
    main()
