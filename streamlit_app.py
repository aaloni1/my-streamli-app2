import streamlit as st

# Sample blog posts data
blog_posts = [
    {
        "title": "The Benefits of Streamlit",
        "content": """
        Streamlit is an open-source app framework for Machine Learning and Data Science projects. 
        It allows you to create beautiful web apps for your machine learning projects with minimal effort. 
        You can turn data scripts into shareable web apps in minutes, all in pure Python.
        """,
        "author": "John Doe",
        "date": "2023-10-01"
    },
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
st.title("My Blog")

# Display blog posts
for post in blog_posts:
    st.subheader(post["title"])
    st.write(f"**By {post['author']} on {post['date']}**")
    st.write(post["content"])
    st.markdown("---")

# Comment section
st.subheader("Leave a Comment")
comment = st.text_area("Your Comment:")
if st.button("Submit Comment"):
    if comment:
        st.success("Thank you for your comment!")
    else:
        st.error("Please enter a comment before submitting.")

# Note: In a real application, you would want to save comments to a database or file.
