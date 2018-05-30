from setuptools import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    requirements = f.read()

setup(
    name='adabot',
    version='1.1.1',
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
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: Portuguese',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Multimedia :: Sound/Audio :: Capture/Recording',
        'Topic :: Multimedia :: Sound/Audio :: Speech',
        'Topic :: Communications :: Chat',
        'Topic :: Home Automation',
    ],
)