from setuptools import setup

setup(
    name='ballistics-calculator',
    version='0.1.0',
    packages=['ballistics_calculator'],
    url='https://github.com/TimurSungatullin/ballistics-calculator',
    license='MIT Licens',
    author='Timur Sungatullin',
    author_email='arkana1223@mail.ru',
    description='Эта библиотека содержит функции для расчета баллистики.',
    install_requires=[
        "numpy==1.24.3",
        "matplotlib==3.7.1",
    ],
)
