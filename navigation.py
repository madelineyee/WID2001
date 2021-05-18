import SessionState
import streamlit as st
import io
from experta import *


st.set_page_config(
    page_icon=":shark:",
    layout="wide",

)

def pageZero(sesh):
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

def pageOne(sesh):
    st.title('page ONE')
    st.write('one')

def pageTwo(sesh):
    st.title('TWO')
    st.write('two')

sesh = SessionState.get(curr_page = 0)
PAGES = [pageZero, pageOne, pageTwo]

def main():
    ####SIDEBAR STUFF
    st.sidebar.title("this is an app:")
    
    st.sidebar.markdown('Might be easier to import the pageOne/pageTwo/pageThree from a separate file to make the code cleaner')

    #####MAIN PAGE NAV BAR:
    # Form to get user's name
    st.markdown(' # Traffic Light Expert System')
    with st.form(key='my_form'):
        name = st.text_input(label='Enter your name')
        submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        st.write(f'### Hello {name}! Welcome to Traffic Light Info Expert System')
   
    st.markdown('----------------------------------')


    #####MAIN PAGE APP:
    
    page_turning_function = PAGES[sesh.curr_page]
    page_turning_function(sesh)

    ## Page Navigation
    st.write('PAGE NUMBER:', sesh.curr_page)
    st.markdown('Click Next to go to the next page')
    if st.button('Back:'):
        sesh.curr_page = max(0, sesh.curr_page-1)
    if st.button('Next page:'):
        sesh.curr_page = min(len(PAGES)-1, sesh.curr_page+1)

if __name__=='__main__':
    main()