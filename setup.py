from setuptools import setup

readme = open('README.md').read()

setup(
    name='vlm_rprimo',
    packages=['vlm_rprimo'],
    version='1.0',
    description='Script para calcular el numero de primos hasta n integrando R con Python',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Víctor Luque Martín',
    license='MIT',
    include_package_data=True,
    classifiers=[],
    keywords=['primos', 'R', 'Python'],
    url="https://github.com/soytupadrrre/vlm_rprimo",
    download_url="https://github.com/soytupadrrre/vlm_rprimo/archive/1.0.tar.gz",
)