from setuptools import setup, find_packages


# Read the README.md file for the long_description
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


# Note: If your package has many dependencies, you can include these in a requirements.txt file
# Read the content of requirements.txt
with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()
# Then use install_requires = requirements in the setup()

# You can auto-generate requirements.txt using the following in your terminal:
# pip install pipreqs
# pipreqs /path/to/project

setup(
    name = 'mypackage',                                 # Replace with your package name
    version='0.0.1',                                    # Set the package version
    description = 'A sample Python package',            # Describe your package
    author = 'Jake Rhodes',                             # Your name or the package author
    author_email = 'rhodes@stat.byu.edu',               # Your email address
    url = 'github.com/rhodes-stat386-fall2023/package-example',  # URL of your project repository
    packages = find_packages(),                         # Automatically find all packages
    install_requires = requirements,                    # Package dependences
    classifiers = [                                     # Add package classifiers (OPTIONAL)
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    long_description = long_description,                # Use README content as long_description
    long_description_content_type = 'text/markdown',    # Specify the content type
    package_data = {'temples_raw': 'data/temples_raw.csv'}
)



