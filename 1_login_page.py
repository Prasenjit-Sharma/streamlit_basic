# streamlit_app.py

import streamlit as st

from st_pages import show_pages, add_page_title, hide_pages, Page, Section

st.set_page_config(
    page_title="Login Page",
    page_icon="🧾",
    layout="wide",
    initial_sidebar_state="collapsed"
)
add_page_title()
if "is_logged_in" not in st.session_state:
    st.session_state["is_logged_in"] = False
    hide_pages(["Projects"])

col1, col2 = st.columns(2)
with col1:
    st.image(
    "https://i1.wp.com/hrnxt.com/wp-content/uploads/2021/07/Hindustan-Petroleum.jpg?resize=580%2C239&ssl=1",
      # Manually Adjust the width of the image as per requirement
)


def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
                st.session_state["username"] in st.secrets["passwords"]
                and st.session_state["password"]
                == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        with col2:
            # First run, show inputs for username + password.
            st.text_input("Username", on_change=password_entered, key="username")
            st.text_input(
                "Password", type="password", on_change=password_entered, key="password"
            )
            return False
    elif not st.session_state["password_correct"]:
        with col2:
            # Password not correct, show input + error.
            st.text_input("Username", on_change=password_entered, key="username")
            st.text_input(
                "Password", type="password", on_change=password_entered, key="password"
            )
            st.error("😕 User not known or password incorrect")
            return False
    else:
        # Password correct.
        return True


if check_password():
    st.session_state.is_logged_in = True
    st.session_state.sidebar_state = 'expanded'
    st.write("Here goes your normal Streamlit app...")
    st.button("Click me")
else:
    st.session_state.sidebar_state = 'collapsed'


# if not st.session_state:
#     hide_pages(["Projects"])
if st.session_state.is_logged_in:
    show_pages(
        [
            Page("1_login_page.py", "Account"),
            Page("pages/Projects.py", "Projects", "✏️"),
            # Can use :<icon-name>: or the actual icon
            #
            # Section(name="Cool apps", icon=":pig:"),

        ]
    )
else:
    show_pages(
        [
            Page("1_login_page.py", "Log In"),
        ]
    )



