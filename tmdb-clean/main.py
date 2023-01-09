import click
from api import APICalls
from cleaner import Cleaner
from requests import Session


def main(api_key, pages):
    session = Session()
    raw_data = APICalls(api_key, session, 10, pages).get_movie_details(10)
    cleaner = Cleaner(raw_data)
    cleaner.filter_columns().fill_columns().unpack_columns()
    cleaner.data.to_csv("data.csv")


@click.command()
@click.option("--key", prompt="API Key", required=True, type=str, help="Your API key.")
@click.option(
    "--pages",
    prompt="How many pages",
    default=10,
    type=int,
    help="How many pages to be fetched.",
)
def run(key, pages):
    main(key, pages)


if __name__ == "__main__":
    run()  # pylint: disable=no-value-for-parameter
