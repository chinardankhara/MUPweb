import streamlit as st
import streamlit_option_menu as som
#tab UI
st.set_page_config(page_title="MUP", page_icon="bar-chart")

#navigation bar

options_list = ['Home', 'For School Counselors', 'For Recruiters',
 'For Funding Agencies', 'Just here to Explore?']
icons_list = ['house-fill', 'person-fill', 'briefcase-fill', 'currency-dollar', 'circle-fill']
selected = som.option_menu(menu_title = None, options = options_list, orientation = 'horizontal', icons = icons_list)

def display_home():
    st.markdown("<h1 style='text-align: center; color: black;'>Welcome to MUP dashboards</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: black;'>A tool to help you measure relevant university metrics for your use case.</h3>", unsafe_allow_html=True)


if selected == "Home":
    display_home()
elif selected == "For School Counselors":
    pass
elif selected == "For Recruiters":
    pass
elif selected == "For Funding Agencies":
    pass
elif selected == "Just here to Explore?":
    pass

hide_menu_style = """<style> footer {visibility: hidden;} </style> """
st.markdown(hide_menu_style, unsafe_allow_html=True)

