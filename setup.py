"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""
import setuptools

APP = ['get_Arrivalinfo_URAGA-military.py']
DATA_FILES = []
OPTIONS = {}

setuptools.setup(
    name="Arrival Information of Large Military Vessels",
    version="0.1.0",
    author="D. Nishiyama.",
    author_email="nishiyama.daiki.tu@alumni.tsukuba.ac.jp",
    description="You can receive a notification when it was discovered that a large government ship was scheduled to pass through the Uraga Channel.",
    url="https://github.com/ProfFunami/Arrival_information_of_large_military_vessels",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    entry_points={
        'console_scripts': ['uraga_info=uraga_src.get_Arrivalinfo:main']
    },
)
