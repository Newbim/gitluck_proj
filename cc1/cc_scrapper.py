# 전체코드
import requests
from bs4 import BeautifulSoup
import re, math
from datetime import datetime
import time

# 마지막 페이지 반환

def get_last_pages(url):
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("div", {"class": "board-count float-left"})
  total = re.sub(r'[^0-9]', '', str(results).split("<span>")[1].split("건")[0])
  max_page = math.ceil(int(total) / 10)
  print(max_page)
  return max_page

# dDay 계산을 위한 함수들

def is_leap_year(year):  # 윤년
  return ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)


def days_in_month(month, year):
  days = {
    "1": 31,
    "2": 29 if is_leap_year(year) else 28,
    "3": 31,
    "4": 30,
    "5": 31,
    "6": 30,
    "7": 31,
    "8": 31,
    "9": 30,
    "10": 31,
    "11": 30,
    "12": 31
  }
  return days[str(month)]


def days_in_year(year):
  return 366 if is_leap_year(year) else 365


def parse_day(year, month, days):
  month = month - 1
  while (month):
    days += days_in_month(month, year)
    month = month - 1

  year = year - 1
  while (1970 < year):
    days += days_in_year(year)
    year = year - 1
  return days


def calculate_ymd(period):
  # 2022.11.18~2022.11.24
  if "~" in period:
    dDay = period.split("~")[1]
    year, month, day = list(map(int, dDay.split(".")))
    today = datetime.today()
    today_year, today_month, today_day = today.year, today.month, today.day
    # print(year, month, day)
    # print("===========================")
    # print(today_year, today_month, today_day)
    return parse_day(year, month, day) - parse_day(today_year, today_month,
                                                   today_day)
  else:
    return None


# 공모전 정보 반환

def extract_contest(html, url):
  href = html.find('a')["href"]
  href_int = re.sub("[^0-9]", "", href)
  url = '&'.join(url.split("&")[:-1])
  element_link = f"{url}&_viewNotice_WAR_noticeportlet_action=view_message&_viewNotice_WAR_noticeportlet_messageId={href_int}"

  result = requests.get(element_link)
  soup = BeautifulSoup(result.text, "html.parser")
  datas = soup.find("td", {"class": "view-title"})
  data_list = datas.get_text().replace(" ", "").split()
  title = data_list[0]
  # campus = ""

  for idx in range(len(data_list)):
    if "공지기간" in data_list[idx]:
      notice_period = data_list[idx][5:]
    elif "행사기간" in data_list[idx]:
      event_period = data_list[idx + 1]
    elif "게시" in data_list[idx]:
      campus = data_list[idx + 1]

  dDay = calculate_ymd(event_period)
  # print(f"========dDay는 {dDay}")
  str_dDay = ""
  if dDay is None:
    str_dDay = f"D-?"
  elif dDay < 0:
    if dDay < -365:
      return None
    str_dDay = "마감"
  elif dDay == 0:
    str_dDay = "D-Day"
  else:
    str_dDay = f"D-{dDay}"
  # datas_link_html = soup.find("td", {"class":"view-script"})
  # data_list = datas.get_text().replace(" ", "").split()
  # imagelink = f"https://www.hanyang.ac.kr"

  try:
    image_link_element = soup.find("img", {"alt": ""})["src"]
    if "hanyang.ac.kr" in image_link_element:
      image_link = image_link_element
    else:
      image_link = f"https://www.hanyang.ac.kr{image_link_element}"
  except:
    image_link = ""

  return {
    "title": title,
    "dDay": str_dDay,
    # "notice_period": notice_period,
    # "event_period": event_period,
    "campus_class": campus,
    "homepagelink": element_link,
    "imagelink": image_link
  }


# title 분류검색기능

def isContest(html):
  title = html.find("a").get_text()
  if ("공모전" in title) or ("대회" in title) or ("대전" in title):
    return True
  return False


# 페이지 번호 바꾸기

def change_url_page(url, page):
  url_list = url.split("&")
  lst = []
  for element in url_list:
    if "sCurPage" in element:
      element = element[:-1] + page
    lst.append(element)
  change_url = '&'.join(lst)
  return change_url




def extract_contests(last_page, url):
  contests = []
  for page in range(1, int(last_page)):
    print(f"Scrapping page {page}")
    url_ = change_url_page(url, str(page))
    try:
      result = requests.get(url_)
    except:
      time.sleep(2)
      result = requests.get(url_)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "title-wrap"})
    for result in results:
      if (isContest(result)):
        contest = extract_contest(result, url_)
        if contest is None:
          return contests
        contests.append(contest)
        # print(contest)
  return contests


def cc_get_contests():
  url = "https://www.hanyang.ac.kr/web/www/notice_all?p_p_id=viewNotice_WAR_noticeportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_viewNotice_WAR_ntoticeportle_sKeyType=title&_viewNotice_WAR_noticeportlet_sCategoryId=7&_viewNotice_WAR_noticeportlet_sCurPage=1&_viewNotice_WAR_noticeportlet_sUserId=0&_viewNotice_WAR_noticeportlet_action=view"
  last_page = get_last_pages(url)
  contests = extract_contests(last_page, url)
  return contests


def cc_get_contests_keyword(word, db):
  lst = []
  for contest in db:
    if word in contest['title']:
      lst.append(contest)
    print(contest)
  return lst


def cc_get_contests_class_erica(db):
  lst = []
  for contest in db:
    if "ERICA" in contest['campus']:
      lst.append(contest)
    print(contest)
  return lst


def cc_get_contests_class_seoul(db):
  lst = []
  for contest in db:
    if "서울" in contest['campus']:
      lst.append(contest)
    print(contest)
  return lst

