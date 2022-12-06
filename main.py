"""
These are the URLs that will give you remote jobs for the word 'python'

https://kr.indeed.com/jobs?q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

from flask import Flask, render_template, request, redirect, send_file
from cc_scrapper import cc_get_contests_keyword
from cc_scrapper import cc_get_contests
from exporter import save_to_file
from exporter import load_file
from exporter import check_file

from cc_scrapper import cc_get_contests_class_erica
from cc_scrapper import cc_get_contests_class_seoul



app = Flask("CC")

db = load_file()
if (check_file()):
  db = db
else:
  db = cc_get_contests()
  save_to_file(db)

dbSearch = {}


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
  else:
    return redirect("/")
  return render_template("search.html",
                         resultsNumber=len(contests),
                         searchingBy=word,
                         contests=contests)


@app.route("/classAll", methods=['GET'])
def classAll():
  # pagenum = request.GET.get("page")
  return render_template("classAll.html",
                         resultsNumber=len(db),
                         searchingBy="ALL",
                         contests=db,
                        )


@app.route("/classErica", methods=['GET'])
def classErica():
  lst = cc_get_contests_class_erica(db)
  return render_template("classErica.html",
                         resultsNumber=len(lst),
                         searchingBy="ERICA",
                         contests=lst)


@app.route("/classSeoul", methods=['GET'])
def classSeoul():
  lst = cc_get_contests_class_seoul(db)
  return render_template("classSeoul.html",
                         resultsNumber=len(lst),
                         searchingBy="SEOUL",
                         contests=lst)


app.run(host="0.0.0.0")

