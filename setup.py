from setuptools import setup, find_packages
setup(
    name='mcqgenerator',
    version='0.1.0',
    author='Jitender',
    packages=find_packages(),
    install_requires=[
        'openai',
        'pandas',
        'langchain',
        'streamlit',
        'python-dotenv',
        'PyPDF2'
    ]
)