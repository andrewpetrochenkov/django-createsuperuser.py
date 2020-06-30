import setuptools

setuptools.setup(
    name='django-createsuperuser',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
