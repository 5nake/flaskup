from setuptools import setup

setup(
    name='flaskup',
    version='0.1',
    long_description=__doc__,
    packages=['flaskup'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask>=0.8', 'simplejson', 'Flask-Babel>=0.8',
                      'Flask-Mail>=0.6.1'],
    entry_points={
        'console_scripts': [
            'flaskup = flaskup.console:main',
        ],
    },
)

