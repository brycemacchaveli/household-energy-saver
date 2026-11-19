import streamlit as st
import pandas as pd

def show_appliance_manager():
    st.title("Appliance Manager")
    st.write("Here you can add or remove appliances.")

    if "appliances" not in st.session_state:
        st.session_state.appliances= []

    # -----------------------------------
    # ADD NEW APPLIANCE
    # -----------------------------------
    st.subheader("Add a new appliance")

    with st.form("for_appliance", clear_on_submit= True): # takes everything into one form (for_appliance : key name used to track form)
        name=st.text_input("Enter appliance name: ")

        quantity=st.number_input("Enter quantity of item: ",
                                 min_value=1)

        kilowatts=st.number_input("Enter appliance kilowatts per hour: ",
                             min_value=0.01)

        hours= st.number_input("Enter hours run: ",
                               min_value=0.1,
                               max_value=24.0)

        submitted=st.form_submit_button("Add appliance")

    # save appliance to appliances
    if submitted:
        if name.strip() == "":
            st.error("Please enter an appliance name. ")
        else:
            appliance= {
               "name": name,
               "quantity": quantity,
               "kilowatts": kilowatts,
               "hours": hours
                }
            st.session_state.appliances.append(appliance)
            st.rerun()

    #create a table using pandas
    st.divider()
    st.subheader("All Appliances")
    appliances=st.session_state.appliances

    if len(appliances)> 0:  #validation
        table =pd.DataFrame(appliances)
        table.columns=[
            "Appliances",
            "Quantity",
            "Kilowatts",
            "Hours"
        ]

        st.dataframe(
            table,
            width= 'stretch',
            hide_index=True # hides index column
        )

        #Delete Appliance
        st.subheader("Delete appliance")
        select=st.selectbox("Select an appliance to delete",
                            range(len(appliances)), #goes through each appliance return their index number
                            format_func=lambda i: f"{appliances[i]['name']} ({appliances[i]['kilowatts']}W, {appliances[i]['hours']} hrs)") #receives index number as i, searches index value
                                                                                                                                        #returns value stored under "name" etc. 

        if st.button ("delete"):
            st.session_state.appliances.pop(select)
            st.rerun()

    else:
        st.write("No appliances added") 




