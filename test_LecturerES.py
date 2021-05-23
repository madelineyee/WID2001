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
        st.write("There are 2 definitions of Machine Learning:")
        st.image("imagefiles/Arthur.jpg")
        st.markdown('<h3><b>Arthur Samuel</b></h3>', unsafe_allow_html=True)
        st.write("A pioneer in the domain of AI - “Machine Learning is the field of study that gives computers the ability to learn without being explicitly programmed.” However, this is an older, informal definition.")
        st.image("imagefiles\Tom.jpg")
        st.markdown('<h3><b>Tom Mitchell</b></h3>', unsafe_allow_html=True)
        st.write("A machine learning professor - “A computer program is said to learn from experience (E) with respect to some class of tasks (T) and performance measure (P). If its performance at tasks in T, as measured by P, improves with experience E.")

    @Rule(InfoML(choice='Examples of the Definitions'))
    def example_defs(self):
        st.image("imagefiles\checkers.jpg")
        st.write("For example: playing checkers.")
        st.write("E = the experience of playing many games of checkers")
        st.write("T = the task of playing checkers")
        st.write("P = the probability that the program will win the next game")

    @Rule(InfoML(choice='Classification of Machine Learning'))
    def classification_ML(self):
        st.write("In general, any machine learning problem can be assigned to one of 2 broad classifications: ")
        st.write("- Supervised Learning") 
        st.write("- Unsupervised Learning")
        st.image("imagefiles\sup-vs-unsup.png")

class SupervisedLearning(KnowledgeEngine):
    @Rule(InfoML(choice='Introduction'))
    def intro_SL(self):
        st.write("In supervised learning, we are given a data set and already know what our current output should look like, having the idea that there is a relationship between the input and output.")
        st.write("Supervised learning problems are categorized into regression & classification problems.")

    @Rule(InfoML(choice='Regression Problem'))
    def regression_def(self):
        st.write("In a regression problem, we are trying to predict results within a continuous output, meaning that we are trying to map input variables to some continuous function")
        st.write("For example: Given data about the size of houses on the real estate market, try to predict their price. Price as a function of size is a continuous output, so this is a regression problem.")

    @Rule(InfoML(choice='Classification Problem'))
    def classification_def(self):
        st.write("In a classification problem, we are trying to map input variables into discrete categories. In other words, we are trying to map input variables into discrete categories.")
        st.write("Example: Given data about the size of houses on the real estate market, try to predict whether the house sells for more or less than the asking price. Here we are classifying the houses based on price into 2 discrete categories.")

class UnsupervisedLearning(KnowledgeEngine):
    @Rule (InfoML(choice="Introduction"))
    def intro_UL(self):
        st.write("Unsupervised learning allows us to approach problems with little or no idea what our results should look like. We can derive structure from data where we don’t necessarily know the effect of the variables.")
        st.write("We can derive this structure by clustering the data based on relationships among the variables in the data. With unsupervised learning there is no feedback based on the prediction results.")
    @Rule (InfoML(choice="Clustering"))
    def clustering_def(self):
        st.write("Take a collection of 1,000,000 different genes, and find a way to automatically group these genes into groups that are somehow similar or related by different variables, such as lifespan, location, roles and so on.")
    @Rule (InfoML(choice="Non-Clustering"))
    def nonclustering_def(self):
        st.write("The “Cocktail Party Algorithm” allows you to find structure in a chaotic environment. For example, identifying individual voices and music from a mesh of sounds at a cocktail party.")


## Streamlit Code

st.title("Lecturer Expert System - Machine Learning")
st.image('ML.jpg')


with st.form(key='my_form'):
    name = st.text_input(label='What is your name?')
    submit_button = st.form_submit_button(label='Submit')
#if submit_button: (Found that removing this line keep the name displayed)
    st.write(f"Why hello there {name}! Welcome to the Machine Learning Lecturer Expert System!")

st.write(f"What would you like to know about Machine Learning? Please choose a chapter that you would like to learn!")
decision = st.selectbox('', ('Pick One!', "Introduction to ML", "Supervised Learning", 
                          "Unsupervised Learning", "Model Representation", "Cost Function", "Gradient Descent"))

if decision == "Introduction to ML":
    intro_choice = st.selectbox("What would you like to know in Introduction to ML?", ('', "Definitions", "Examples of the Definitions", "Classification of Machine Learning"))
    engine = IntroToML()
    engine.reset()
    engine.declare(InfoML(choice=intro_choice))
    engine.run()
elif decision == "Supervised Learning":
    sl_choice = st.selectbox("What would you like to know in Supervised Learning?", ('', "Introduction", "Regression Problem", "Classification Problem"))
    engine = SupervisedLearning()
    engine.reset()
    engine.declare(InfoML(choice=sl_choice))
    engine.run()
elif decision == "Unsupervised Learning":
    ul_choice = st.selectbox("What would you like to know in Supervised Learning?", ('', "Introduction", "Clustering", "Non-clustering"))
    engine = UnsupervisedLearning()
    engine.reset()
    engine.declare(InfoML(choice=ul_choice))
    engine.run()
