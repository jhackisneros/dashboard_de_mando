import streamlit as st
from functions.ChronosLogic import ChronosLogic

class ChronosPage:
    def __init__(self):
        self.logic = ChronosLogic()

    def show(self):
        self.logic.render()
