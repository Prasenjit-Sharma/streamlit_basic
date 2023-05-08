import streamlit as st
from streamlit_option_menu import option_menu


# Define the login function
def login():
    # Set the page title and image
    st.set_page_config(page_title="Data Analysis Website", page_icon=":bar_chart:")
    st.image("https://example.com/logo.png", width=200)

    # Display the login form
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "password":

            # Display the navigation bar if login is successful
            st.write("Login successful!")
            # Define the navigation bar
            menu = ["Home", "Data Analysis", "Settings"]
            choice = option_menu("Select an option", menu)
            # Define the dropdown menus
            if choice == "Home":
                st.write("Welcome to the home page!")
            elif choice == "Data Analysis":
                analysis_menu = ["Overview", "Trends", "Insights", "Forecast"]
                analysis_choice = option_menu("Select an option", analysis_menu)
                if analysis_choice == "Overview":
                    st.write("This is the data analysis overview page.")
                elif analysis_choice == "Trends":
                    st.write("This is the data analysis trends page.")
                elif analysis_choice == "Insights":
                    st.write("This is the data analysis insights page.")
                elif analysis_choice == "Forecast":
                    st.write("This is the data analysis forecast page.")
            elif choice == "Settings":
                settings_menu = ["Profile", "Notifications", "Preferences", "Logout"]
                settings_choice = option_menu("Select an option", settings_menu)
                if settings_choice == "Profile":
                    st.write("This is the profile settings page.")
                elif settings_choice == "Notifications":
                    st.write("This is the notifications settings page.")
                elif settings_choice == "Preferences":
                    st.write("This is the preferences settings page.")
                elif settings_choice == "Logout":
                    st.write("You have been logged out.")
            st.experimental_rerun()
        else:
            # Display an error message if login is unsuccessful
            st.error("Incorrect username or password. Please try again.")


# Run the login function
login()
