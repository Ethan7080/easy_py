from setuptools import setup, find_packages

setup(
    name='easy_py',
    version='0.0.1',
    packages=find_packages(),
    description='Makes your python programming adventure way easier with shortened functions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ethan Wang',
    author_email='ethanwanglife@gmail.com',
    url='https://github.com/yourusername/your_package',
    license='MIT',
    install_requires=[
        
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)