import streamlit as st
from streamlit_ace import st_ace
from pathlib import Path
import os
from PIL import Image
from memory_profiler import profile

import pandas as pd

# -- Set page config
apptitle = 'Code Quality Check'
image = Image.open('/home/kevin/PycharmProjects/Codes_Quality_Check/Hi-PARIS_EngineeringTeam_Fond_Blanc_Moyen.JPG')
st.set_page_config(page_title=apptitle, page_icon=image,layout="wide")
st.image(image, width=500)



# -- Default detector list
detectorlist = ['H1','L1', 'V1']



st.title("Code Quality Check ")

# uploaded_files = st.file_uploader("Choose a python scripts", accept_multiple_files=True, type=["py"])
# for uploaded_file in uploaded_files:
#     bytes_data = uploaded_file.read()
#     st.write("filename:", uploaded_file.name)
#     st.write(bytes_data)

st.sidebar.title("Choice of a profiling tool")

apps = ["Line Profiler", "Memory Profiler", "Graphviz" ]

check_boxes = [st.sidebar.checkbox(app, key=app) for app in apps]

st.write([app for app, checked in zip(apps, check_boxes) if checked])

checked_apps = [app for app, checked in zip(apps, check_boxes) if checked]

if st.button("Download data"):
    for app in checked_apps:
        download_data(app) # <-- download data with requests for example for this stock




# app_mode = st.sidebar.selectbox("Choose the app mode",
#                                 ["flake8", "line_profiler", "memory_profiler"])
#
# if app_mode == "flake8":
#     st.sidebar.success("To continue selecting your python scripts")
#     uploaded_files = st.file_uploader("Choose a python scripts", accept_multiple_files=True, type=["py"])
#
#     if uploaded_files is not None:
#
#         if st.button("Process"):
#
#             for file in uploaded_files:
#
#                 file_details = {"filename": file.name, "filetype": file.type,
#                                 "filesize": file.size}
#
#                 st.write(file_details)
#
#             with open(os.path.join("/home/kevin/FileDir", file.name), "wb") as f:
#
#                 f.write((file).getbuffer())
#
#             st.success('File Saved')
#
# elif app_mode == "line_profiler":
#
#     st.sidebar.success("To continue selecting your python scripts")
#
#     uploaded_files = st.file_uploader("Choose a python scripts", accept_multiple_files=True, type=["py"])
#
#     if uploaded_files is not None:
#
#         if st.button("Process"):
#
#             for file in uploaded_files:
#
#                 file_details = {"filename": file.name, "filetype": file.type,
#                                 "filesize": file.size}
#
#                 st.write(file_details)
#
#             with open(os.path.join("/home/kevin/FileDir", file.name), "wb") as f:
#
#                 f.write((file).getbuffer())
#
#             st.success('File Saved')
#
# elif app_mode == "memory_profiler":
#     st.sidebar.success("To continue selecting your python scripts")
#     uploaded_files = st.file_uploader("Choose a python scripts", accept_multiple_files=True, type=["py"])
#
#     if uploaded_files is not None:
#
#         if st.button("Process"):
#
#             for file in uploaded_files:
#                 file_details = {"filename": file.name, "filetype": file.type,
#                                 "filesize": file.size}
#                 st.write(file_details)
#
#             with open(os.path.join("/home/kevin/FileDir", file.name), "wb") as f:
#                 f.write((file).getbuffer())
#             st.success('File Saved')

st.markdown("## Input")
code = st_ace(language='python',
              theme='xcode')
with open('readme.txt', 'w') as f:
    f.write(code)
p = Path('readme.txt')
p.rename(p.with_suffix('.py'))
os.system("flake8 --statistics readme.py > flake8_output.txt")

if code != "":
    st.markdown("## Output")
    # st.markdown("``` python\n"+code+"```")
    with open('flake8_output.txt') as f:
        lines = f.readlines()

    st_ace(value=lines,
           language='python',
           theme='pastel_on_dark',
           readonly=True)

    for i in lines:
        st.info(i)

    text = st.write(lines)





st.subheader("About this app")
st.markdown(""" This app displays report from Flake8, LineProfiler, and MemoryProfiler downloaded from GitHub. """)