import helper
import streamlit as st 

st.sidebar.title("Restaurant Name Generator")

book = st.sidebar.text_input('Please enter the name of the book for which you would like to see similar books')

submit = st.sidebar.button('Get recommendation')

if submit:
    if not book:
        st.error("Please enter book name")
    else:
        data = helper.recommend(book=book)
        if data:
            for i in range(len(data)):
                st.column_width = 100
                col1 = st.columns(1)[0]  

                name = data[i][0] 
                author = data[i][1]
                url = data[i][2]   
                    
                with col1:
                    st.image(url, use_column_width=False, caption=name, width=100) 
                    st.text(f"book name : {name.capitalize()}")
                    st.text(f"book author : {author}")


