import csv

def save_to_file(contests):
  file = open("ccdata.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["title", "dDay", "campus_class", "homepagelink", "imagelink"])
  for contest in contests:
    writer.writerow(list(contest.values()))
  return 

def load_file():
  lst = []
  try:
    with open("ccdata.csv", newline='') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        lst.append(row)
      return lst
  except:
    return lst

def check_file():
  try:
    file = open("ccdata.csv", mode="r")
    return True
  except:
    return False