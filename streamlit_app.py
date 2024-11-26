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
        "image": "mtp://Unisoc_itel_P55_11892193BS002243/Internal%20shared%20storage/Pictures/Remini"  # Replace with your image path or URL
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
    
    # Display the image
    if "image" in post:
        st.image(post["image"], caption="This is an image of Adam Rey G. Aloni", use_column_width=True)
    
    st.markdown("---")
