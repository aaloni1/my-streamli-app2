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
       "image": "https://scontent.fcgy2-4.fna.fbcdn.net/v/t39.30808-6/447232820_485701057364609_6882034262964220786_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=a5f93a&_nc_eui2=AeHjriIDTRJC_PcvJAfgIouOFYiAgsWwUSoViICCxbBRKheimFO4y58FaaCHAq9X9ZazI6GTSJfowGXCwAWihCGQ&_nc_ohc=BKxVkhXz20EQ7kNvgHPdImd&_nc_zt=23&_nc_ht=scontent.fcgy2-4.fna&_nc_gid=Ai8oJezuBIWDV3zOmo6nf18&oh=00_AYC8O_UH06Ya04GiX9_yRbtBH9FcVgi15JusViQXFAD3pQ&oe=674B3112"  # Replace with your image path or URL
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
