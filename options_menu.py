import streamlit as st
# from options_menu import st_options_menu
from streamlit_option_menu import option_menu

def main():
    st.set_page_config(page_title='Data Analysis', page_icon=':bar_chart:', layout='wide')

    # create top navigation bar
    menu_items = {
        "Page 1": {
            "Subpage 1.1": "/page1/subpage1",
            "Subpage 1.2": "/page1/subpage2",
            "Subpage 1.3": "/page1/subpage3",
            "Subpage 1.4": "/page1/subpage4",
        },
        "Page 2": {
            "Subpage 2.1": "/page2/subpage1",
            "Subpage 2.2": "/page2/subpage2",
            "Subpage 2.3": "/page2/subpage3",
            "Subpage 2.4": "/page2/subpage4",
        },
        "Page 3": {
            "Subpage 3.1": "/page3/subpage1",
            "Subpage 3.2": "/page3/subpage2",
            "Subpage 3.3": "/page3/subpage3",
            "Subpage 3.4": "/page3/subpage4",
        },
    }

    # selected_menu_items = st_options_menu(menu_items)
    selected_menu_items = option_menu("Home", options=menu_items)
    # display selected menu item
    st.write("You selected:", selected_menu_items)

if __name__ == '__main__':
    main()
