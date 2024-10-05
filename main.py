import streamlit as st 
from scrape import scrape_website,split_dm_content,clean_body_content,extract_body_content
from parse import parse_with_ollama

st.set_page_config(page_title="AI Web Scraper", page_icon="🎈")
st.header("AI Web Scraper")
url= st.text_input("Enter url website")

if st.button("Scarpe Website"):
    st.spinner("Scraping the site")
    result=scrape_website(url)
    body_content=extract_body_content(result)
    cleaned_content=clean_body_content(body_content)

    st.session_state.dom_content= cleaned_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)

if "dom_content" in st.session_state:
    parse_description=st.text_area("Describe what you want to parser?")

    if st.button("Parse Content "):
        if parse_description:
            st.write("Parsing the content")

            dom_chunks=split_dm_content(st.session_state.dom_content)
            parsed_result=parse_with_ollama(dom_chunks,parse_description)
            st.write(parsed_result)