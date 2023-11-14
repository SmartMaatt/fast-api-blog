<h1 align="center">FastAPI blog test</h1>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#license">License</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  <img src="https://img.shields.io/badge/Author-SmartMatt-blue" />
</p>

## Overview
This repository contains a sample project for a blog and user management system using the FastAPI framework. The project features user authentication with token-based authorization and utilizes an SQLite database for data persistence.

## Features

- **Blog Management:** Create and read blog posts.
- **Token-based Authentication:** Secure access control using JWT tokens.
- **SQLite Database:** Utilized for efficient storage and retrieval of blog posts.

## Installation

To set up the project environment, follow these instructions:
1. Clone the repository
```bash
git clone https://github.com/SmartMaatt/fast-api-blog.git
```

2. Navigate to the project directory.
   
3. Create python virtual environment.
   
4. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage
To run the FastAPI server, execute:
```bash
uvicorn main:app --reload
```
The API will be available at http://127.0.0.1:8000.

### Documentation
For more detailed API documentation, visit http://127.0.0.1:8000/docs after starting the server.


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
&copy; 2023 Mateusz Płonka (SmartMatt). All rights reserved.
<a href="https://smartmatt.pl/">
    <img src="https://smartmatt.pl/github/smartmatt-logo.png" title="SmartMatt Logo" align="right" width="60" />
</a>

<p align="left">
  <a href="https://smartmatt.pl/">Portfolio</a> •
  <a href="https://github.com/SmartMaatt">GitHub</a> •
  <a href="https://www.linkedin.com/in/mateusz-p%C5%82onka-328a48214/">LinkedIn</a> •
  <a href="https://www.youtube.com/user/SmartHDesigner">YouTube</a> •
  <a href="https://www.tiktok.com/@smartmaatt">TikTok</a>
</p>
