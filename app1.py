import helper1
import streamlit as st 


from streamlit_option_menu import option_menu


with st.sidebar:
    
    selected = option_menu('Book Recommender System',
                          
                          ['Top 20 books',
                           'recommend similar books'],
                          icons=['book', 'book'],
                          default_index=0)
    
    

if (selected == 'Top 20 books'):
    
    st.title('Top 20 books')
    helper1.top10()
    helper1.footer()
    

if (selected == 'recommend similar books'):
    
    book = st.text_input('Please enter the name of the book for which you would like to see similar books')

    submit = st.button('Get recommendation')


    if submit:
        if not book:
            st.error("Please enter book name")
        else:
            data = helper1.recommend(book=book)
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
    helper1.footer()
        

            

