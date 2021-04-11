from setuptools import setup, find_packages

with open('README.md', 'r') as readme_file:
    readme = readme_file.read()

setup(
    name='simple-flask-website-simulator',
    version='1.0.0',
    author='Ehsan Tabatabaei Yazdi',
    author_email='etycomputergmail.com',
    description='This is a simple Flask application for simulation website delays.',
    long_description=readme,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/etycomputer/simple-flask-website-simulator',
    install_requires=['pytest'],
    tests_require=['selenium', 'beautifulsoup4'],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
    ],
    python_requires='>=3.8.1',
)
