import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser

st.set_page_config(page_title="Web Scraper")
st.markdown("<h1 style='text-align: center;'>Web Scraper</h1>",unsafe_allow_html=True)
# st.image("https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=100&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 100w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=200&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 200w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=300&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 300w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 400w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 500w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 600w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 700w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 800w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 900w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 1000w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=1200&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 1200w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=1400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 1400w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=1600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 1600w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=1800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 1800w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=2000&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 2000w")

with st.form("Search"):
    keyword=st.text_input("Enter your Search: RK")
    search=st.form_submit_button("Submit")
placeholder=st.empty()
if keyword:
    page=requests.get(f"https://unsplash.com/s/photos/{keyword}")
    print(page.status_code)
    soup=BeautifulSoup(page.content, 'lxml')
    rows=soup.find_all("div", class_="d95fI")
    # print(len(rows))
    col1,col2=placeholder.columns(2)
    for index,row in enumerate(rows):
        figures=row.find_all("figure")
        # print(figures)
        for i in range(2):
            img=figures[i].find("img", class_="ApbSI z1piP vkrMA")
            list=img['src'].split('?')
            anchor=figures[i].find("a", class_="Prxeh")
            # print(anchor['href'])
            if i==0:
                col1.image(list[0])
                btn=col1.button("Download", key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com/"+anchor['href'])
            else:
                col2.image(list[0])
                btn=col2.button("Download", key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com/"+anchor['href'])