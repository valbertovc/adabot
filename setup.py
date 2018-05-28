from setuptools import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    requirements = f.read()

EXCLUDE_FROM_PACKAGES = ['adabot.settings_dev']

setup(
    name='adabot',
    version='0.2.0',
    description='Ada is chatbot for home automation',
    keywords='ada chatbot bot home automation',
    long_description=readme,
    author='Valberto Carneiro',
    author_email='valbertovc@gmail.com',
    url='https://github.com/python-ada-bot',
    license=license,
    include_package_data=True,
    install_requires=requirements,
    packages=['adabot', 'tests', 'docs', 'adabot.data', 'adabot.audio'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'TOPIC :: Communications :: Chat',
        'TOPIC :: Home Automation',
    ],
)