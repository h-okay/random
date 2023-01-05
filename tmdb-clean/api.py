import grequests  # must import first because of monkey patch
import requests


class APICalls:
    def __init__(
        self, api_key: str, session: requests.Session, req_size, page_size
    ) -> None:
        self.api_key = api_key
        self.session = session
        self.req_size = req_size
        self.page_size = page_size

    @property
    def movie_ids(self):
        return self.get_movie_ids(self.req_size, self.page_size)

    @staticmethod
    def page_chunks(length, chunk_size):
        for i in range(0, length):
            start = i * chunk_size if i > 0 else 1
            end = (i + 1) * chunk_size
            yield range(start, end)

    @staticmethod
    def id_chunks(id_list, chunk_size):
        for i in range(0, len(id_list)):
            start = i * chunk_size if i > 0 else 1
            end = (i + 1) * chunk_size
            yield id_list[start:end]

    def get_movie_ids(self, req_size=10, page_size=20):
        url = "https://api.themoviedb.org/3/movie/top_rated?api_key={}&language=en-US&page={}"

        responses = []
        for page_chunk in APICalls.page_chunks(req_size, page_size):
            urls = [url.format(self.api_key, page) for page in page_chunk]
            reqs = (grequests.get(url=url, session=self.session) for url in urls)
            responses += grequests.map(reqs)

        data = [
            response.json().get("results")
            for response in responses
            if response.status_code == 200
        ]
        return [movie.get("id") for page in data for movie in page]

    def get_movie_details(self, req_size=10):
        url = "https://api.themoviedb.org/3/movie/{}?api_key={}"

        responses = []
        for id_chunk in APICalls.id_chunks(self.movie_ids, req_size):
            urls = [url.format(id, self.api_key) for id in id_chunk]
            reqs = (grequests.get(url=url, session=self.session) for url in urls)
            responses += grequests.map(reqs)

        details = [
            response.json() for response in responses if response.status_code == 200
        ]
        return details
