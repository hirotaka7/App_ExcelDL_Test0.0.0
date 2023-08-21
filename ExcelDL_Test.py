import streamlit as st
import pandas as pd
import numpy as np
import zipfile
from io import BytesIO
from xlsxwriter import Workbook

st.set_page_config(layout="wide")
st.title('Excel Download Test')

d_Height=150

P_Code='アルファ'
df_A=pd.DataFrame(
    [
        [P_Code,P_Code,P_Code,P_Code],
        [P_Code,P_Code,P_Code,P_Code],
    ],
    columns=['col1','col2','col3','col4']
)
st.dataframe(df_A,height=d_Height,use_container_width=True)

P_Code='Bravo'
df_B=pd.DataFrame(
    [
        [P_Code,P_Code,P_Code,P_Code],
        [P_Code,P_Code,P_Code,P_Code],
    ],
    columns=['col1','col2','col3','col4']
)
st.dataframe(df_B,height=d_Height,use_container_width=True)

P_Code='チャーリー'
df_C=pd.DataFrame(
    [
        [P_Code,P_Code,P_Code,P_Code],
        [P_Code,P_Code,P_Code,P_Code],
    ],
    columns=['col1','col2','col3','col4']
)
st.dataframe(df_C,height=d_Height,use_container_width=True)

st.download_button('DL Alpha(shift_jis) csv', df_A.to_csv(index=False).encode('shift-jis'),file_name='Alpha_jis.csv')
st.download_button('DL Alpha(utf-8) csv', df_A.to_csv(index=False).encode('shift-jis'),file_name='Alpha_utf8.csv')
def df_to_xlsx(df_A,df_B,df_C):
    byte_xlsx=BytesIO()
    writer_xlsx=pd.ExcelWriter(byte_xlsx, engine="xlsxwriter")
    df_A.to_excel(writer_xlsx,index=False,sheet_name="Alpha")
    df_B.to_excel(writer_xlsx,index=False,sheet_name="Bravo")
    df_C.to_excel(writer_xlsx,index=False,sheet_name="Charlie")
    writer_xlsx.close()
    out_xlsx=byte_xlsx.getvalue()
    return out_xlsx
out_xlsx=df_to_xlsx(df_A,df_B,df_C)
st.download_button('DL Excel',out_xlsx,file_name='Phonetic.xlsx')

# def xlsx_to_zip(df_A,df_B,df_C):
#     byte_xlsx=BytesIO()
#     writer_xlsx=pd.ExcelWriter(byte_xlsx, engine="xlsxwriter")
#     df_A.to_excel(writer_xlsx,index=False,sheet_name="Alpha")
#     df_B.to_excel(writer_xlsx,index=False,sheet_name="Bravo")
#     df_C.to_excel(writer_xlsx,index=False,sheet_name="Charlie")
#     writer_xlsx.close()
#     out_xlsx=byte_xlsx.getvalue()
#     return out_xlsx


def xlsx_to_zip(out_xlsx):
    zip_buf=BytesIO()
    with zipfile.ZipFile(zip_buf,'w',compression=zipfile.ZIP_DEFLATED) as new_zip:
        new_zip.writestr('Phonetic.xlsx',out_xlsx)
    out_zip=zip_buf.getvalue()
    return out_zip
out_zip=xlsx_to_zip(out_xlsx)
st.download_button('DL zip',out_zip,file_name='Phonetic.zip')
        







