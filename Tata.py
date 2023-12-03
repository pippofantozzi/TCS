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
        st.subheader('LED:')
        st.table(most_recent['Do you utilize LED lighting?'])
    with second:
        st.subheader('HVAC:')
        st.table(most_recent['Do you utilize HVAC System Optimization?'])
    with third:
        st.subheader('Renewable Energy:')
        st.table(most_recent['Do you have some form of renewable energy system in place?'])
    with fourth:
        st.subheader('Smart Building:')
        st.table(most_recent['Is your building considered a Smart Building?'])
    with fifth:
        st.subheader('Water Consumption:')
        st.table(most_recent['Are there low-flow fixtures in place for water consumption?'])
    with sixth:
        st.subheader('Co-working:')
        st.table(most_recent['How many Co-Working spaces do you have?'])

    st.write("")
    first, second, third, fourth = st.columns(4)
    with first:
        st.subheader('Fitness Center:')
        st.table(most_recent['Does your building include a fitness center or some form of fitness membership nearby for its tenants?'])
    with second:
        st.subheader('Social Area:')
        st.table(most_recent['Does your building include some sort of social area for the employees to network and socialize?'])
    with third:
        st.subheader('Event Organization:')
        st.table(most_recent['Are there events being organized for socializing and networking within your building?'])
    with fourth:
        st.subheader('Budget:')
        st.table(most_recent['What is your budget'])


    butt = st.button("🧠Analyze information and produce solution")
    if butt:
        st.header(f"Solution for {company_name}'s problem:")
        st.subheader('🥇Overall Solution with Weighted PPP Optimization:')
        st.write("Based on our historical clients' problems and our most effective solutions, and based on our trained Machine Learning models,",
                 "the most effective solution given the problem you described and the information/data about your building would be:")
        st.write(f"""Occupancy Maximisation:
* Floor Repurposing:
    * Floor 17: Sky Lounge Bar
    * Floor 16: Co-Working Space
    * Floor 15: Co-Working Space
    * Floor 5: Remain as Work Space
    * Floor 4: Event Space/Conference Facilities
    * Floor 3: Fitness and Wellness Centre
Energy Efficiency Upgrades:
* Lighting Upgrades:
    * Switch to LED lighting, reducing energy consumption by up to 50% (or 300,000 kWh per year).
* HVAC System Optimization:
    * Reduce heating and cooling costs by 20-30%.
    * Implement programmable thermostats for comfort and up to 15% energy savings.
* Insulation and Windows:
    * Improve insulation for 10-20% reduction in heating and cooling costs.
* Renewable Energy:
    * Implement solar panels for renewable energy, reducing reliance on the grid.
* Smart Building Tech:
    * Implement automation systems, IoT, and occupancy sensors for 10-20% additional energy savings.
* Water Conservation:
    * Install low-flow fixtures to reduce water consumption.


Estimated Costs:
* Entire Building Upgrades:
    * Lighting Upgrades: $112,194 to $336,582
    * HVAC System Optimization: $168,291 to $560,970
    * Insulation and Windows: $280,485 to $1,121,940
    * Renewable Energy (Solar): $3,000,000 to $7,500,000
    * Smart Building Tech: $56,097 to $280,485
    * Water Conservation: $50,000 to $200,000
    * Total Estimated Cost: ≈$15,609,100
* Designated Space (Entire Floor):
    * Sky Lounge Bar (Fl 17): $1,719,300 to $2,865,500
    * Co-Working Space (Fl 16-15): $1,286,850 to $2,573,700
    * Remain as Work Space (Fl 5): Assumes existing setup
    * Event Space (Fl 4): $1,146,200 to $2,292,400
    * Fitness and Wellness (Fl 3): $1,432,750 to $2,292,400
    * Total Estimated Cost: ≈$13,265,044""")



    
    


        
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
