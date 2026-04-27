# turbo-invention

[![CI](https://github.com/kolaschiii6/turbo-invention/actions/workflows/ci-docker.yml/badge.svg)](https://github.com/kolaschiii6/turbo-invention/actions/workflows/ci-docker.yml)

# Text Encryption CLI

## Description
A command-line application for encrypting and decrypting text using Caesar cipher and ROT13.

## Features
- Caesar encryption and decryption
- ROT13 encryption and decryption
- Command-line interface
- Automated tests with pytest
- Easily accessible

## Installation

```bash
git clone https://github.com/kolaschiii6/turbo-invention
cd turbo-invention
pip install -r requirements.txt
```
**OR**
Download a lightweight .exe distributive from [Releases](https://github.com/kolaschiii6/turbo-invention/releases)

To run the application using Docker, use the following commands:

```bash
# Build the image
docker build -t crypto-app .

# Run the container (using -it for interactive CLI)
docker run -it crypto-app
```

## Team
- zorianalesyk (cipher logic)
- deduganchik10 (tests)
- Nazar (CLI interface)
- kolaschiii6 (documentation, Docker, distributables)
