import streamlit as st

def show_energy_calculator():
    st.title("Energy Calculator")
    st.write("Here you can estimate daily, monthly and yearly energy usage and JPS bill costs.")

    st.subheader("Enter appliance details and rates")
    col1,col2=st.columns(2)

    with col1:
        appliance_name=st.text_input("Enter appliance name: ")
        kilowatts= st.number_input("Enter appliance kilowatts: ",min_value=0.001, value=0.100, format="%.3f") #0.100 kw = 100 watts
        quantity= st.number_input("Enter quantity of item: ", min_value=1)

    with col2:
        hours=st.number_input("Enter hours used per day: ", min_value=0.0, max_value=24.0)
        days= st.number_input("Enter the number of days in billing cycle: ", min_value=1, max_value=366, value=30)
        rate= st.number_input("Enter JPS kilowatts per hour rate: ", min_value=0.01, value=55.5)

    #daily kilowatt formula= kilowatts * quantity * hours
    daily_kwh= kilowatts * quantity * hours
    monthly_kwh=daily_kwh * days
    yearly_kwh=daily_kwh * 365

    daily_cost= daily_kwh * rate
    monthly_cost=monthly_kwh * rate
    yearly_cost= yearly_kwh * rate

    st.divider()
    st.subheader(f"Estimated Usage and JPS Bill Cost for {appliance_name}")

    co1,co2,co3=st.columns(3, border=True)

    co1.metric("Daily Energy", f"{daily_kwh:.2f} kwh")
    co2.metric(f"Energy for {days} days", f"{monthly_kwh:.2f} kwh")
    co3.metric("Yearly Energy", f"{yearly_kwh:.2f} kwh")

    c1,c2,c3=st.columns(3, border= True)

    c1.metric("Daily Cost", f"${daily_cost:,.2f}")
    c2.metric(f"{days} Day JPS Bill", f"${monthly_cost:,.2f}")
    c3.metric(f"Yearly Cost", f"${yearly_cost:,.2f}")