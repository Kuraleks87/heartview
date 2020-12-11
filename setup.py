from setuptools import setup, find_packages

with open("README.md", "r") as redme_file:
    readme = redme_file.read()

requriments = ["ipython>=6"]

setup(
      name="heartview",
      version ="0.0.1",
      author="Ivan Ivanov",
      author_email="ivan.ivanov@gmail.com",
      description="test",
      long_description = readme,
      long_description_content_type="text/markdown",
      url="https://github.com/Kuraleks87/heartview.git",
      packages=find_packages(),
      install_requires=requriments,
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
      python_requires='>=3.6',
)