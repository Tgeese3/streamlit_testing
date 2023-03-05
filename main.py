import streamlit as st
from PIL import Image
import time

st.title('streamlit Begin')
st.write('Display image')

'start!'

latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!'

if st.checkbox('Show Image'):
    img = Image.open('influencer.jpg')
    st.image(img, caption='Nogizaka 46', use_column_width=True  )