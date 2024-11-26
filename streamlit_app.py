import streamlit as st
import pandas as pd

# Create a logo for the blog with a gradient from white to black
st.markdown(
    """
    <h1 style="text-align: center; background: linear-gradient(to right, white, black); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Adam's Blog</h1>
    """,
    unsafe_allow_html=True
)

# Blog posts data
blog_posts = [
    {
        "content": [
            ("Name", "Adam Rey G. Aloni"),  # Included name in content
            ("Age", "19 years old"),
            ("Gender", "Male"),
            ("Birthdate", "October 27, 2005"),
            ("Birthplace", "Quiapo, Manila"),
            ("Permanent Address", "Purok 4 Bonifacio, Ritaglenda, Basilisa, Dinagat Islands"),
            ("Current Address", "Quiapo, Manila"),
        ],
        "image": "https://scontent.fcgy2-4.fna.fbcdn.net/v/t39.30808-6/447232820_485701057364609_6882034262964220786_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=a5f93a&_nc_eui2=AeHjriIDTRJC_PcvJAfgIouOFYiAgsWwUSoViICCxbBRKheimFO4y58FaaCHAq9X9ZazI6GTSJfowGXCwAWihCGQ&_nc_ohc=BKxVkhXz20EQ7kNvgHPdImd&_nc_zt=23&_nc_ht=scontent.fcgy2-4.fna&_nc_gid=Ai8oJezuBIWDV3zOmo6nf18&oh=00_AYC8O_UH06Ya04GiX9_yRbtBH9FcVgi15JusViQXFAD3pQ&oe=674B3112"  # Sample image URL
    }
]

# Display blog posts
for post in blog_posts:
    # Display the image
    if "image" in post:
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center;">
                <img src="{post['image']}" style="width: 250px; height: 250px; object-fit: cover;" />
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    # Title for the content section
    st.subheader("About Me")  # Added title for the content section
    
    # Display content in a structured format
    for item in post["content"]:
        st.write(f"**{item[0]}:** {item[1]}")
    
    st.markdown("---")
    
    # Title for interests/hobbies section
    st.subheader("Interests & Hobbies")  # Added title for interests/hobbies section
    
    # List of interests and hobbies
    interests = [
        "Baseball",
        "Badminton",
        "Gaming (specifically: Role Playing Games, Casual Games, and Fast-Paced Competitive Games)",
        "Reading (specifically self-help books)"
    ]
    
    # Display each interest as a bullet point
    for interest in interests:
        st.write(f"- {interest}")
    
    st.markdown("---")
    
    # Title for School Attended section
    st.subheader("School Attended")  # Title for the school attended section
    
    # Create a DataFrame for the schools attended
    school_data = {
        "Level": [
            "Elementary Schools Attended",
            "Grade 1-3",
            "Grade 4-5",
            "Grade 6",
            "High Schools Attended",
            "Grade 7-8",
            "Grade 9-10",
            "Senior High Schools Attended",
            "Grade 11-12"
        ],
        "School": [
            "",
            "Blessed Christian School De Sta Rosa",
            "Elementary School Central 2",
            "Blessed Christian School De Sta. Rosa",
            "",
            "Blessed Christian School De Sta. Rosa",
            "Ritaglenda National Highschool",
            "",
            "Don Jose Ecleo Memorial College"
        ]
    }

    # Convert the dictionary to a DataFrame
    school_df = pd.DataFrame(school_data)

    # Display the DataFrame as a table
    st.table(school_df)

    st.markdown("---")

    # Title for Achievements section
    st.subheader("Achievements")  # Title for the achievements section

    # List of achievements
    achievements = [
        {
            "title": "Certificate of Completion",
            "description": "Awarded for completing a course or program.",
            "image": "https://4b8e914bcf.cbaul-cdnwnd.com/8cbb878a5a782afad9cfd136a77e20c1/200000005-0e0360e037/CamScanner%2011-26-2024%2010.19%20%281%29_6.webp?ph=4b8e914bcf"  # Replace with your image path or URL
        },
        {
            "title": "OJT Certificate of Completion",
            "description": "Awarded for completing an on-the-job training program.",
            "image": "https://4b8e914bcf.cbaul-cdnwnd.com/8cbb878a5a782afad9cfd136a77e20c1/200000007-55f4855f4a/CamScanner%2011-26-2024%2010.19%20%281%29_5.webp?ph=4b8e914bcf"  # Replace with your image path or URL
        },
        {
            "title": "Certificate of Merit (Graduated With Honor)",
            "description": "Awarded for graduating with honors.",
            "image": "https://4b8e914bcf.cbaul-cdnwnd.com/8cbb878a5a782afad9cfd136a77e20c1/200000009-6b1c46b1c7/CamScanner%2011-26-2024%2010.19%20%281%29_4.webp?ph=4b8e914bcf"  # Replace with your image path or URL
        }
    ]

    # Display each achievement
    for achievement in achievements:
        st.write(f"**{achievement['title']}**: {achievement['description']}")

        # Display the achievement image without circular styling
        if "image" in achievement:
            st.markdown(
                f"""
                <div style="display: flex; justify-content: center;">
                    <img src="{achievement['image']}" style="width: 400px; height: 300px; object-fit: cover;" />
                </div>
                """, 
                unsafe_allow_html=True
            )
        st.markdown("---")  # Separator for achievements
