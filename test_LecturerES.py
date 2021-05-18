# Install libraries
from random import choice
from experta import *
import streamlit as st

class InfoML(Fact):
    """ Information about Machine Learning """
    pass

class IntroToML(KnowledgeEngine):
    @Rule(InfoML(choice='Definitions'))
    def def_ML(self):
        st.write("There are 2 definitions of Machine Learning.")
        st.write("Arthur Samuel, a pioneer in the domain of AI states: “Machine Learning is the field of study that gives computers the ability to learn without being explicitly programmed.” However, this is an older, informal definition.")
        st.write("Tom Mitchell, a machine learning professor states: “A computer program is said to learn from experience (E) with respect to some class of tasks (T) and performance measure (P). If its performance at tasks in T, as measured by P, improves with experience E.")

    @Rule(InfoML(choice='Examples of the Definitions'))
    def example_defs(self):
        st.write("For example: playing checkers.")
        st.write("E = the experience of playing many games of checkers")
        st.write("T = the task of playing checkers")
        st.write("P = the probability that the program will win the next game")

    @Rule(InfoML(choice='Classification of Machine Learning'))
    def classification_ML(self):
        st.write("In general, any machine learning problem can be assigned to one of 2 broad classifications: ")
        st.write("- Supervised Learning") 
        st.write("- Unsupervised Learning")


st.title("Lecturer Expert System - Machine Learning")

with st.form(key='my_form'):
    name = st.text_input(label='What is your name?')
    submit_button = st.form_submit_button(label='Submit')
if submit_button:
    st.write(f"Hello {name}! Welcome to the Machine Learning Lecturer Expert System!")

st.write(f"What would you like to know about Machine Learning? Please choose a chapter that you would like to learn!")
decision = st.selectbox('', ('Pick One!', "Introduction to ML", "Supervised Learning", 
                        "Unsupervised Learning", "Model Representation", "Cost Function", "Gradient Descent"))

if decision == "Introduction to ML":
    intro_choice = st.selectbox("What would you like to know in Introduction to ML?", ('', "Definitions", "Examples of the Definitions", "Classification of Machine Learning"))
    engine = IntroToML()
    engine.reset()
    engine.declare(InfoML(choice=intro_choice))
    engine.run()