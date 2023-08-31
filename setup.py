from setuptools import setup


def get_long_description():
    """
    Return the README.
    """
    return open("README.md", "r", encoding="utf8").read()


setup(
    name="jaccount-auth",
    version="0.0.1",
    url="https://github.com/linsyking/jaccount-auth",
    license="MIT",
    description="A small plugin to help use jaccount login in python programs.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="linsyking",
    author_email="xiangyiming2002@gmail.com",
    maintainer="linsyking",
    maintainer_email="xiangyiming2002@gmail.com",
    packages=["jaccount_auth"],
    include_package_data=True,
    project_urls={
        "Bug Reports": "https://github.com/linsyking/jaccount-auth/issues",
        "Source": "https://github.com/linsyking/jaccount-auth",
    },
    install_requires=[
        "aiohttp",
        "beautifulsoup4",
        "pillow",
    ],
)
