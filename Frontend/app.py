import pandas as pd
import numpy as np
import pickle
import streamlit as st

# Since i have stored recommendations for the first 200 respondents,
# import the similarity matrix and job data
dfcont = pd.read_csv("F:/Job-Recommendation-System/data/collaborative filtering/recommendations.csv")

with open('similarity_matrix.pkl', 'rb') as f:
    sim = pickle.load(f)

def recommend_jobs(user_id):
    """
    Recommends jobs based on the user ID and the similarity matrix.

    Args:
        user_id (int): The ID of the user for whom recommendations are needed

    Returns:
        pandas.DataFrame: A DataFrame containing recommended companies, job titles,
                          URLs, skills.
    """
    if 1 <= user_id <= 200:
        # Find the most similar user (excluding the user itself)
        m1 = max(sim[user_id][:user_id])
        m2 = max(sim[user_id][user_id + 1:])
        ma = max(m1, m2)
        suser = sim[user_id].index(ma)

        # Get recommended data from the similar user
        recommended_data = dfcont.loc[dfcont.Respondent == suser]

        return recommended_data[["company", "jobtitle", "advertiserurl", "skills"]]
    else:
        return pd.DataFrame()  

st.title("Job Recommendation System")
user_id = st.number_input("Enter your User ID:", min_value=1)

if st.button("Recommend Jobs"):
    if user_id:
        recommended_jobs = recommend_jobs(user_id)
        if not recommended_jobs.empty:
            st.subheader(f"Recommended Jobs for User {user_id}")
            
            st.write(recommended_jobs.to_html(escape=False), unsafe_allow_html=True)
        else:
            st.warning("No recommendations found for User ID " + str(user_id))
    else:
        st.warning("Please enter a valid User ID.")
