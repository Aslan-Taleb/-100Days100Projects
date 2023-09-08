from bs4 import BeautifulSoup
import requests
import re
import os
import random

FILE_MOVIES = "movies.txt"
FILE_MOVIES_WATCHED = "movies_watched.txt"


def from_html_to_string():
    if os.path.exists(FILE_MOVIES):
        with open(FILE_MOVIES, 'r', encoding="UTF-8") as f:
            website = f.read()
    else:
        html_to_string = requests.get(
            'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
        website = html_to_string.text
        with open(FILE_MOVIES, 'w', encoding="UTF-8") as f:
            f.write(website)
    soup = BeautifulSoup(website, "html.parser")
    return soup


def get_title(soup):
    titles = []
    all_titles = []
    result = soup.findAll('h3')
    for i in result:
        titles.append(i.getText('title'))
    for title in titles:
        title_text = re.sub(r'\d+\)', '', title).strip()
        all_titles.append(title_text)
    all_titles = all_titles[::-1]
    return all_titles


def welcome():
    print("What would you like to do?")
    print("1. Choose a movie")
    print("2. See movies you've already watched")
    print("3. Quit")
    choice = input("Enter your choice (1 or 2 or 3): ")
    return choice


def read_watched_movies_from_file():
    watched_movies = []
    try:
        with open(FILE_MOVIES_WATCHED, 'r', encoding="UTF-8") as f:
            for line in f:
                movie = line.strip()
                if movie:
                    watched_movies.append(movie)
    except FileNotFoundError:

        pass
    return watched_movies


def mark_movie_as_watched(movie):
    with open(FILE_MOVIES_WATCHED, 'a', encoding="UTF-8") as f:
        f.write(movie + '\n')


def choose_movie():
    # Check if movies file exists, and if so, read titles from file
    if os.path.exists(FILE_MOVIES):
        with open(FILE_MOVIES, 'r', encoding="UTF-8") as f:
            titles = [line.strip() for line in f.readlines()]
    else:
        print("Loading movies...")
        soup = from_html_to_string()
        titles = get_title(soup)
        with open(FILE_MOVIES, 'w', encoding="UTF-8") as f:
            for title in titles:
                f.write(title + '\n')

    unwatched_titles = [title for title in titles if title not in read_watched_movies_from_file()]
    if not unwatched_titles:
        print("You have watched all the available movies.")
        return None
    random_movie = random.choice(unwatched_titles)

    # Set up frame for displaying selected movie
    frame_width = 50
    movie_title = random_movie.center(frame_width-2)
    top_border = "╔" + "═" * (frame_width-2) + "╗"
    bottom_border = "╚" + "═" * (frame_width-2) + "╝"
    side_border = "║"
    message = "Do you want to watch this movie? [y/n]: "

    # Print frame and ask for user input
    print(top_border)
    print(side_border + movie_title + side_border)
    print(bottom_border)
    user_input = input(message).lower()

    # Respond to user input and mark movie as watched or not watched
    if user_input == "y":
        mark_movie_as_watched(random_movie)
        print(f"{random_movie} has been added to your watched movies.\n")
    elif user_input == "n":
        print(f"{random_movie} has not been added to your watched movies.\n")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

    return random_movie


def view_watched():
    watched_movies = read_watched_movies_from_file()
    if watched_movies:
        print("╔══════════════════════════════════════════════════════╗")
        print("║             Here are the movies you've watched         ║")
        print("╟────────────────────────────────────────────────────────╢")
        for i, movie in enumerate(watched_movies):
            print(f"║  {i+1}. {movie.ljust(50)}║")
        print("╚══════════════════════════════════════════════════════╝\n")
    else:
        print("You haven't watched any movies yet.\n")

