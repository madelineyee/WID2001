from random import choice
from experta import *
import streamlit as st

## Rules (using experta)
class Light(Fact):
    """Info about the traffic light."""
    pass

class RobotCrossStreet(KnowledgeEngine):
    @Rule(Light(color='green'))
    def green_light(self):
        st.write("Walk")

    @Rule(Light(color='red'))
    def red_light(self):
        st.write("Don't walk")

    @Rule(AS.light << Light(color=L('yellow') | L('blinking-yellow')))
    def cautious(self, light):
        st.write("Be cautious because light is", light["color"])



## Interface (using streamlit)
st.title('Traffic Light Info')

# Form to get user's name
with st.form(key='my_form'):
    name = st.text_input(label='Enter your name')
    submit_button = st.form_submit_button(label='Submit')
if submit_button:
    st.write(f'Hello {name}! Welcome to Traffic Light Info Expert System')


st.write(f'What would you like to know about traffic lights?')
decision = st.selectbox('',('Pick One','Facts about Traffic Lights','I want to cross the street'))
if decision == 'Facts about Traffic Lights':
    st.write("The world's first traffic light was installed in London in 1868.")
elif decision == 'I want to cross the street':
    lightcolour = st.selectbox('What colour is the traffic light?',('','green','red','yellow','blinking-yellow'))
    engine = RobotCrossStreet()
    engine.reset()
    engine.declare(Light(color=lightcolour))
    engine.run()



