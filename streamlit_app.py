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
        "image": ""  # Sample image URL
    }
]

# Title of the blog
st.title("Adam Aloni's Blog")

# Display blog posts
for post in blog_posts:
    st.subheader(post["title"])
    
    # Display content in a structured format
    for item in post["content"]:
        st.write(f"**{item[0]}:** {item[1]}")
    
    # Display the image with a 1:1 aspect ratio, without a caption
    if "image" in post:
        st.image(post["image"], width=400, height=300)  # 1:1 aspect ratio without caption
    
    st.markdown("---")
