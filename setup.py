from setuptools import setup, find_packages

setup(
    name='Pyrebase',
    version='3.0.28',
    url='https://github.com/thisbejim/Pyrebase',
    description='A simple python wrapper for the Firebase API',
    author='James Childs-Maidment',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='Firebase',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'requests',
        'gcloud',
        'oauth2client',
        'requests_toolbelt>=0.7',
        'python_jwt>=3.2',
        'pycryptodome>=3.4'
    ]
)
