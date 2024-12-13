import streamlit as st
st.title('EVEN OR ODD')
num1 = st.number_input('Enter number',min_value=0,step=1)
if st.button('Even/odd'):
    if num1 % 2 == 0:
        st.success('Even Number')
    else:
        st.error('odd Number')