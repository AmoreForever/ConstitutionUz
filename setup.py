from setuptools import setup

__version__ = "1.0.1"


setup(
    name="ConstitutionUz",
    version=__version__,
    keywords=["constitution", "uzbekistan"],
    description="Constitution of the Republic of Uzbekistan.",
    author="AmoreForever",
    url="https://github.com/AmoreForever/ConstitutionUZ",
    author_email='me.thefarkhodov@gmail.com',
    license="MIT",
    project_urls={"Source": "https://github.com/AmoreForever/constitutionuz"},
    package_data={
        "ConstitutionUz": ["py.typed"],
    },
    requires=["requests", "bs4"]
)

