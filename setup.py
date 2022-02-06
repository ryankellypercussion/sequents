from setuptools import setup

setup(
    name='template',
    version='0.0.1',
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={
        'interactive': ['ipykernel>=6.8.0', 'jupyter>=1.0.0', 'notebook>=6.4.8'],
        'nlp': ['matplotlib>=3.5.1', 'networkx>=2.6.3', 'nltk>=3.6.7', 'numpy>=1.22.2']
    }
)