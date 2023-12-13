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
    options=["TCS DeepConsultant", "How It Works","Settings"],
    icons=["capslock","book","gear"],
    menu_icon=["triangle"],
    default_index=0,
    orientation="horizontal"
)

if selected == "TCS DeepConsultant":

    # --- MAINPAGE --- 
    st.title("Welcome to DeepConsultant, how can I help today?")
    st.markdown("##")

    form_answers = read()
    company_names = form_answers['Identity:\nWhat is the name of your Company?'].unique()
    company_name = st.selectbox('Which client are we analyzing?:',company_names) 
    most_recent = form_answers.loc[form_answers['Identity:\nWhat is the name of your Company?'] == company_name][-1:]
    #form_answer = st.selectbox('Check if this is the form date input you want to analyze:',dates) 

    first,second,third = st.columns(3)
    with first:
        information = st.button("🔍See Client's Information Uploaded")
    with second:
        solution = st.button("🧠See Generated Solution")
    with third:
        new_solutions = st.button("⚡Generate New Solutions")
    if information:
        st.header(f"{company_name}'s most recent form upload contains the following information:")
        st.markdown("---")
        summary = most_recent['Summary:\n\nBriefly describe what kind of company you are, where you are located, what problem you are facing, and what solution you are looking for']
        st.subheader('🔍Problem Summary:')
        st.write(summary.iloc[0])
        st.markdown("---")

        PPP = most_recent['PPP:\nHow much do you value each P in PPP?\n\nAnswer as: Profit-0.4,People-0.2,Planet-0.4\n\nAnswer must add up to 1']
        Profit,People,Planet = str(PPP)[12:15],str(PPP)[23:26],str(PPP)[34:37]
        first, second, third, = st.columns(3)
        with first:
            st.subheader(f'💰Profit: {float(Profit)*100}%')
        with second:
            st.subheader(f'🙇People: {float(People)*100}%')
        with third:
            st.subheader(f'🌎Planet: {float(Planet)*100}%')

        st.markdown("---")
        st.subheader("🌐Client Data:")
        st.markdown("---")
        first, second, third, fourth, fifth, sixth = st.columns(6)
        with first:
            profitability_info = most_recent['Profitability:\nWhat percentage of your budget is allocated to marketing and advertising?'].iloc[0]

            # Use st.write to display the information
            st.write('**Profitability:**\nWhat percentage of your budget is allocated to marketing and advertising?:')
            st.markdown("---")
            st.write(f'**Answered: {profitability_info}**')
        with second:
            st.write('**Cost Management:**\nDo you utilize data analytics to monitor and control operational costs? (Yes/No)')
            info = most_recent['Cost Management:\nDo you utilize data analytics to monitor and control operational costs? (Yes/No)'].iloc[0]
            st.markdown("---")
            st.write(f'**Answered: {info}**')
        with third:
            st.write('**Sustainability Practices:**\nHow would you describe your waste management strategy? (Recycling, Reduction, None)')
            info = (most_recent['Sustainability Practices:\nHow would you describe your waste management strategy? (Recycling, Reduction, None)'].iloc[0])
            st.markdown("---")
            st.write(f'**Answered: {info}**')
        with fourth:
            st.write('**Environmental Certifications:**\nHave you implemented energy-efficient technologies in your operations? (Yes/No)')
            info = (most_recent['Environmental Certifications:\nHave you implemented energy-efficient technologies in your operations? (Yes/No)'].iloc[0])
            st.markdown("---")
            st.write(f'**Answered: {info}**')
        with fifth:
            st.write('**Community Engagement:**\nHow many local community events or initiatives did your business participate in during the last year?')
            info = (most_recent['Community Engagement:\nHow many local community events or initiatives did your business participate in during the last year?'].iloc[0])
            st.markdown("---")
            st.write(f'**Answered: {info}**')
        with sixth:
            st.write('**Employee Satisfaction:**\nOn a scale of 1 to 5, how would your employees rate the effectiveness of internal communication?')
            info = (most_recent['Employee Satisfaction:\nOn a scale of 1 to 5, how would your employees rate the effectiveness of internal communication?'].iloc[0])
            st.markdown("---")
            st.write(f'**Answered: {info}**')
        st.markdown("---")
        first, second, third, fourth = st.columns(4)
        with first:
            st.write('**Employee Training and Development:**\nHow many hours of training per month, on average, do you provide to each employee?')
            info = (most_recent['Employee Training and Development:\nHow many hours of training per month, on average, do you provide to each employee?'].iloc[0])
            st.markdown("---")
            st.write(f'**Answered: {info}**')
        with second:
            st.write('**Customer Feedback and Loyalty Programs:**\nDo you use sentiment analysis tools to extract insights from customer feedback? (Yes/No)')
            info = (most_recent['Customer Feedback and Loyalty Programs:\nDo you use sentiment analysis tools to extract insights from customer feedback? (Yes/No)'].iloc[0])
            st.markdown("---")
            st.write(f'**Answered: {info}**')
        with third:
            st.write('**Customer Satisfaction Metrics:**\nWhat channels do you primarily use to collect customer feedback? (Surveys, Social Media, Reviews)')
            info = (most_recent['Customer Satisfaction Metrics:\nWhat channels do you primarily use to collect customer feedback? (Surveys, Social Media, Reviews)'].iloc[0])
            st.markdown("---")
            st.write(f'**Answered: {info}**')
        with fourth:
            st.write('**Innovation for Growth:**\nHave you adopted any AI or automation technologies in your business processes? (Yes/No)')
            info = (most_recent['Innovation for Growth:\nHave you adopted any AI or automation technologies in your business processes? (Yes/No)'].iloc[0])
            st.markdown("---")
            st.write(f'**Answered: {info}**')
        st.markdown("---")
        

    #butt = st.button("🧠Analyze information and produce solution")
    if solution:
        st.header(f"Solution for {company_name}'s problem:")
        st.markdown("---")
        st.subheader('🥇Overall Solution:')
        st.write(f"One of the most effective ways we have solved this problem in the past, given this clients persona, objective, and problem is",
                 "by making the space more attractive to employees, whilst reducing the unnecessary mundane office equipment. To be more precise,",
                 "this client should make the office furniture more modern, comfortable, and appealing such as beige chairs with wooden legs and",
                 "beige linen sofas in the middle. Include consumables for the employees such as a barista ready at the corner of the room.",
                 "include more greenery to make the ambiance feel more like home and appeal to the employees. The rooftop should be accessible for both",
                 "coffee or cocktail visits during the evening. Consider implementing solar pannel windows leading to more sustainble energy consumption",
                 "both decreasing costs and also increasing revenue from the selling of the energy supply. Include a sky lounge bar in the rooftop for",
                 "employees to socialize and network with other employees in the building. Additionally, if there is enough capital, using one of the",
                 "floors for a wellness and fitness center will increase employee satisfaction as well as increasing their energy in the workplace")
        st.markdown("---")
        st.header('🏆PPP Maximization:')
        st.write(f'**Based on the information given to us, and {company_name}s prefered PPP weights, the top 3 best things they can change are:**')
        st.write("""
                - Implement data analytics to monitor and control operational costs (Likely increase of 30% in profits)
                - Implement energy efficient technologies (Likely Decrease of 15% Long term costs and Decrease of 40% in energy consumption)
                - Increase employee training and development from 10 hours to 25 hours (Increasing employee engagement and increasing productivity and quality of jobs)
                """)
        st.write("Based on our trained ML models, this is the most effective change to your values and weighted PPP. With a likely 60%",
                 "increase in Profits, 40%, increase in sustainability metrics, and a 25%, increase in employee satisfaction. (For these metrics alone,",
                 "not including suggested general solution)")
        st.markdown("---")
        st.header("📲Sentiment Analysis:")
        st.markdown("---")
        st.write("""
            **Positive Feedback:**""")
        #st.markdown("---")
        st.write("""
            **1. Collaborative Workspaces:**
            A significant number of positive reviews highlight the building's collaborative workspaces. Employees appreciate the open layout and flexible seating arrangements, fostering a sense of community and encouraging teamwork. To capitalize on this positive sentiment, consider expanding collaborative areas or introducing more modern furniture to enhance comfort.

            **2. Amenities and Facilities:**
            Many reviews commend the building's amenities and facilities, such as the well-equipped gym, spacious lounge areas, and on-site dining options. Capitalize on these positive sentiments by continuing to invest in top-notch facilities that contribute to employee well-being and work-life balance.

            **3. Responsive Management:**
            Positive comments frequently mention the management's responsiveness to concerns and quick resolution of maintenance issues. Maintain this positive aspect by consistently addressing concerns promptly and communicating effectively with tenants to foster a positive tenant-management relationship.""")
        st.markdown("---")
        st.write("""
            **Areas for Improvement:**""")
        #st.markdown("---")
        st.write("""
            **1. Parking Facilities:**
            Several negative reviews mention challenges with parking facilities. Consider conducting a review of the current parking arrangements and exploring options to improve accessibility and convenience for tenants. This may involve optimizing existing spaces or expanding the parking capacity if feasible.

            **2. Temperature Control:**
            A recurring theme in negative reviews is dissatisfaction with temperature control on certain floors. To address this issue, consider upgrading the HVAC systems to ensure a more consistent and comfortable working environment. Regular maintenance checks and proactive response to temperature-related concerns will contribute to improved satisfaction.

            **3. Common Area Cleanliness:**
            Some reviews express concerns about the cleanliness of common areas. Enhance the cleaning schedule for shared spaces, including lobbies, hallways, and restrooms. Additionally, encourage tenants to report cleanliness issues promptly, and implement measures to address concerns in a timely manner.""")
        st.markdown("---")
        st.write("""
            **Sentiment Analysis Conclusion:**
            While the sentiment analysis reveals a generally positive perception of the commercial real estate building, addressing specific concerns related to parking facilities, temperature control, and common area cleanliness can contribute to an even more favorable tenant experience. Capitalizing on the existing strengths, such as collaborative workspaces, amenities, and responsive management, will further solidify the building's reputation as an excellent workplace. Regularly monitoring and addressing tenant feedback will be essential for continuous improvement and tenant satisfaction.""")
        st.markdown("---")

        st.header("📌Conclusion:")
        st.write("""In tackling the challenges faced by St. Helens Tower, the proposed multipart solution presents a comprehensive approach that intertwines enhancing employee satisfaction, optimizing operational efficiency, and leveraging sentiment analysis to refine existing strengths and address areas of improvement.

The overarching solution focuses on transforming the workspace into an inviting and functional environment. By incorporating modern, comfortable furniture, introducing greenery, and offering amenities like a barista corner and rooftop access, the aim is to create a space that fosters productivity, well-being, and a sense of community among employees. Embracing sustainability through solar panels and a focus on energy efficiency not only reduces costs but also aligns with contemporary environmental values.

Additionally, the prioritized changes aligned with St. Helens Tower's preferred PPP weights provide a clear roadmap for maximizing profits, sustainability metrics, and employee satisfaction. The implementation of data analytics, energy-efficient technologies, and increased employee training emerges as pivotal drivers, promising substantial gains across these key metrics.

Furthermore, the sentiment analysis highlights both the strengths to capitalize on and areas that necessitate improvement. Leveraging collaborative workspaces and top-notch amenities as strengths, the proposal suggests enhancing these elements to further elevate employee experience. Simultaneously, addressing concerns related to parking, temperature control, and common area cleanliness signifies a commitment to refining existing shortcomings, ensuring a more holistic and satisfying tenant experience.

In conclusion, this multipart solution offers a balanced strategy that not only addresses the immediate concerns at St. Helens Tower but also lays the groundwork for sustainable growth, enhanced employee satisfaction, and a strengthened tenant experience. It's a roadmap tailored to the specific needs and aspirations of the Tower, aiming not just for short-term fixes but for enduring, positive transformations.""")
        st.markdown("---")
        first,second = st.columns(2)
        with first:
            pdf = st.button("📄Download solution as pdf")
        with second:
            prompt = st.text_input("Do you want to send this solution to any other emails? Write them here:")
            email = st.button("📩Send Email")
        

    
    


        
