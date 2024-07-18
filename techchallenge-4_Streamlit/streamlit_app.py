import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.info(
    """
    - Web App URL: <https://techchallenge4-alexandresuehiro-zi9ej5yn9lgqhjfqgqw3mq.streamlit.app/>
    - GitHub repository: <https://github.com/alexandresuehiro/Postgrad_FIAP_3DTAT/tree/main/techchallenge-4_Streamlit>
    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
    Alexandre Suehiro: <https://wetlands.io>
    [GitHub](https://github.com/alexandresuehiro) | [Twitter](https://twitter.com/asuehiro) | [LinkedIn](https://www.linkedin.com/in/alexandre-suehiro-de-paula-e-silva-b3096218/)
    """
)

# Customize page title
st.title("Streamlit for Oil Pricing")

st.markdown(
    """
    This multipage app template demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and [leafmap](https://leafmap.org). It is an open-source project and you are very welcome to contribute to the [GitHub repository](https://github.com/giswqs/streamlit-multipage-template).
    """
)

st.header("Instructions")

markdown = """
1. For the [GitHub repository](https://github.com/giswqs/streamlit-multipage-template) or [use it as a template](https://github.com/giswqs/streamlit-multipage-template/generate) for your own project.
2. Customize the sidebar by changing the sidebar text and logo in each Python files.
3. Find your favorite emoji from https://emojipedia.org.
4. Add a new app to the `pages/` directory with an emoji in the file name, e.g., `1_🚀_Chart.py`.

"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
