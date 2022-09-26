from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name='NlpToolkit-NamedEntityRecognition',
    version='1.0.11',
    packages=['NamedEntityRecognition', 'NamedEntityRecognition.data'],
    package_data={'NamedEntityRecognition.data': ['*.txt']},
    url='https://github.com/StarlangSoftware/TurkishNamedEntityRecognition-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='NER Corpus Processing Library',
    install_requires=['NlpToolkit-Corpus'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
