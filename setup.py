from setuptools import setup


setup(
    name="noeval",
    description="Warn if `eval()` is committed to a repository",
    url="https://github.com/brianjbuck/noeval",
    version="1.0.0",
    author="Brian Buck",
    author_email="brian@thebuckpasser.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    install_requires=[],
    py_modules=["noeval"],
    entry_points={"console_scripts": ["noeval = noeval:main"]},
)
