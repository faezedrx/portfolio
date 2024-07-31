import streamlit as st
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def main():
    st.set_page_config(page_title="portfolio", layout="centered")
    st.title("it's Faezeh Darbeheshti")

    # st.header("it's Faezeh Darbeheshti")
    st.write("Final Year Web Development Student | Tech Enthusiast | Lifelong Learner")
    st.write("my Email: faezeh.darbeheshti@gmail.com , [LinkedIn](https://linkedin.com/in/faezeh-darbeheshti-6a294824b) , [Github](https://github.com/faezedrx) ")


    sample_works = [
        {
            "title": "github portfolio",
            "description": "This project is a portfolio application for displaying GitHub repositories in a visually appealing manner using Streamlit",
            "image": "github-portfolio.jpg",
            "link": "https://app-portfolio.streamlit.app/"
        },
        {
            "title": "Calculator App",
            "description": "This is a simple calculator application built using Streamlit and Python",
            "image": "Calculator-App.jpg",
            "link": "https://calculator-app-st.streamlit.app/"
        },
        {
            "title": "Task Management",
            "description": "Task Management web application built with Streamlit",
            "image": "task-manage.jpg",
            "link": "https://webservicetaskmanagement-t5wape44rotg7hgijqfmgj.streamlit.app/"
        },
        {
            "title": "To Do app",
            "description": "To Do application that allows users to fetch random tasks, add them to a list, and manage their custom tasks with js",
            "image": "task-api.jpg",
            "link": "https://faezedrx.github.io/task-api/"
        },
        {
            "title": "Leisure Activities Survey",
            "description": "This project features a delightful survey form where users can cast their votes for their favorite pastimes using HTML, CSS, and JavaScript",
            "image": "Leisure.jpg",
            "link": "https://faezedrx.github.io/hob/"
        },
        {
            "title": "Tic Tac Toe Game",
            "description": "This is a simple implementation of the classic Tic-Tac-Toe game using HTML, CSS, and JavaScript.",
            "image": "Tic-Tac-Toe-Game.jpg",
            "link": "https://faezedrx.github.io/tic-tac-toe-game-js/"
        },
        {
            "title": "bamboo",
            "description": "A simple and efficient task management application built with PHP and MySQL, featuring user authentication, task scheduling, and email reminders.",
            "image": "bamboo-s.png",
            "link": "https://bamboo-services.ir/"
        },
        {
            "title": "Lottery App - with JS",
            "description": "This is a simple and fancy lottery application built with HTML, CSS, and JavaScript. You can add names to a list and then click the "Draw Lottery" button.",
            "image": "Lottery-App.jpg",
            "link": "https://faezedrx.github.io/lottery-app-js/"
        }
    ]

    st.markdown(
        """
        <style>
        .work-card {
            border: 1px solid #ccc;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            margin-bottom: 20px; /* فاصله بین کارت‌ها */
        }
        .work-card:hover {
            transform: scale(1.05);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .work-image {
            width: 100%;
            height: auto;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        .work-title {
            margin-bottom: 10px;
            font-size: 1.5em;
        }
        .work-description {
            margin-bottom: 10px;
            font-size: 1em;
        }
        .work-link {
            text-decoration: none;
            color: #0078FF;
            font-weight: bold;
            transition: color 0.3s ease;
        }
        .work-link:hover {
            color: #0056b3;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
    for i, work in enumerate(sample_works):
        column = col1 if i % 2 == 0 else col2

        image_base64 = get_base64_image(work['image'])

        with column:
            st.markdown(
                f"""
                <div class="work-card">
                    <img src="data:image/jpg;base64,{image_base64}" alt="work image" class="work-image">
                    <h2 class="work-title">{work['title']}</h2>
                    <p class="work-description">{work['description']}</p>
                    <a href="{work['link']}" target="_blank" class="work-link"> view more </a>
                </div>
                """,
                unsafe_allow_html=True
            )

if __name__ == "__main__":
    main()
