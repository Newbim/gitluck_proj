"""
These are the URLs that will give you remote jobs for the word 'python'

https://kr.indeed.com/jobs?q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

from flask import Flask, render_template, request, redirect, send_file
import math
from flask_paginate import Pagination, get_page_args
from cc_scrapper import cc_get_contests_keyword
from cc_scrapper import cc_get_contests
from exporter import save_to_file
from exporter import load_file
from exporter import check_file

from cc_scrapper import cc_get_contests_class_erica
from cc_scrapper import cc_get_contests_class_seoul
from cc_scrapper import cc_get_contests_keyword


app = Flask(__name__)

db = load_file()
if (check_file()):
  db = db
else:
  db = cc_get_contests()
  save_to_file(db)

dbSearch = {}

app.template_foder = "templates"
users = list(range(len(db)))


def get_users(offset=0, per_page=9):
  print(users[offset:offset + per_page])
  return users[offset:offset + per_page]


@app.route("/")
def home():
  return render_template("home.html")


@app.route("/search", methods=['GET'])
def search():
  word = request.args.get("q")
  if (word):
    existing_contests = dbSearch.get(word)
    if existing_contests:
      contests = existing_contests
    else:
      contests = cc_get_contests_keyword(word, db)
      dbSearch[word] = contests
    users = list(range(len(contests)))  
    per_page = 9
    page, per_page, offset = get_page_args(page_parameter="page",
                                       per_page = per_page,
                                       per_page_parameter="per_page")
    total = len(users)
    pagination_users = get_users(offset=offset, per_page=per_page)
    pagination = Pagination(page=page,
                            per_page=per_page,
                            total=total,
                            css_framework='bootstrap4')
  else:
    return redirect("/")
  return render_template("search.html",
                         page_num = len(contests),
                         users=pagination_users,
                         page=page,
                         per_page=per_page,
                         searchingBy=word,
                         pagination=pagination,
                         contests=contests)


@app.route("/classAll", methods=['GET'])
def classAll():
  # # pagenum = request.GET.get("page")
  # return render_template("classAll.html",
  #                        resultsNumber=len(db),
  #                        searchingBy="ALL",
  #                        contests=db,
  #                       )
  per_page = 9
  page, per_page, offset = get_page_args(page_parameter="page",
                                         per_page = per_page,
                                         per_page_parameter="per_page")
  total = len(users)
  pagination_users = get_users(offset=offset, per_page=9)
  pagination = Pagination(page=page,
                          per_page=per_page,
                          total=total,
                          css_framework='bootstrap4')

  return render_template("classAll.html",
                         page_num = len(db),
                         users=pagination_users,
                         page=page,
                         per_page=per_page,
                         pagination=pagination,
                         contests=db)


@app.route("/classErica", methods=['GET'])
def classErica():
  lst = cc_get_contests_class_erica(db)
  users = list(range(len(lst)))
  per_page = 9
  page, per_page, offset = get_page_args(page_parameter="page",
                                         per_page = per_page,
                                         per_page_parameter="per_page")
  total = len(users)
  pagination_users = get_users(offset=offset, per_page=per_page)
  pagination = Pagination(page=page,
                          per_page=per_page,
                          total=total,
                          css_framework='bootstrap4')

  return render_template("classErica.html",
                         page_num = len(lst),
                         users=pagination_users,
                         page=page,
                         per_page=per_page,
                         pagination=pagination,
                         contests=lst)


@app.route("/classSeoul", methods=['GET'])
def classSeoul():
  lst = cc_get_contests_class_seoul(db)
  users = list(range(len(lst)))
  per_page = 9
  page, per_page, offset = get_page_args(page_parameter="page",
                                         per_page = per_page,
                                         per_page_parameter="per_page")
  total = len(users)
  pagination_users = get_users(offset=offset, per_page=9)
  pagination = Pagination(page=page,
                          per_page=per_page,
                          total=total,
                          css_framework='bootstrap4')

  return render_template("classSeoul.html",
                         page_num = len(lst),
                         users=pagination_users,
                         page=page,
                         per_page=per_page,
                         pagination=pagination,
                         contests=lst)


if __name__ == "__main__":
  # app.run(debug=True)
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
