import streamlit as st
st.title("Gross Salary Calculator")
bsal = st.number_input("Enter your Basic Salary: ",min_value=0,step=1)
if st.button("Calculate Gross Salary"):
    hra,da = (0.67*bsal,0.73*bsal) if bsal<10000 else (0.69*bsal,0.76*bsal) if bsal<20000 else (0.73*bsal,0.8*bsal)
    gs = bsal+hra+da
    st.success(f"Gross salary:{gs:.2f} ")
