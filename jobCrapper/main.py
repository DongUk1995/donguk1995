from flask import Flask, render_template, request, redirect, send_file
from extractors.indeed import extract_jobs_indeed
from extractors.we_work_remotely import extract_jobs_wwr
from file import save_to_file

app = Flask("JobScrapper")

db = {}

@app.route("/")
def index():
    return render_template("home.html")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        indeed = extract_jobs_indeed(keyword) #링크
        wwr = extract_jobs_wwr(keyword) #링크
        jobs = indeed + wwr
        db[keyword] = jobs #dictionary의 item에 접근 할 수 있는 방법
    return render_template("search.html", keyword=keyword, jobs=jobs)


@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}_job.csv", as_attachment=True)


app.run("0.0.0.0")
