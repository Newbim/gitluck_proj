# CampusContests Web


CampusContests Web 프로젝트는, 
한양대학교 학생을 대상으로 맞춤형 공모전 정보를 제공하기 위한 웹사이트 개발 프로젝트이다. 

## 1. 코드 
해당 github에 올라온 파일은 기능에 따라 4개로 분류된다.

  - **`main.py`** | 웹 서버
  
    웹 전체 동작 제어하는 코드이다. 
    flask를 이용하여 웹 서버를 생성하고 웹 크롤링 결과를 html 에 넘겨주는 역할을 한다.        
  <br>
  
  - **`cc_scrapper.py` `exporter.py`** | 웹 스크래핑 및 정보 저장
  
    cc_scrapper.py와 exporter.py는 웹 스크래핑과 관련이 있다.
    |코드|내용|
    |------|------|
    |cc_scrapper.py|한양대학교 전체 공지에 올라온 공모전정보를 스크래핑하는 코드|
    |exporter.py|스크래핑 한 정보를 csv파일로 저장하기 위한 코드|
  <br>

  - **`static` 디렉토리 - CSS, JAVASCRIPT** | 웹 스타일 지정 및 변환
     
    웹 페이지 스타일과 웹 페이지 event 동작을 표현하는 코드가 들어있는 디렉토리이다. 
    static 디렉토리에서, **css와 js디렉토리**로 나뉜다. **css 디렉토리**에는 `classStyle.css`, `homeStyle.css`가 존재하며, **js 디렉토리**에는 `classScript.js`가 존재한다.
    |코드|내용|
    |------|------|
    |classStyle.css|게시자 기준 전체, 서울, 에리카로 분류한 웹페이지에 대하여 스타일을 적용하는 코드|
    |homeStyle.css|홈페이지 스타일을 정의한 코드|
    |classScript.js|스타일을 변환하는 코드. 다크모드를 적용할 때의 스타일과 스크롤 시 나타나는 스타일을 정의한 코드이다. |
  <br>    
  
  - **`templates` 디렉토리 - HTML** | 웹 페이지 
  

    html 코드가 들어있는 디렉토리이다.
    templates디렉토리에는, **classAll.html, classErica.html, classSeoul.html, home.html, search.html** 이 존재한다. 

    |코드|내용|
    |------|------|
    |classAll.html, classErica.html, classSeoul.html|게시자 기준 전체, 서울, 에리카로 분류한 정보를 나타내는 웹 페이지 코드|
    |home.html|홈페이지 코드|
    |search.html|검색할 시 나타나는 웹 페이지 코드|
  <br>



## 2. 설치 및 사용
   - **Visual Studio Code 에서 실행**
     1) 설치
     
        1. 터미널 | `pip install flask` 입력
        
        2. 터미널 | `pip install flask_paginate` 입력
        
        3. 터미널 | `pip install requests` 입력
        
        4. 터미널 | `pip install bs4` 입력
        
        5. 터미널 | `pip install waitress` 입력
     2) 실행
     
        1. 터미널 | `python main.py` 입력
        
        2. 웹브라우저 | `localhost:8080` 입력 
     3) 실행 시 공모전 내용이 안뜨는 오류가 발생할 경우
     
        
        1. 파일삭제 | `ccdata.csv` 가 생성되어 있는 경우 삭제
        
        2. vscode 설정 | 
        
           (1) `설정(Ctrl + , or 톱니바퀴)` 
           
           (2) `encoding 검색` 
           
           (3) `default` : UTF-8
           
           (4) `Auto Guess Encoding` : 빈 체크박스 클릭 
        
       
  <br>
        
   - **Replit에서 실행**
      ```
      Replit에서 실행할 경우, 설치사항이 없습니다. 
      실행시, Run 버튼을 클릭하면 됩니다.
      ```
  <br>

## 3. 라이선스

- 프론트엔드 오픈소스 툴킷 **`Bootstrap`** 사용

- 프론트엔드 오픈소스 커뮤니티 **`Codepen`** 에서, Job Search Platform UI 사용
  ```
  Copyright (c) 2022 Aysenur Turk (https://codepen.io/TurkAysenur/pen/jOqdNbm)
  ```
- ContestCampus 라이선스
  ```
  Copyright (c) 2022 Gitluck Team
  ```
