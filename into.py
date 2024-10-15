import streamlit as st
import pickle
import pandas as pd


movies = pickle.load(open("movies1.pk1" , "rb"))
movies = pd.DataFrame(movies)
similar = pickle.load(open("similar.pk1" , "rb"))


def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://png.pngtree.com/thumb_back/fh260/background/20210902/pngtree-film-festival-black-atmospheric-background-image_784970.jpg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function to add background image
add_bg_from_url()


def recommend(moviee):
  movie_index = movies[movies["title"] == moviee].index[0]
  distance = similar[movie_index]
  movie_list = sorted(list(enumerate(distance)) , reverse = True , key = lambda x:x[1])[1:6]
  
  rm = []
  for i in movie_list:
    rm.append(movies.iloc[i[0]].title)
  return rm

st.title("Movie Recomemmendation System")
options = st.selectbox(
    'Write Your Favourite movie',
    movies["title"].values
)

if st.button("Recommand Movie"):
    a = recommend(options)
    for i in a:
        st.write(i)



