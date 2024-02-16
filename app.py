import streamlit as st
import pandas as pd


popular_df = pd.read_pickle("popular.pkl")
pt = pd.read_pickle('pt.pkl')
similarity_score = pd.read_pickle('similarity_score.pkl')
book = pd.read_pickle('book.pkl')

st.title("Collaborative Filtering based Book Recommendation System")

def recommend(name):
    index = np.where(pt.index == name)[0][0]
    similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:10]
    data = []
    for i in similar_items:
        temp = book.loc[book["Book-Title"] == pt.index[i[0]]]
        item = {
            'Book-Title': temp.iloc[0]['Book-Title'],
            'Book-Author': temp.iloc[0]['Book-Author'],
            'Image-URL-L': temp.iloc[0]['Image-URL-L'],

        }
        data.append(item)

    num_rows = (len(data) + 3) // 4


    for i in range(num_rows):

        row_start = i * 4
        row_end = min((i + 1) * 4, len(data))
        cols = st.columns(4)
        for k in range(row_start, row_end):
            with cols[k % 4]:
                st.image(data[k]['Image-URL-L'])
                st.write("Book Title:", data[k]['Book-Title'])
                st.write("Book Author:", data[k]['Book-Author'])
                st.write("---")


title = st.text_input("Book Title")
if title:
    recommend(title)


st.header('Top Books')


num_rows = (len(popular_df) + 3) // 4

for i in range(num_rows):

    row_start = i * 4
    row_end = min((i + 1) * 4, len(popular_df))
    cols = st.columns(4)
    for j in range(row_start, row_end):
        with cols[j % 4]:
            st.image(popular_df.iloc[j]['Image-URL-L'])
            st.write("Book Title:", popular_df.iloc[j]['Book-Title'])
            st.write("Book Author:", popular_df.iloc[j]['Book-Author'])
            st.write("No. of Ratings:", popular_df.iloc[j]['num_rating'])
            st.write("Average Rating:", popular_df.iloc[j]['avg_rating'])
            st.write("---")
