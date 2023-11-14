import streamlit as st


def square_feet():
    length = st.session_state['feet']
    width = st.session_state['width']
    results = length * width
    return results


st.text('Get Square Feet')
st.number_input('Enter Length', key='feet', step=1)
st.number_input('Enter width:', key='width', step=1)

total = square_feet()
display = st.write(f'{total}sq')
st.button('Results')

