# setup.py
from setuptools import setup, find_packages

setup(
    name='jieba_zh_TW',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'jieba_zh_TW': ['dict.txt.big'],
    },
    description='Jieba with Traditional Chinese dictionary',
    author='Your Name',
    license='MIT',
)
