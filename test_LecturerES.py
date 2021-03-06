# Install libraries
from os import write
from random import choice
from experta import *
import streamlit as st

# Importing classes for quiz
# IMPORTANT - run this file when you're in the WID2001 directory - else it will not run
import quiz.chap1 as chap1
from quiz.chap1 import *

import quiz.chap2 as chap2
from quiz.chap2 import *

import quiz.chap3 as chap3
from quiz.chap3 import *

import quiz.chap4 as chap4
from quiz.chap4 import *

import quiz.chap5 as chap5
from quiz.chap5 import *

import quiz.chap6 as chap6
from quiz.chap6 import *

text = '''

---

'''
class InfoML(Fact):
    """ Information about Machine Learning """
    pass

class IntroToML(KnowledgeEngine):
    @Rule(InfoML(choice='Learning Outcomes'))
    def learning_outcomes(self):
        st.write("Based on the Undergraduate Degree Programme Handbook, you will learn how to:")
        st.write("- Explain the concepts and techniques for supervised learning and unsupervised learning.")
        st.write("- Apply practical solutions to solve common problems in machine learning.")

    @Rule(InfoML(choice='Course Content and Outline'))
    def course_content(self):
        st.write("According to my knowledge as a newly developed Lecturer Expert System, I only have a handful of information in my repository of knowledge.")
        st.write("What I can teach you include:")
        st.write("- Introduction to ML\n"
        "- Supervised Learning\n"
        "- Unsupervised Learning\n"
        "- Model Representation\n"
        "- Cost Function\n"
        "- Gradient Descent\n")

        st.write("Once you're done equipping yourself with knowledge, I have a QUIZ function where you can test what you've learnt with me!")
        st.write("There will be a quiz for every chapter in LESMLO so be sure to try them out for a surprise!")
    
    @Rule(InfoML(choice='Definitions'))
    def def_ML(self):
        st.write("There are 2 definitions of Machine Learning:")
        st.image("imagefiles/Arthur.jpg",use_column_width=True )
        st.markdown('<h3><b>Arthur Samuel</b></h3>', unsafe_allow_html=True)
        st.write("A pioneer in the domain of AI - ???Machine Learning is the field of study that gives computers the ability to learn without being explicitly programmed.??? However, this is an older, informal definition.")
        st.image("imagefiles/Tom.jpg",use_column_width=True)
        st.markdown('<h3><b>Tom Mitchell</b></h3>', unsafe_allow_html=True)
        st.write("A machine learning professor - ???A computer program is said to learn from experience (E) with respect to some class of tasks (T) and performance measure (P). If its performance at tasks in T, as measured by P, improves with experience E.")

    @Rule(InfoML(choice='Examples of the Definitions'))
    def example_defs(self):
        st.markdown('<h3><b>Examples: Playing Checkers</b></h3>', unsafe_allow_html=True)
        st.image("imagefiles/checkers.jpg")
        st.write("E = the experience of playing many games of checkers")
        st.write("T = the task of playing checkers")
        st.write("P = the probability that the program will win the next game")

    @Rule(InfoML(choice='Classification of Machine Learning'))
    def classification_ML(self):
        st.write("In general, any machine learning problem can be assigned to one of 2 broad classifications: ")
        st.write("- Supervised Learning") 
        st.write("- Unsupervised Learning")
        st.image("imagefiles/sup-vs-unsup.png")
    @Rule (InfoML(choice="Quiz"))
    def quiz_chap1(self):
        chap1.run_chap1()

