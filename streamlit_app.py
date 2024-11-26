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
        "image": "https://scontent.fcgy2-1.fna.fbcdn.net/v/t39.30808-6/433417706_438975722037143_7625983037556897230_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=a5f93a&_nc_eui2=AeHFI0B3-Gc3ddOZxWgAOcWlBuJ-k46bmwkG4n6TjpubCWb6n4z6t6wzehcx9aBN2wOZ3N9e0TkbzC4LNji6Kbnf&_nc_ohc=4OvX5EqjfN4Q7kNvgFXz1b0&_nc_zt=23&_nc_ht=scontent.fcgy2-1.fna&_nc_gid=AcRACG3qb9nuvuwI9Dzp60I&oh=00_AYD27O7IqnwNsNfNX36GwVH1UrBBq18_ylCYR20Q5hPBMw&oe=674B4C7B"  # Sample image URL
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
        st.image(post["image"], width=150, height=150)  # 1:1 aspect ratio without caption
    
    st.markdown("---")
