from setuptools import setup,find_packages

setup(
    name='sales_metrics',
    author='latoya',
    author_email='latoya@email.com',
    version='0.1.0',
    install_requires=['pandas'],
    packages=find_packages(include=['sales_metrics','sales_metrics.*'])
)