class SupervisedLearning(KnowledgeEngine):
    @Rule(InfoML(choice='Introduction'))
    def intro_SL(self):
        st.markdown('<h3><b>Supervised Learning</b></h3>', unsafe_allow_html=True)
        st.image("imagefiles/SL.jpg")
        st.write("In supervised learning, we are given a data set and already know what our current output should look like, having the idea that there is a relationship between the input and output.")
        st.write("Supervised learning problems are categorized into regression & classification problems.")

    @Rule(InfoML(choice='Regression Problem'))
    def regression_def(self):
        st.markdown('<h3><b>Regression</b></h3>', unsafe_allow_html=True)
        st.write("In a regression problem, we are trying to predict results within a continuous output, meaning that we are trying to map input variables to some continuous function")
        st.write("For example: Given data about the size of houses on the real estate market, try to predict their price. Price as a function of size is a continuous output, so this is a regression problem.")

    @Rule(InfoML(choice='Classification Problem'))
    def classification_def(self):
        st.markdown('<h3><b>Classification</b></h3>', unsafe_allow_html=True)
        st.write("In a classification problem, we are trying to map input variables into discrete categories. In other words, we are trying to map input variables into discrete categories.")
        st.write("Example: Given data about the size of houses on the real estate market, try to predict whether the house sells for more or less than the asking price. Here we are classifying the houses based on price into 2 discrete categories.")
    @Rule (InfoML(choice="Quiz"))
    def quiz_chap2(self):
        chap2.run_chap2()
class UnsupervisedLearning(KnowledgeEngine):
    @Rule (InfoML(choice="Introduction"))
    def intro_UL(self):
        st.markdown('<h3><b>Unsupervised Learning</b></h3>', unsafe_allow_html=True)
        st.image("imagefiles/UL.png")
        st.write("Unsupervised learning allows us to approach problems with little or no idea what our results should look like. We can derive structure from data where we don???t necessarily know the effect of the variables.")
        st.write("We can derive this structure by clustering the data based on relationships among the variables in the data. With unsupervised learning there is no feedback based on the prediction results.")
    @Rule (InfoML(choice="Clustering"))
    def clustering_def(self):
        st.markdown('<h3><b>Clustering</b></h3>', unsafe_allow_html=True)
        st.write("Take a collection of 1,000,000 different genes, and find a way to automatically group these genes into groups that are somehow similar or related by different variables, such as lifespan, location, roles and so on.")
    @Rule (InfoML(choice="Non-Clustering"))
    def nonclustering_def(self):
        st.markdown('<h3><b>Non-Clustering</b></h3>', unsafe_allow_html=True)
        st.write("The ???Cocktail Party Algorithm??? allows you to find structure in a chaotic environment. For example, identifying individual voices and music from a mesh of sounds at a cocktail party.")
    @Rule (InfoML(choice="Quiz"))
    def quiz_chap3(self):
        chap3.run_chap3()

class ModelRepresentation(KnowledgeEngine):
    @Rule (InfoML(choice="Introduction"))
    def intro_MR(self):
        st.markdown('<h3><b>Model Representation</b></h3>', unsafe_allow_html=True)
        st.write("A machine learning model can't directly see, hear, or sense input examples. Instead, you must create a representation of the data to provide the model with a useful vantage point into the data's key qualities. That is, in order to train a model, you must choose the set of features that best represent the data.")
    @Rule (InfoML(choice="Notation"))
    def notation_MR(self):
        st.markdown('<h3><b>Notations</b></h3>', unsafe_allow_html=True)
        st.write("$x^i$ = input variables / input features")
        st.write("$y^i$ = output or target variable that we want to predict")
        st.write("$(x^i , y^i)$ = training example")
        st.write("$(x^i , y^i); i = 1,...,m$ = training set")
        st.write("$X$ = space of input values")
        st.write("$Y$ = space of output values")
        st.write("The superscript $???(i)???$ in the notation is simply an index into the training set & has nothing to do with exponential.")
    @Rule (InfoML(choice="Goal for a given training set"))
    def goal_MR(self):
        st.markdown('<h3><b>Goal for a givven Training Set </b></h3>', unsafe_allow_html=True)
        st.write("To learn a function $h: X -> Y$ so that $h(x)$ is a ???good??? predictor for the corresponding value of y.")
        st.write("$h$ = hypothesis")
    @Rule (InfoML(choice="Definition of Hypothesis"))
    def hypothesis_MR(self):
        st.markdown('<h3><b>Definition of Hypothesis</b></h3>', unsafe_allow_html=True)
        st.write("Technically, this is a problem called function approximation, where we are approximating an unknown target function (that we assume exists) that can best map inputs to outputs on all possible observations from the problem domain.")
        st.write("An example of a model that approximates the target function and performs mappings of inputs to outputs is called a hypothesis in machine learning.")
        st.image("imagefiles/hypothesis.jpg")
    @Rule (InfoML(choice="Quiz"))
    def quiz_chap4(self):
        chap4.run_chap4()
