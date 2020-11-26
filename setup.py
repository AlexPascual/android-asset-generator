import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="android-asset-generator", # Replace with your own username
    version="1.0.6",
    author="Alejandro Pascual",
    author_email="alex_paz_5599@hotmail.com",
    description="A simple android assets generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/android-asset-generator/",
    packages=setuptools.find_packages(),
    entry_points ={
            'console_scripts': [
                'android-asset-generator = generator.gen:main'
            ]
        },
    install_requires=[
          'python-resize-image',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
