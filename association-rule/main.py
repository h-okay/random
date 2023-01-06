import os

import click


@click.command()
@click.option(
    "--username",
    required=True,
    prompt="Your username",
    help="The username to authenticate with.",
)
@click.option(
    "--key",
    required=True,
    prompt="Your key",
    help="Kaggle api key to authenticate with.",
)
def main(username, key):
    os.environ["KAGGLE_USERNAME"] = username
    os.environ["KAGGLE_KEY"] = key
    from arl import AssociationRuleLearner  # pylint: disable=import-outside-toplevel

    arl = AssociationRuleLearner()
    arl.run()


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
