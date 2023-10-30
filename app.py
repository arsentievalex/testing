import streamlit as st
import pickle
import os

st.set_page_config(page_title="test", page_icon="📝", layout="wide", menu_items=None)



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

#dot.render('decision_tree', view=False)

st.graphviz_chart(dot, use_container_width=True)


