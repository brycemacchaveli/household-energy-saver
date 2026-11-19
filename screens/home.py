import streamlit as st
def show_home():
    st.title("Welcome to the Household Energy Advisor App")
    st.markdown(
    """
    Does your household face challenges in keeping the monthly JPS bills at a low price?
    Many households receive their monthly Jamaica Public Service (JPS) bill without knowing which appliances are driving up the cost.

    Why This App Matters:
    - See Where Your Money Goes: Break down your JPS bill into exact Jamaican dollars (J$) per appliance.
    - Simulate Savings: Test "What-If" scenarios before changing your daily habits.
    - Get Smart Alerts & AI Advice: Receive reminders to turn off heavy appliances and ask our AI Advisor for customized tips.
    """
    )
    st.divider()
    st.subheader("How to Navigate the App")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.info("Step 1: Sidebar\n\nEnter your actual JPS monthly bill (J$), kWh used, and rate per kWh.")
    
    with c2:
        st.info("Step 2: Appliance Manager\n\nSelect household appliances, convert Volts/Amps to Watts, and save your list.")
    
    with c3:
        st.info("Step 3: Dashboard & What-If\n\nView cost histograms, find your #1 energy hog, and test reduction.")
    
    with c4:
        st.info("Step 4: AI Advisor\n\nGet 10 tailored energy-saving tips, advice and ask questions.")
    
    st.divider()
    st.subheader("Electrical Safety Education for Jamaican Households")

    st.write("Saving energy goes hand-in-hand with keeping your family safe from electrical hazards:")
    
    st.write("Tip 1: Do not attempt DIY electrical fixes or wiring changes: \n " \
    "Only hire licensed or registered electricians for home repairs, wiring checks, and appliance installations.")
   
    st.write("Tip 2: Use Surge Protectors: \n" \
    "Protect valuable electronics—such as televisions, refrigerators, computers, and " \
    "sound systems with good quality surge protectors to defend against low voltage power spikes.")
    
    st.write("Tip 3: Childproof Outlets and Cords: \n" \
    " Cover wall outlets, keep electrical cords out of the reach of children,"
    " and teach children never to stick objects into sockets or touch exposed wires.")
   
    st.write("Tip 4: Watch for Warning Signs: \n" \
    "Unplug devices immediately if they spark, smoke, or make buzzing noises.")
   