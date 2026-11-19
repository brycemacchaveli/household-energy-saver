import streamlit as st
import pandas as pd

def show_energy_dashboard():
    st.title("Energy Dashboard")
    st.write("Here you can visualize your energy consumption, costs and potential savings.")

    if "appliances" not in st.session_state or len(st.session_state.appliances)== 0:
        st.warning("No appliances added as yet")
        return

    elec_rate=st.number_input("Enter electricity rate ($ per kWh): ",
                              min_value= 0.01, value=55.0)
    reduction=st.slider("Enter target usage reduction (%): ",
                        min_value=1,
                        max_value= 50)
    
    appliances= st.session_state.appliances
    dashboard_data= []

    total_kwh=0
    total_cost=0
    total_savings=0

    highest_name = ""
    highest_cost= 0

    for item in appliances:
        #formula for monthly kwh= kwh * quantity * hours per day * 30 days
        monthly_kwh= item["kilowatts per hour"] * item["quantity"] * item["hours"] * 30
        monthly_cost= monthly_kwh * elec_rate
        cost_per_item= monthly_cost / item["quantity"]
        savings= monthly_cost * (reduction/100)

        total_kwh= total_kwh + monthly_kwh
        total_cost= total_cost + monthly_cost
        total_savings= total_savings + savings

        if monthly_cost > highest_cost:
            highest_cost= monthly_cost
            highest_name= item["name"]

        dashboard_data.append({
            "Appliance": item["name"],
            "Quantity": item["quantity"],
            "Power (kwh) ": item["kilowatts per hour"],
            "Monthly (kwh)": round(monthly_kwh,2),
            "Cost per item": round(cost_per_item,2),
            "Total cost": round(monthly_cost, 2),
            "Potential Savings": round(savings,2)

        })
    col1,col2,col3,col4=st.columns(4)
    col1.metric("Monthly Usage", f"{total_kwh:.2f} kWh")
    col2.metric("Total Monthly Cost", f"${total_cost:.2f}")
    col3.metric("Highest Cost Appliance", highest_name, f"${highest_cost:.2f}", delta_color="off")# delta_color="off" gets rid of arrow on highest cost
    col4.metric("Potential Savings",f"${total_savings:.2f}")

    table=pd.DataFrame(dashboard_data) #converts dashboard_data into a dataframe for charts

    st.divider()
    st.subheader("User Monthly Consumption")
    st.bar_chart(table, x= "Appliance", y= "Monthly (kwh)")

    st.divider()
    st.subheader("Monthly cost and Potential Savings")
    st.bar_chart(table, x= "Appliance", y= ["Total cost", "Potential Savings"])

    st.divider()
    st.subheader("Cost Per Appliance Breakdown")
    st.dataframe(table, width='stretch', hide_index= True)



