import streamlit as st
from app_pages.multipage import MultiPage
from app_pages.page_hypothesis
from app_pages.page_mildew_detector
from app_pages.page_summary
from app_pages.page_visualisation
from app_pages.page_ml_performance


# Creates an instance of MultiPage class
app = MultiPage(app_name="Mildew Detection in Cherry Leaves")

# Calls the app_page method in the MultiPage class
app.app_page("Summary", project_summary_page)
app.app_page("Cherry Leaves Visualisation", cherry_leaves_visualisation_page)
app.app_page("Mildew Detector", mildew_detector_page)
app.app_page("Hypothesis", project_hypothesis_page)
app.app_page("Machine Learning Performance", ml_performance_page)

# Runs the app
app.run()
