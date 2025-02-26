import streamlit as st
import pandas as pd

def calculate_score(responses):
    scores = {
        "Emotional Wellbeing": sum(responses[:5]),
        "Relational Wellbeing": sum(responses[5:10]),
        "Physical Wellbeing": sum(responses[10:15]),
        "Mental Wellbeing": sum(responses[15:20]),
        "Purpose & Meaning": sum(responses[20:25]),
    }
    return scores

def interpret_score(score):
    if score >= 21:
        return "Thriving – This area is a major strength."
    elif score >= 16:
        return "Doing Well – You are in a good place but could make slight improvements."
    elif score >= 11:
        return "Needs Attention – This area requires some focus."
    else:
        return "Major Growth Opportunity – Consider prioritizing improvement in this area."

st.title("Wellbeing Dimensions Assessment")
st.write("Rate yourself on a scale of 1 (Strongly Disagree) to 5 (Strongly Agree)")

questions = [
    # Emotional Wellbeing
    "I acknowledge and accept my emotions rather than suppressing them.",
    "I allow myself to fully experience emotions without judgment.",
    "I have healthy coping strategies for stress and difficult emotions.",
    "I feel emotionally resilient when facing challenges.",
    "I can express my emotions effectively to others.",
    # Relational Wellbeing
    "I have meaningful connections with friends, family, or colleagues.",
    "I regularly engage in social interactions that energize me.",
    "I feel comfortable asking for help when needed.",
    "I maintain healthy boundaries in my relationships.",
    "I feel valued and supported by my social circle.",
    # Physical Wellbeing
    "I get enough quality sleep to feel rested and energized.",
    "I eat a balanced diet that fuels my body.",
    "I engage in regular physical activity or exercise.",
    "I stay hydrated and take care of my body’s basic needs.",
    "I make time for relaxation and recovery.",
    # Mental Wellbeing
    "My internal self-talk is generally positive and encouraging.",
    "I am aware of my thought patterns and can challenge negative thinking.",
    "I engage in activities that stimulate my mind and creativity.",
    "I manage stress in a healthy and constructive way.",
    "I feel a sense of control over my mental and emotional state.",
    # Purpose & Meaning
    "I feel a strong sense of purpose in my daily life.",
    "The work I do (professionally or personally) aligns with my values.",
    "I take time to reflect on what truly matters to me.",
    "I engage in activities that give me a deep sense of fulfillment.",
    "I feel connected to something greater than myself."
]

responses = []
for question in questions:
    responses.append(st.slider(question, 1, 5, 3))

if st.button("Calculate My Wellbeing Score"):
    scores = calculate_score(responses)
    st.subheader("Your Wellbeing Scores")
    for category, score in scores.items():
        st.write(f"**{category}:** {score} - {interpret_score(score)}")
