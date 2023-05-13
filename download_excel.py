import streamlit as st
import pandas as pd
import io

# buffer to use for excel writer
buffer = io.BytesIO()

df = pd.read_csv("tips.csv")
df = df[["total_bill","tip","sex"]].head(10)
# print(df)

# st.write(df)
cell_hover = {
    "selector": "td:hover",
    "props": [("background-color", "#FFFFE0")]
}
index_names = {
    "selector": ".index_name",
    "props": "font-style: italic; color: darkgrey; font-weight:normal;"}
headers = {
    "selector": "th:not(.index_name)",
    "props": "background-color: #800000; color: white; text-align: center"
}
properties = {"border": "1px solid black", "width": "65px", "text-align": "center"}

df.style.format(precision=2).set_table_styles([cell_hover, index_names, headers]).set_properties(**properties)
# st.dataframe(df.style.set_table_styles())
st.table(df)

# Download as excel button
with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
    # Write each dataframe to a different worksheet.
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    # Close the Pandas Excel writer and output the Excel file to the buffer
    writer.save()

    download2 = st.download_button(
        label="Download data as Excel",
        data=buffer,
        file_name='Data.xlsx',
        mime='application/vnd.ms-excel'
    )
