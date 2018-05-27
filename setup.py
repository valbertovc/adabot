from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    requirements = f.read()

setup(
    name='ada-bot',
    version='0.1.0',
    description='Ada is chatbot for home automation',
    keywords='ada chatbot bot home automation',
    long_description=readme,
    author='Valberto Carneiro',
    author_email='valbertovc@gmail.com',
    url='https://github.com/python-ada-bot',
    license=license,
    install_requires = requirements,
    packages=find_packages(exclude=('tests', 'docs')),
    classifiers=[
        'Development Status :: development',
        'License :: OSI Approved :: GNU/GPL',
        'Programming Language :: Python :: 3.6',
        'Topic :: Chatbot :: Linguistic',
      ],
)