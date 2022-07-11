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

def display_recruiter_page():
    #get the select box set up
    with open('Institution List.csv') as f:
        reader = csv.reader(f)
        options_list = [i[1] for i in list(reader)]
    institution_select = st.multiselect("Select colleges to view", options = options_list, 
    help = "For best results, select 2-3 colleges")

    #create the total research plot
    research_figure = go.Figure()
    research_data = pd.read_excel('recruiter_data/total_research.xlsx')
    for i in institution_select:
        series = research_data.loc[research_data['Institution'] == i]
        series = series.T.iloc[4:][::-1]
        series.reset_index(inplace = True)
        series.columns = ['Year', 'Total Research']
        series['Total Research'] = series['Total Research'].apply(lambda x: x*1000)
        series['Year'] = series['Year'].apply(lambda x: int(x[:4]))
        research_figure.add_trace(go.Scatter(x = series['Year'], y = series['Total Research'],
        name = i, mode = 'lines'))
    research_figure.update_layout(height = 600, width = 900, legend_orientation = 'h', xaxis_title = 'Year',
     yaxis_title = 'Expenditure (in USD)', legend_title = 'Institution Key', font = dict(family='Serif'))

    #create the annual giving plot
    giving_figure = go.Figure()
    giving_data = pd.read_excel('recruiter_data/giving.xlsx')
    for i in institution_select:
        series = giving_data.loc[giving_data['Institution'] == i]
        series = series.T.iloc[4:][::-1]
        series.reset_index(inplace = True)
        series.columns = ['Year', 'Giving']
        series['Giving'] = series['Giving'].apply(lambda x: x*1000)
        series['Year'] = series['Year'].apply(lambda x: int(x[:4]))
        giving_figure.add_trace(go.Scatter(x = series['Year'], y = series['Giving'],
        name = i, mode = 'lines'))
    giving_figure.update_layout(height = 600, width = 900, legend_orientation = 'h', xaxis_title = 'Year',
        yaxis_title = 'Annual Giving (in USD)', legend_title = 'Institution Key', font = dict(family='Serif'))

    #create the doctorates plot
    doctorates_figure = go.Figure()
    doctorates_data = pd.read_excel('recruiter_data/doctorates.xlsx')
    for i in institution_select:
        series = doctorates_data.loc[doctorates_data['Institution'] == i]
        series = series.T.iloc[4:][::-1]
        series.reset_index(inplace = True)
        series.columns = ['Year', 'Doctorates']
        series['Year'] = series['Year'].apply(lambda x: int(x[:4]))
        doctorates_figure.add_trace(go.Scatter(x = series['Year'], y = series['Doctorates'],
        name = i, mode = 'lines'))
    doctorates_figure.update_layout(height = 600, width = 900, legend_orientation = 'h', xaxis_title = 'Year',
        yaxis_title = 'Annual Doctorates', legend_title = 'Institution Key', font = dict(family='Serif'))
    
    #create the headcount plot
    headcount_figure = go.Figure()
    headcount_data = pd.read_excel('recruiter_data/headcount.xlsx')
    for i in institution_select:
        series = headcount_data.loc[headcount_data['Institution'] == i]
        series = series.T.iloc[4:][::-1]
        series.reset_index(inplace = True)
        series.columns = ['Year', 'Headcount']
        series['Year'] = series['Year'].apply(lambda x: int(x[:4]))
        headcount_figure.add_trace(go.Scatter(x = series['Year'], y = series['Headcount'],
        name = i, mode = 'lines'))
    headcount_figure.update_layout(height = 600, width = 900, legend_orientation = 'h', xaxis_title = 'Year',
        yaxis_title = 'Headcount', legend_title = 'Institution Key', font = dict(family='Serif'))
    
    #create the faculty awards plot
    awards_figure = go.Figure()
    awards_data = pd.read_excel('recruiter_data/faculty_awards.xlsx')
    for i in institution_select:
        series = awards_data.loc[awards_data['Institution'] == i]
        series = series.T.iloc[4:][::-1]
        series.reset_index(inplace = True)
        series.columns = ['Year', 'Awards']
        series['Year'] = series['Year'].apply(lambda x: int(x[:4]))
        awards_figure.add_trace(go.Scatter(x = series['Year'], y = series['Awards'],
        name = i, mode = 'lines'))
    awards_figure.update_layout(height = 600, width = 900, legend_orientation = 'h', xaxis_title = 'Year',
        yaxis_title = 'Total Awards', legend_title = 'Institution Key', font = dict(family='Serif'))
    
    #create the national academy plot
    academy_figure = go.Figure()
    academy_data = pd.read_excel('recruiter_data/national_academy.xlsx')
    for i in institution_select:
        series = academy_data.loc[academy_data['Institution'] == i]
        series = series.T.iloc[5:][::-1]
        series.reset_index(inplace = True)
        series.columns = ['Year', 'Academy']
        series['Year'] = series['Year'].apply(lambda x: int(x[:4]))
        academy_figure.add_trace(go.Scatter(x = series['Year'], y = series['Academy'],
        name = i, mode = 'lines'))
    academy_figure.update_layout(height = 600, width = 900, legend_orientation = 'h', xaxis_title = 'Year',
        yaxis_title = 'Number of members', legend_title = 'Institution Key', font = dict(family='Serif'))

    #write the funding and research data to page
    st.write("<h2 style='text-align: center; color: black;'>Funding and Research Data</h2>", unsafe_allow_html=True)
    st.write("##")
    col1, col2 = st.columns(2)
    with col1:
        st.write("<h4 style='text-align: center; color: black;'>Total Research Expenditure (in USD)</h4>", unsafe_allow_html=True)
        st.plotly_chart(research_figure, use_container_width=True)
    with col2:
        st.write("<h4 style='text-align: center; color: black;'>Annual Donations (in USD)</h4>", unsafe_allow_html=True)
        st.plotly_chart(giving_figure, use_container_width=True)

    #write the doctorates and headcount data to page
    st.write("###")
    st.write("<h2 style='text-align: center; color: black;'>Student and Research Data</h2>", unsafe_allow_html=True)
    st.write("##")
    col3, col4 = st.columns(2)
    with col3:
        st.write("<h4 style='text-align: center; color: black;'>Annual Doctorates Graduated</h4>", unsafe_allow_html=True)
        st.plotly_chart(doctorates_figure, use_container_width=True)
    with col4:
        st.write("<h4 style='text-align: center; color: black;'>Total Student Headcount</h4>", unsafe_allow_html=True)
        st.plotly_chart(headcount_figure, use_container_width=True)
    
    #write the awards and academy data to page
    st.write("###")
    st.write("<h2 style='text-align: center; color: black;'>Awards and Prestige</h2>", unsafe_allow_html=True)
    st.write("##")
    col5, col6 = st.columns(2)
    with col5:
        st.write("<h4 style='text-align: center; color: black;'>National Academy Memberss</h4>", unsafe_allow_html=True)
        st.plotly_chart(awards_figure, use_container_width=True)
    with col6:
        st.write("<h4 style='text-align: center; color: black;'>Annual Faculty Awards</h4>", unsafe_allow_html=True)
        st.plotly_chart(academy_figure, use_container_width=True)



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

