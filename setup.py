import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vit-tensorflow", # Replace with your own username
    version="0.0.1",
    author="Kim",
    author_email="",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/johnypark/vit-tensorflow",
    packages=setuptools.find_packages(),
    install_requires = ['tensorflow',
                       'tensorflow-addons',
                       'einops',
                        'typeguard'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

