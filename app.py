import streamlit as st
import pickle
import os

st.set_page_config(page_title="test", page_icon="📝", layout="wide", menu_items=None)

page_bg_img = f"""
<style>
  /* Existing CSS for background image */
  [data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://i.postimg.cc/CxqMfWz4/bckg.png");
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
    background-attachment: local;
  }}
  [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
  }}

  /* New CSS to make specific divs transparent */
  .stChatFloatingInputContainer, .css-90vs21, .e1d2x3se2, .block-container, .css-1y4p8pa, .ea3mdgi4 {{
    background-color: transparent !important;
  }}
</style>
"""

sidebar_bg = f"""
<style>
[data-testid="stSidebar"]{{
    z-index: 1;
}}
</style>
"""


st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown(sidebar_bg, unsafe_allow_html=True)

st.title('GitHub Search')


from graphviz import Digraph

dot = Digraph(comment='Number Classifier', format='png')

# Node style settings
dot.attr('node', shape='ellipse', color='lightblue2', style='filled')

# Nodes for decision tree
dot.node('A', 'Input number: n')
dot.node('B', 'n > 0 ?')
dot.node('C', 'positive')
dot.node('D', 'n < 0 ?')
dot.node('E', 'negative')
dot.node('F', 'zero')

# Edges (connections between nodes)
dot.edge('A', 'B')
dot.edge('B', 'C', label='Yes')
dot.edge('B', 'D', label='No')
dot.edge('D', 'E', label='Yes')
dot.edge('D', 'F', label='No')

dot.render('decision_tree', view=False)

st.graphviz_chart(dot, use_container_width=True)


footer_html = """
    <div class="footer">
    <style>
        .footer {
            position: fixed;
            z-index: 2;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #283750;
            padding: 10px 20px;
            text-align: center;
        }
        .footer a {
            color: #4a4a4a;
            text-decoration: none;
        }
    </style>
        Made for Docker AI/ML Hackathon 2023. Powered by LlamaIndex and OpenAI.
    </div>
"""
st.markdown(footer_html, unsafe_allow_html=True)