class CostFunction(KnowledgeEngine):
    @Rule (InfoML(choice="Introduction"))
    def intro_CF(self):
        st.markdown('<h3><b>Cost Function</b></h3>', unsafe_allow_html=True)
        st.write("We can measure the accuracy of our hypothesis function by using a cost function. This takes an average difference of all the results of the hypothesis with inputs from x???s and the actual output y???s.")
    @Rule (InfoML(choice="Squared error function")) 
    def sqf_CF(self):
        st.markdown('<h3><b>Squared error function</b></h3>', unsafe_allow_html=True)
        st.write("$m$: Is the number of our training examples.")
        st.write("$??$: The Summatory.")
        st.write("$i$: The number of Example and the Output.")
        st.write("$h$: The Hypothesis of our Linear Regression Model")
        st.write(r"""$J(\theta) = \frac{1}{2m} \sum_{i=1}^m \left( h_{\theta}(x^{(i)}) - y^{(i)}\right)^2$""")
        st.write("This function is called the ???Squared error function??? or ???Mean squared error???.")
        st.write("After calculating the Cost Function, it will return a value that corresponds to the Model error. The continuous goal is to minimize the Cost Function. When the Cost Function is minimized, the error is minimized, and consequently, the performance of the Model is improved. But how can we minimize the cost function? There are various ways to do it but the commonly used one is called Gradient Descent which we will learn in the next chapter.")
    @Rule (InfoML(choice="Quiz"))
    def quiz_chap5(self):
        chap5.run_chap5()
class GradientDescent(KnowledgeEngine):
    @Rule (InfoML(choice="Introduction"))
    def intro_GD(self):
        st.markdown('<h3><b>Gradient Descent</b></h3>', unsafe_allow_html=True)
        st.write("Gradient Descent Algorithm tries continuously to find the minimum values that will satisfy the Hypothesis, and consequently, minimize the Cost Function!")
    @Rule (InfoML(choice="Representation of Gradient Descent"))
    def representation_GD(self):
        st.markdown('<h3><b>Representation of Gradient Descent</b></h3>', unsafe_allow_html=True)
        st.image("imagefiles/GD.png")
        st.write("This is a representation of the Gradient Descent Algorithm.")
        st.write("Cost function is successfully minimized when it is at the very bottom of the pits in the graph.")
        st.write("\nThe method to do this is by taking the derivative (the tangential line to a function) of the cost function. The slope of the tangent is the derivative at that point and it will give us a direction to move towards. We make steps down the cost function in the direction with the steepest descent. The size of each step is determined by the parameter ??, which is called the learning rate.")
        st.write("\nFor example, the distance between each 'star' in the graph above represents a step determined by parameter ??. (smaller ?? = smaller step, larger ?? = larger step)")
        st.write(r"""The direction in which the step is taken is determined by the partial derivative of $J(\theta _{0},\theta _{1})$""")
        st.write("Depending on where one starts on the graph, one could end up at different points. The image above shows us two different starting points that end up in two different places.")
    @Rule (InfoML(choice="Algorithm"))
    def algo_GD(self):
        st.markdown('<h3><b>Algorithm</b></h3>', unsafe_allow_html=True)
        st.write("The gradient descent algorithm is:")
        st.write("repeat until convergence:")
        st.write(r"""$\theta_j := \theta_j - \alpha\frac{\partial}{\partial \theta_j}J({\theta_{0}},\theta_{1})$ """)
        st.write(r"""where $j=0,1$ represents the feature index number""")
    @Rule (InfoML(choice="Quiz"))
    def quiz_chap6(self):
        chap6.run_chap6()

