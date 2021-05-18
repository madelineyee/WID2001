# Importing libraries

from experta import *
import streamlit as st

class Greetings(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact (action = "greet")

    @Rule (Fact(action = "greet"),
        NOT(Fact(name=W())))
    def ask_name(self):
        self.declare(Fact(name=input("Hi! What's your name? ")))

    @Rule(Fact(action = "greet"),
        NOT(Fact(location=W())))
    def ask_location(self):
        self.declare(Fact(location=input("Where are you from? ")))

    @Rule(Fact(action = "greet"),
        Fact (name = MATCH.name),
        Fact (location = MATCH.location))
    
    def greet(self, name, location):
        print("Hi %s! How is the weather in %s today? " % (name, location))


engine = Greetings()
engine.reset()
engine.run()
