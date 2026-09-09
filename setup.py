import setuptools
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

version_file = os.path.realpath(os.path.join(os.path.dirname(__file__), "underautomation", "abb", "lib", "version.txt"))

with open(version_file, "r", encoding="utf-8") as fh:
    version = fh.read().strip()

setuptools.setup(
    name="UnderAutomation.ABB",
    version=version,
    author="UnderAutomation",
    author_email="support@underautomation.com",
    description="Quickly create applications that communicate with your ABB robots over Robot Web Services (RWS)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://underautomation.com/abb",
    project_urls={
        "Documentation": "https://underautomation.com/abb/documentation/get-started-python",
        "Source": "https://github.com/underautomation/ABB.py",
    },
    license="Commercial",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Intended Audience :: Developers",
        "Intended Audience :: Manufacturing",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries",
    ],
    packages=setuptools.find_packages(include=["underautomation", "underautomation.*"]),
    python_requires="<3.14,>=3.7",
    install_requires=[
        "pythonnet==3.0.5",
    ],
    include_package_data=True,
    package_data={
        "underautomation": [
            "abb/lib/*.dll",
            "abb/lib/*.txt",
        ],
    },
)
