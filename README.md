[![My YouTube Video](https://img.youtube.com/vi/gM_yjxFoF6I/0.jpg)](https://www.youtube.com/watch?v=gM_yjxFoF6I)


---
## :rocket: Dev Guide

1. [Introduction](#introduction)
2. [Team members](#team)
3. [Features](#기능-소개)
4. [Process Flow](#process-flow)
5. [ERD](#erd)
6. [Tech stacks](#tech-stacks)
7. [Project Directory Structure](#project-directory-structure)
---
## Introduction
#### Bookgroo는 키워드 기반 책을 추천해주는 챗봇 구현 project입니다
---
## Team

|Role        |Name      |GitHub        |Responsibilities |
|------------|----------|--------------|-----------------|
|team leader👑|**이고운**| [@dlrhdns75177](https://github.com/dlrhdns75177)|backend (drf, langchain)        |
|team member |**맹주형**| [@jhmang1128](https://github.com/jhmang1128)     |backend (langchain,drf)        |
|team member |**정지웅**| [@JaceJung-dev](https://github.com/JaceJung-dev) |backend (drf, langchain)        |
|team member |**최보근**| [@invisible-bo](https://github.com/invisible-bo) |frontend (html, css, js)        |
---
## 기능 소개
1. 회원가입, 로그인, 로그아웃 기능 제공
2. 키워드를 포함한 책 질문 입력 시 적절한 책을 추천해주는 챗봇 구현

---
## Process Flow
![process flow](/static/process_flow.png)
---
## ERD
![ERD](/static/ERD.png)
---
## Tech stacks
**Backend**
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)&nbsp;![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)&nbsp;![DRF](https://img.shields.io/badge/DRF-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)&nbsp;![DRFJWT](https://img.shields.io/badge/DRFJWT-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

**Frontend**
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)&nbsp;![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)&nbsp;![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

**AI**
![OPENAI](https://img.shields.io/badge/OPENAI-%23412991.svg?style=for-the-badge&logo=OPENAI&logoColor=white)&nbsp;![langchain](https://img.shields.io/badge/langchain-%231C3C3C.svg?style=for-the-badge&logo=langchain&logoColor=white)&nbsp;![imagen3](https://img.shields.io/badge/imagen3-%231C3C3C.svg?style=for-the-badge&logo=imagen3&logoColor=white)

**Web Crawling**
![Beautifulsoup](https://img.shields.io/badge/beautifulsoup-%23412991.svg?style=for-the-badge&logo=beautifulsoup&logoColor=white)

**Version Control Systems**
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)&nbsp;

**Collaboration Tools**
![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=Notion&logoColor=white)&nbsp;![Slack](https://img.shields.io/badge/Slack-%234A154B.svg?style=for-the-badge&logo=Slack&logoColor=white)

---
## Project Directory Structure
```bash
| | | |____BOOKGROO
| | | | |____.env
| | | | |____.git
| | | | | |____COMMIT_EDITMSG
| | | | | |____config
| | | | | |____description
| | | | | |____HEAD
| | | | | |____hooks
| | | | | |____index
| | | | | |____info
| | | | | |____logs
| | | | | |____objects
| | | | | |____packed-refs
| | | | | |____refs
| | | | |____.gitignore
| | | | |____accounts
| | | | | |____admin.py
| | | | | |____apps.py
| | | | | |____migrations
| | | | | |____models.py
| | | | | |____serializers.py
| | | | | |____tests.py
| | | | | |____urls.py
| | | | | |____utils.py
| | | | | |____views.py
| | | | | |______init__.py
| | | | | |______pycache__
| | | | |____bookgroo
| | | | | |____asgi.py
| | | | | |____settings.py
| | | | | |____urls.py
| | | | | |____wsgi.py
| | | | | |______init__.py
| | | | | |______pycache__
| | | | |____chatrooms
| | | | | |____admin.py
| | | | | |____apps.py
| | | | | |____migrations
| | | | | |____models.py
| | | | | |____serializers.py
| | | | | |____urls.py
| | | | | |____views.py
| | | | | |______init__.py
| | | | | |______pycache__
| | | | |____db.sqlite3
| | | | |____frontend
| | | | | |____assets
| | | | | |____components
| | | | | |____pages
| | | | | |____scripts
| | | | | |____styles
| | | | |____LangChain
| | | | | |____chatbot.py
| | | | | |____main_chatbot.py
| | | | | |____store_DB.py
| | | | | |____test_chatbot.py
| | | | | |____test_graph.ipynb
| | | | | |____test_graph.ipynb
| | | | | |______init__.py
| | | | | |______pycache__
| | | | |____manage.py
| | | | |____README.md
| | | | |____requirements.txt
| | | | |____static
| | | | | |____Bookgroo.jpg
| | | | | |____ERD.png
| | | | | |____process_flow.png
```