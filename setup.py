from setuptools import setup, find_packages

setup(
    name = 'mypackage',             # Replace with your package name
    version='0.1',                # Set the package version
    description='A sample Python package',  # Describe your package
    author='Your Name',           # Your name or the package author
    author_email='youremail@example.com',  # Your email address
    url='https://github.com/yourusername/mypackage',  # URL of your project repository
    packages=find_packages(),     # Automatically find all packages
    install_requires=[            # List project dependencies
        'numpy',
        'pandas',
    ],
    classifiers=[                 # Add package classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
