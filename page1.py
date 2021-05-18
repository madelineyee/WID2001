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

