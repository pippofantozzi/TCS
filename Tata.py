import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from Performance_Sheet import *


## teste
st.set_page_config(page_title="TCS DeepConsultant", 
                    page_icon=":🧠:",
                    layout="wide")
selected = option_menu( 
    menu_title="TCS Intelligence System",
    options=["TCS DeepConsultant", "How It Works"],
    icons=["capslock","book"],
    menu_icon=["triangle"],
    default_index=0,
    orientation="horizontal"
)

if selected == "TCS DeepConsultant":

    # --- MAINPAGE --- 
    st.title("Welcome to DeepConsultant")
    st.markdown("##")

    form_answers = read()
    company_names = form_answers['Identity:\nWhat is the name of your Company?'].unique()
    company_name = st.selectbox('Which client are we analyzing?:',company_names) 
    most_recent = form_answers.loc[form_answers['Identity:\nWhat is the name of your Company?'] == company_name][-1:]
    #form_answer = st.selectbox('Check if this is the form date input you want to analyze:',dates) 

    st.header(f"{company_name}'s most recent form upload contains the following information:")
    st.write("")
    summary = most_recent['Summary:\n\nBriefly describe what kind of company you are, where you are located, what problem you are facing, and what solution you are looking for']
    st.subheader('🔍Problem Summary:')
    st.table(summary)

    PPP = most_recent['PPP:\nHow much do you value each P in PPP?\n\nAnswer as: Profit-0.4,People-0.2,Planet-0.4\n\nAnswer must add up to 1']
    Profit,People,Planet = str(PPP)[12:15],str(PPP)[23:26],str(PPP)[34:37]
    first, second, third, = st.columns(3)
    with first:
        st.subheader(f'💰Profit: {float(Profit)*100}%')
    with second:
        st.subheader(f'🙇People: {float(People)*100}%')
    with third:
        st.subheader(f'🌎Planet: {float(Planet)*100}%')

    st.write(" ")
    st.subheader("🌐Client Data:")
    st.write(" ")
    first, second, third, fourth, fifth, sixth = st.columns(6)
    with first:
        st.subheader('Profitability:')
        st.table(most_recent['Profitability:\nWhat percentage of your budget is allocated to marketing and advertising?'])
    with second:
        st.subheader('Cost Management:')
        st.table(most_recent['Cost Management:\nDo you utilize data analytics to monitor and control operational costs? (Yes/No)'])
    with third:
        st.subheader('Sustainability Practices:')
        st.table(most_recent['Sustainability Practices:\nHow would you describe your waste management strategy? (Recycling, Reduction, None)'])
    with fourth:
        st.subheader('Environmental Certifications:')
        st.table(most_recent['Environmental Certifications:\nHave you implemented energy-efficient technologies in your operations? (Yes/No)'])
    with fifth:
        st.subheader('Community Engagement:')
        st.table(most_recent['Community Engagement:\nHow many local community events or initiatives did your business participate in during the last year?'])
    with sixth:
        st.subheader('Employee Satisfaction:')
        st.table(most_recent['Employee Satisfaction:\nOn a scale of 1 to 5, how would your employees rate the effectiveness of internal communication?'])

    st.write("")
    first, second, third, fourth = st.columns(4)
    with first:
        st.subheader('Employee Development:')
        st.table(most_recent['Employee Training and Development:\nHow many hours of training per month, on average, do you provide to each employee?'])
    with second:
        st.subheader('Customer Feedback:')
        st.table(most_recent['Customer Feedback and Loyalty Programs:\nDo you use sentiment analysis tools to extract insights from customer feedback? (Yes/No)'])
    with third:
        st.subheader('Customer Satisfaction:')
        st.table(most_recent['Customer Satisfaction Metrics:\nWhat channels do you primarily use to collect customer feedback? (Surveys, Social Media, Reviews)'])
    with fourth:
        st.subheader('Innovation:')
        st.table(most_recent['Innovation for Growth:\nHave you adopted any AI or automation technologies in your business processes? (Yes/No)'])


    butt = st.button("🧠Analyze information and produce solution")
    if butt:
        st.header(f"Solution for {company_name}'s problem:")
        st.subheader('🥇Overall Solution:')
        st.write(f"One of the most effective ways we have solved this problem in the past, given this clients persona, objective, and problem is",
                 "by making the space more attractive to employees, whilst reducing the unnecessary mundane office equipment. To be more precise,",
                 "this client should make the office furniture more modern, comfortable, and appealing such as beige chairs with wooden legs and",
                 "beige linen sofas in the middle. Include consumables for the employees such as a barista ready at the corner of the room.",
                 "include more greenery to make the ambiance feel more like home and appeal to the employees. ")
        st.header('🏆PPP Maximization:')
        st.write(f'Based on the information given to us, and {company_name}s prefered PPP weights, the top 3 best things they can change are:')
        st.write("""
                - Implement data analytics to monitor and control operational costs (Likely increase of 30% in profits)
                - Implement energy efficient technologies (Likely Decrease of 15% Long term costs and Decrease of 40% in energy consumption)
                - Increase employee training and development from 10 hours to 25 hours (Increasing employee engagement and increasing productivity and quality of jobs)
                """)
        st.write("Based on our trained ML models, this is the most effective change to your values and weighted PPP. With a likely 60%",
                 "increase in Profits, 40%, increase in sustainability metrics, and a 25%, increase in employee satisfaction. (For these metrics alone,",
                 "not including suggested general solution)")



    
    


        
