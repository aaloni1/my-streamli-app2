import streamlit as st


blog_posts = [
    {
        "title": "Adam Rey G. Aloni",
        "content": """
      Age: 19 years old 
      Gender: Male
      Birthdate: October 27, 2005
      Birthplace: Quiapo, Manila""",
        }
    {
        "title": "Getting Started with Data Science",
        "content": """
        Data Science is a field that uses scientific methods, processes, algorithms, and systems 
        to extract knowledge and insights from structured and unstructured data. 
        It is a multi-disciplinary field that uses techniques from statistics, machine learning, and data analysis.
        """,
        "author": "Jane Smith",
        "date": "2023-10-05"
    }
]

# Title of the blog
st.title("Adam Aloni's Blog")

# Display blog posts
for post in blog_posts:
    st.subheader(post["title"])
    st.write(f"**By {post['author']} on {post['date']}**")
    st.write(post["content"])
    st.markdown("---")
