from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pyodesolve',
    version='0.1.0',
    author='Your Name',  # CHANGE THIS
    author_email='your.email@example.com',  # CHANGE THIS
    description='Advanced ODE/DAE solver suite in pure Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/yourusername/pyodesolve',  # CHANGE THIS
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.7',
    keywords='ode solver numerical integration stiff bdf runge-kutta',
)
