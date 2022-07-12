import streamlit as st
import streamlit_option_menu as som
import plotly.graph_objects as go
import csv 
import pandas as pd

#tab UI
st.set_page_config(page_title="MUP", page_icon="bar-chart", layout = 'wide')

#navigation bar
options_list = ['Home', 'For School Counselors', 'For Recruiters',
 'For Funding Agencies', 'Just here to Explore?']
icons_list = ['house-fill', 'person-fill', 'briefcase-fill', 'currency-dollar', 'circle-fill']
selected = som.option_menu(menu_title = None, options = options_list, orientation = 'horizontal', icons = icons_list)

#function for home page content
def display_home():
    st.markdown("<h1 style='text-align: center; color: black;'>Welcome to MUP dashboards</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: black;'>A tool to help you measure relevant university metrics for your use case.</h3>", unsafe_allow_html=True)

#function for recruiter page content
def display_recruiter_page():
    #get the select box set up
    with open('Institution List.csv') as f:
        reader = csv.reader(f)
        options_list = [i[1] for i in list(reader)]
    institution_select = st.multiselect("Select colleges to view", options = options_list, 
    help = "For best results, select 2-3 colleges")

    """
    @params
    input_file_path: file path of the excel input data file
    type: string
    figure_details: plotly figure details in this order: legend_orientation, x_axis_title, y_axis_title, legend_title
    type: list
    apply_multiplier: multiplier to apply to the y-axis values. Default is 1.
    type: int
    @returns
    plotly figure line chart with a Scatter object trace
    """
    def plot_helper(input_file_path, figure_details, apply_multiplier = 1):
        df = pd.read_excel(input_file_path)
        figure = go.Figure()
        for i in institution_select:
            series = df.loc[df['Institution'] == i]
            if input_file_path == 'recruiter_data/national_academy.xlsx':
                series = series.T.iloc[5:][::-1]
            else:
                series = series.T.iloc[4:][::-1]
            series.reset_index(inplace = True)
            series.columns = ['Year', 'dummy']
            series['dummy'] = series['dummy'].apply(lambda x: x * apply_multiplier)
            series['Year'] = series['Year'].apply(lambda x: int(x[:4]))
            figure.add_trace(go.Scatter(x = series['Year'], y = series['dummy'], name = i, mode = 'lines'))
        figure.update_layout(height = 600, width = 900, legend_orientation = 'h', xaxis_title = figure_details[0],
         yaxis_title = figure_details[1], legend_title = figure_details[2], font = dict(family = 'Serif'))
        return figure

    research_figure = plot_helper('recruiter_data/total_research.xlsx', ['Year', 'Expenditure (in USD)', 'Institution Key'], 1000)
    giving_figure = plot_helper('recruiter_data/giving.xlsx', ['Year', 'Annual Giving (in USD)', 'Institution Key'], 1000)
    doctorates_figure = plot_helper('recruiter_data/doctorates.xlsx', ['Year', 'Annual Doctorates', 'Institution Key'])
    headcount_figure = plot_helper('recruiter_data/headcount.xlsx', ['Year', 'Headcount', 'Institution Key'])
    awards_figure = plot_helper('recruiter_data/faculty_awards.xlsx', ['Year', 'Total Awards', 'Institution Key'])
    academy_figure = plot_helper('recruiter_data/national_academy.xlsx', ['Year', 'Number of members', 'Institution Key'])
    
    """
    @params
    title_string: title of the page section
    type: string
    figure_list: list of plotly figures to display
    type: list
    figure_titles: list of titles for the figures
    type: list
    @returns
    None
    """
    def write_content(title_string, figure_list, figure_titles):
        st.write("<h2 style='text-align: center; color: black;'>" + title_string + "</h2>", unsafe_allow_html=True)
        st.write("##")
        x, y = st.columns(2)
        with x:
            st.write("<h4 style='text-align: center; color: black;'>" + figure_titles[0] + "</h4>", unsafe_allow_html=True)
            st.plotly_chart(figure_list[0], use_container_width=True)
        with y:
            st.write("<h4 style='text-align: center; color: black;'>" + figure_titles[1] + "</h4>", unsafe_allow_html=True)
            st.plotly_chart(figure_list[1], use_container_width=True)
    
    write_content("Funding and Research Data", [research_figure, giving_figure],
     ["Total Research Expenditure (in USD)", "Annual Donations (in USD)"])
    write_content("Student and Research Data", [doctorates_figure, headcount_figure],
     ["Annual Doctorates Graduate", "Total Student Headcount"])
    write_content("Awards and Prestige", [awards_figure, academy_figure],
     ["National Academy Members", "Annual Faculty Awards"])

if selected == "Home":
    display_home()
elif selected == "For School Counselors":
    pass
elif selected == "For Recruiters":
    display_recruiter_page()
elif selected == "For Funding Agencies":
    pass
elif selected == "Just here to Explore?":
    pass

#hide the "made with streamlit" footer
hide_menu_style = """<style> footer {visibility: hidden;} </style> """
st.markdown(hide_menu_style, unsafe_allow_html=True)
