from exceptions import InvalidRateValue
from movie import Movie


def run_error_handling_example():
    funny_movie = Movie("Funny movie", "Comedy")
    viewer_name = input("What is your name: ")

    while True:
        rate = int(input("Rate the movie (1-5): "))
        try:
            funny_movie.vote(viewer_name, rate)
        except InvalidRateValue as error:
            print(error)
            print("Try again...")
        else:
            print("Your vote has been saved")
            break
        finally:
            print("Its great that you are voting!")


if __name__ == "__main__":
    run_error_handling_example()