elif selected == "How It Works":
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
    st.write("""
**Problem Statement:**
Tata Consultancy Services (TCS) wants a more effective way to provide solutions to their commercial real estate clients.

**Proposed Solution:**
1. **Client Input Form:**
   - Clients fill out a form with a written description of their real estate problem and provide predictive metrics related to profit, sustainability, and employee satisfaction.

2. **AI Solution Components:**

   a. **ChatGPT-like System (Generative AI):**
      - This system understands the client's problem by analyzing the written description and leveraging TCS's historical problem-solving knowledge.
      - Generates a written output suggesting a solution based on business expertise and past successes.

   b. **Machine Learning Models (Non-generative AI):**
      - Processes predictive metrics to predict profit, sustainability, and employee satisfaction.
      - Performs sensitivity analysis to recommend the top 5 changes the client should make to optimize these metrics.

   c. **Web Scraping Bot (Non-generative AI):**
      - Extracts positive and negative reviews about the client's real estate from the internet.

3. **Integration and Final Output (Generative AI):**
   - Three outputs from the above components (ChatGPT-like, ML Models, Web Scraping) are passed to a final generative AI.
   - This final AI generates a clear, written response for TCS:
      - Part 1: Outlines the general solution based on historical knowledge and current problem description.
      - Part 2: Recommends changes to predictive variables for optimal metrics and quantifies their impact.
      - Part 3: Advises the client based on online reviews, suggesting improvements and areas to be cautious.

**Explanation:**
- **Generative AI:** This creates human-like text based on the input it receives. In this solution, the ChatGPT-like system and the final generative AI are generative components.

- **Non-generative AI:** This involves data analysis, predictions, and information extraction. In this solution, the machine learning models and the web scraping bot fall into this category.

**Key Points:**
- *Generative AI is used for generating human-like responses and suggestions.*
- *Non-generative AI is used for data processing, analysis, and information extraction.*

This integrated solution allows TCS to efficiently understand client problems, optimize predictive metrics, and consider real-world feedback for comprehensive and effective recommendations in the commercial real estate domain.""")
    

else:
    st.title("Settings:")
    st.markdown("---")
    st.toggle("Send Client Generated Solution Via Email As Soon As Form Is Submitted")
    st.markdown("---")
    st.text_input("Add other employee emails to receive proposed solution to problem when as soon as ready:")   
    st.button("Add Emails")
    st.markdown("---")
    st.write("**Current Emails included in list:** | RachelWise@brokers.com | DylanMasters@brokers.com | OliviaSwift@brokers.com")
