from movie import Movie
from comedy import Comedy
from ranking_generator import RankingGenerator


def run_movie_example():
    funny_movie = Movie("Funny Movie", "Comedy")
    funny_movie.vote("Dominik", rate=5)
    funny_movie.vote("Karola", rate=4)
    print(funny_movie)

    # print(funny_movie._rates)
    # print(funny_movie.__viewers)
    # print(funny_movie._Movie__viewers)


def run_ranking_example():
    funny_movie = Movie("Funny Movie", "Comedy")
    funny_movie.vote("Dominik", rate=5)
    funny_movie.vote("Karola", rate=4)

    scary_movie = Movie("Scary House", "Horror")
    scary_movie.vote("Dominik", rate=4)
    scary_movie.vote("Karola", rate=3)

    RankingGenerator.generate_ranking([funny_movie, scary_movie])


def run_comedy_example():
    fun_movie = Comedy("Fun Movie")
    fun_movie.vote("Dominik", rate=5)
    fun_movie.vote("Karola", rate=4)
    print(fun_movie)


if __name__ == "__main__":
    run_movie_example()
    run_ranking_example()
    run_comedy_example()