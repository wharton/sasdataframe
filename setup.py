try:
    from setuptools import setup
except ImportError:
    from distuils.core import setup

setup(
        name="sasdataframe",
        version='0.0.3',
        description="Import a SAS dataset into a Pandas dataframe",
        author="Joe Dougherty",
        author_email="josepd@wharton.upenn.edu",
        url="http://www.upenn.edu",
        packages=['sasdataframe'],
        install_requires=['inlinesas'],
        )