### Streamlit Code

st.title("Lecturer Expert System - Machine Learning") 
st.image('imagefiles/ML.jpg')

# Introduction
with st.form(key='name_form'):
    st.write("Welcome to the Machine Learning Lecturer Expert System! My name is LESMLO" + 
    " which stands for 'Lecturer Expert System for Machine Learning Operations! Very nice to meet you and to teach you today.")
    st.write("Please tell me about yourself!")
    name = st.text_input(label='What is your name?')
    occupation = st.text_input(label='What is your occupation?')
    submit_button = st.form_submit_button(label='Submit')
#if submit_button: (Found that removing this line keep the name displayed)
    st.write(f"Why hello there {name}! Hope you're excited to learn more about Machine Learning with me!")

st.header("Course Briefing")
st.write(f"Would you like to know more about what's in store with LESMLO?")
outline_decision = st.selectbox('', ("Sure!", "Learning Outcomes", "Course Content and Outline"))
if outline_decision == "Learning Outcomes":
    engine = IntroToML()
    engine.reset()
    engine.declare(InfoML(choice=outline_decision))
    engine.run()
elif outline_decision == "Course Content and Outline":
    engine = IntroToML()
    engine.reset()
    engine.declare(InfoML(choice=outline_decision))
    engine.run()

####################################################################################################################################

st.markdown(text)
st.header("Learning Section")
st.write(f"What would you like to know about Machine Learning? Please choose a chapter that you would like to learn!")
decision = st.selectbox('', ('Pick One!', "Introduction to ML", "Supervised Learning", 
                          "Unsupervised Learning", "Model Representation", "Cost Function", "Gradient Descent"))

if decision == "Introduction to ML":
    intro_choice = st.selectbox("What would you like to know in Introduction to ML?", ('', "Definitions", "Examples of the Definitions", "Classification of Machine Learning", "Quiz"))
    engine = IntroToML()
    engine.reset()
    engine.declare(InfoML(choice=intro_choice))
    engine.run()
elif decision == "Supervised Learning":
    sl_choice = st.selectbox("What would you like to know in Supervised Learning?", ('', "Introduction", "Regression Problem", "Classification Problem", "Quiz"))
    engine = SupervisedLearning()
    engine.reset()
    engine.declare(InfoML(choice=sl_choice))
    engine.run()
elif decision == "Unsupervised Learning":
    ul_choice = st.selectbox("What would you like to know in Unsupervised Learning?", ('', "Introduction", "Clustering", "Non-Clustering", "Quiz"))
    engine = UnsupervisedLearning()
    engine.reset()
    engine.declare(InfoML(choice=ul_choice))
    engine.run()
elif decision == "Model Representation":
    mr_choice = st.selectbox("What would you like to know in Model Representation?", ('', "Introduction", "Notation", "Goal for a given training set", "Definition of Hypothesis", "Quiz"))
    engine = ModelRepresentation()
    engine.reset()
    engine.declare(InfoML(choice=mr_choice))
    engine.run()
elif decision == "Cost Function":
    cf_choice = st.selectbox("What would you like to know in Cost Function?", ('', "Introduction", "Squared error function", "Quiz"))
    engine = CostFunction()
    engine.reset()
    engine.declare(InfoML(choice=cf_choice))
    engine.run()
elif decision == "Gradient Descent":
    gd_choice = st.selectbox("What would you like to know in Gradient Descent?", ('', "Introduction", "Representation of Gradient Descent","Algorithm", "Quiz"))
    engine = GradientDescent()
    engine.reset()
    engine.declare(InfoML(choice=gd_choice))
    engine.run()