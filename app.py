import streamlit as st

from screens.home import show_home
from screens.appliance_manager import show_appliance_manager
from screens.energy_dashboard import show_energy_dashboard
from screens.energy_calculator import show_energy_calculator

# -----------------------------------
# APPLICATION CONFIGURATION
# -----------------------------------
st.set_page_config(
    page_title="Household Energy Advisor",
    page_icon="⚡",
    layout="wide"
)
# -----------------------------------
# INITIALIZE APPLICATION STATE
# -----------------------------------
if "appliance" not in st.session_state:
    st.session_state.appliances=[
        {"name" : "Refrigerator", "quantity": 1, "kilowatts per hour": 0.15, "hours": 24}
    ]

# -----------------------------------
# SIDEBAR NAVIGATION
# -----------------------------------
st.sidebar.title("Energy Advisor")
st.sidebar.caption("Monitor your electricity usage")
st.sidebar.divider()
menu=st.sidebar.radio(
    "Main Menu",
    ["Home",
     "Energy Dashboard",
     "Appliance Manager",
     "Energy Calculator",
     "AI Energy Advisor"]
)
# -----------------------------------
# MENU MANIPULATION
# -----------------------------------
if menu == "Home":
    show_home()

elif menu == "Energy Dashboard":
    show_energy_dashboard()

elif menu == "Appliance Manager":
    show_appliance_manager()

elif menu == "Energy Calculator":
    show_energy_calculator()

elif menu == "AI Energy A dvisor":
    st.write("Coming soon")


# -----------------------------------
# FOOTER
# -----------------------------------
st.divider()
st.caption("Household Energy Advisor 2026- Group 15")