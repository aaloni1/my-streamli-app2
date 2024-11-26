import streamlit as st

# Blog posts data
blog_posts = [
    {
        "title": "Adam Rey G. Aloni",
        "content": [
            ("Age", "19 years old"),
            ("Gender", "Male"),
            ("Birthdate", "October 27, 2005"),
            ("Birthplace", "Quiapo, Manila"),
        ],
        "author": "Adam Aloni",
        "date": "2023-10-01"
    },
    {
        "title": "Getting Started with Data Science",
        "content": [
            ("Overview", "Data Science is a field that uses scientific methods, processes, algorithms, and systems to extract knowledge and insights from structured and unstructured data."),
            ("Multi-Disciplinary", "It is a multi-disciplinary field that uses techniques from statistics, machine learning, and data analysis."),
        ],
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
    
    # Display content in a structured format
    for item in post["content"]:
        st.write(f"**{item[0]}:** {item[1]}")
    
    st.markdown("---")
