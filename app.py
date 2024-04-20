import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def plot_iv_curve(data):
    fig, ax = plt.subplots()
    ax.plot(data['Voltage'], data['Current'])
    ax.set_xlabel('Voltage (V)')
    ax.set_ylabel('Current (A)')
    ax.set_title('IV Curve')
    st.pyplot(fig)

def main():
    st.sidebar.title('Analysis')
    st.sidebar.write('This app displays an IV curve.')

    st.title('IV Curve Analysis')

    uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

    if uploaded_file is not None:
        try:
            data = pd.read_excel(uploaded_file)
            st.write(data.head())
            plot_iv_curve(data)
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