else:
    st.title("Inside the Mind of DeepConsultant")
    st.markdown('##')

    st.subheader('What are the 3 main benefits of using DeepConsultant?')
    st.markdown(
        """
        - **1) Consistent, reliable and instantaneous source of business knowledge:** DeepConsultant will be trained on only the best consultancy advice from TCS to its clients. Where employees 
        might have gaps in knowledge and skills, DeepConsultant will be a one stop shop for the ultimate consultancy suggestion for any given problem, based on TCS history of problem solving.

        - **2) Creative Generation:** By feeding past business knowledge onto the system, DeepConsultant will become a superpowered brain that will be able to see patterns and learn how to solve new 
        problems in logical novel ways. Especially since it now uses additional Machine Learning models to aid in its understanding of how different factors affect desired metrics

        - **3) Client Satisfaction:** With this tool, TCS will be able to offer not only a more speedy response to its clients, especially compared to its competitors, but 
        will offer more reliable and consistent top tier consultancy advice. Whether working with a junior employee or senior, the client will always feel like he got 
        the answer from the best of the best.
        """
        )
    st.subheader('Explain the DeepConsultant process, in 3 Steps:')
    st.write('- **1) Input Data:** Two types of data will be needed to power the system, the first is text data',
             'It should briefly describe who the client is, what is its overall situation and what it seeks to improve.',
             'The second set of data should be features/inputs about the client which serve as powerful predictors for',
             'predicting key metrics, such as profit, sustainability, or employee satisfaction. The data preferably should be inputted',
             'via a form by the client and retrieved by the system with ease, but can also be inputted manually by TCS employees')
    
    tab = pd.DataFrame()
    tab['Problem/Client Request'] = ["This client has come to us with the problem of inefficient space utilization in their commercial real estate portfolio. They are struggling to maximize the use of available space, leading to operational inefficiencies and increased costs."]
    tab['Solution by TCS'] = ["Tata consultancy company might recommend a comprehensive space planning and optimization strategy. This involves assessing the current layout, identifying underutilized areas, and redesigning the space to enhance functionality. This could include implementing flexible workspaces, collaborative zones, and technology-driven solutions to make better use of the available square footage."]
    st.table(tab)
    
    st.write('- **2) Sensitivity Analysis:** The features with predictive power are then passed through models which',
             'individually predict the likely current profit, sustainability, and employee satisfaction of the property.',
             'To get an aggregate understanding of the current state of the property in terms of PPP, the following objective',
             'function can be used:')
    # Display the objective function using LaTeX
    st.latex(r'''
            \text{Objective Function} = \left(\frac{c_e}{m_e}w_e + \frac{c_p}{m_p}w_p + \frac{c_s}{m_s}w_s\right)
            ''')
    tab = pd.DataFrame()
    tab['Outputs'] = ['e','p','s']
    tab['c'] = ['Current Employee Satis','Current Profit','Current Sustainability']
    tab['m'] = ['Mean Employee Satis','Mean Profit','Mean Sustainability']
    tab['w'] = ['Weight Employee Satis','Weight Profit','Weight Sustainability']
    st.table(tab)
    st.write('- With this function, we can get a number that expresses the overall PPP score of the property in its current state.',
             'We can also tweak the weights to decide how important each P is in the PPP for this client. From this, we can perform Sensitivity Analysis, which is a measure of how the input features impact the outputs of the models.',
             'This is useful as we can see what would be the most effective change that the client could do, to maximize his',
             'PPP.')
    st.write('- **3) Joined Knowledge:** The system then prompts the DeepConsultant with the text input of the problem, and further',
             'feads it the rankings of what our models believe would have the biggest positive change in the clients weighted PPP.',
             'This allows DeepConsultant to not only review how TCS top consultants solved a problem similar to this before in different scenarios',
             'But it also has added information on pontential significant changes that TCS had not considered when solving these problems.',
             'Thus giving a reliable and founded professional suggestion to the problem, with added information which could amplify the results even further')
    

    st.subheader('What data would TCS need to perfect DeepConsultant?')
    st.write('- Assuming all the data is ready, building something like this would likely take a matter of days on skilled hands.',
             'For a quick, well built model, all TCS would need is a csv with two columns (Client Problem/Our Complete Solution) which would contain all the',
             'historical problem solving from TCS top consultants and their achievements. Assuming TCS already knows what generally good',
             'indicators of successful PPP are, they would just need a massive dataset from all their past clients, with the input features, and their current PPPs.')
    st.write('- Of course, this is not usually the case so it might take some time to preprocess past phone call data, emails and texts and documents to make them into a simple Problem -> Solution csv format.',
             'Also getting the data of the input features could take a while if they dont have that already, and if they dont know what the good predictors are,',
             'this can be discovered by Data Scientists, but again could take a while as well.')
