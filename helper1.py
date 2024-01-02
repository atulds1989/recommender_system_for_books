import numpy as np 
import pandas as pd 

import pickle
import streamlit as st 


popular_books_df = pickle.load(open('popular_books_df.pkl','rb'))
pivot_df = pickle.load(open('pivot_df.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
cosine_similarity_scores = pickle.load(open('cosine_similarity_scores.pkl','rb'))



def top10():


    st.title('Book Recommender System')

    st.title("Top 10 popular movies")

    book_name = list(popular_books_df['Book-Title'].values)
    author=list(popular_books_df['Book-Author'].values)
    image=list(popular_books_df['Image-URL-M'].values)
    votes=list(popular_books_df['rating_count'].values)
    rating=list(popular_books_df['avg_ratings'].values)

    for i in range(20):
        st.write(f"### {book_name[i].capitalize()}")
        col1, col2, col3 = st.columns(3)
        
        with col2:
            st.image(image[i], use_column_width=True, caption="")
        
        with col1:
            st.subheader("Author:")
            st.text(author[i])
        
        with col3:
            st.subheader("Votes:")
            st.text(votes[i])
            
            st.subheader("Rating:")
            st.text(rating[i])



###################################
def recommend(book):
    try:
        index = np.where(pivot_df.index == book.lower())[0][0]
        
    except IndexError:
        st.error("Book not found. Please enter a valid book name.")
        return None

    similar_items = sorted(list(enumerate(cosine_similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pivot_df.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    return data


# book = st.text_input('Please enter the name of the book for which you would like to see similar books')

# submit = st.button('Get recommendation')

# if submit:
#     if not book:
#         st.error("Please enter book name")
#     else:
#         data = recommend(book=book)
#         if data:
#             for i in range(len(data)):
#                 st.column_width = 100
#                 col1 = st.columns(1)[0]  

#                 name = data[i][0] 
#                 author = data[i][1]
#                 url = data[i][2]   
                    
#                 with col1:
#                     st.image(url, use_column_width=False, caption=name, width=100) 
#                     st.text(f"book name : {name.capitalize()}")
#                     st.text(f"book author : {author}")


def footer():

    st.markdown("---")
    st.markdown("### About")
    st.markdown("This app recommends books based on user input and displays the top 10 popular books.")
    st.markdown("Developed by Your Name")