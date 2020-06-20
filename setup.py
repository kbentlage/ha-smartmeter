from setuptools import setup

setup(
    name='smartmeter',
    version='1.0.0',
    packages=['smartmeter'],
    entry_points={
        'console_scripts': [
            'smartmeter = smartmeter.__main__:main'
        ]
    },
)