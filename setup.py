from setuptools import setup, find_packages

setup(
    name="deep-rl-simulation",
    version="0.1.0",
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    author="Yann LeCun",
    description="High-fidelity simulation environment for training complex reinforcement learning agents.",
    url="https://github.com/YannLeCun25/deep-rl-simulation",
)
