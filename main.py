import unicodedata
from flask import Flask, render_template, session, redirect, request
import os
import json
import platform


def getdir():
    current_os = platform.uname()
    print(current_os.system)
    if current_os.node == "taumah-HP-Pavilion-Notebook-15-bc5xxx":
        return "/home/taumah/Bureau/killian-besancon"
    if current_os.node == "Windows":
        return "C:/Users/thoma/Desktop/killian-besancon"
    if current_os.system != "Windows":
        return "/var/www/killian-besancon"
    else:
        return "./"


app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = "vnkdj@nfjknfl1232#"


# with open(getdir()+'/config.json', 'r', encoding="utf-8") as outfile:
#     data = json.load(outfile)
# optns = data


@app.route("/")
def index():
    projets = {}
    catlist = os.listdir(getdir() + "/static/projets")
    # remove all files
    catlist = [
        cat
        for cat in catlist
        if not os.path.isfile(getdir() + "/static/projets/" + cat)
    ]
    # trier les catégories par ordre alphabétique
    catlist = sorted(catlist)
    catnamefiles = []
    listname = []
    for cat in catlist:
        plist = os.listdir(getdir() + "/static/projets/" + cat)
        for p in plist:
            if os.path.isfile(getdir() + "/static/projets/" + cat + "/" + p):
                # read file p
                with open(
                    getdir() + "/static/projets/" + cat + "/" + p, "r", encoding="utf-8"
                ) as outfile:
                    # readline
                    line = outfile.readline()
                    # add to listname
                listname.append(line)

        # remove all files
        plist = [
            p
            for p in plist
            if not os.path.isfile(getdir() + "/static/projets/" + cat + "/" + p)
        ]
        for pfile in plist:
            with open(
                getdir() + "/static/projets/" + cat + "/" + pfile + "/projet.json",
                "r",
                encoding="utf-8",
            ) as outfile:
                data = json.load(outfile)
            if cat not in projets.keys():
                projets[cat] = []
            projets[cat].append(
                {"img": data["img"], "titre": data["titre"], "id": pfile}
            )

    # trier les projets par id dans chaque catégorie
    for cat, plist in projets.items():
        projets[cat] = sorted(plist, key=lambda k: k["id"])

    print(len(projets.items()))
    print(len(listname))
    counter = 0
    html_projets = ""
    for cat, plist in projets.items():
        html_projets += (
            '<div class="portfolio-group" catname="' + listname[counter] + '">'
        )
        counter += 1
        for projet in plist:
            html_projets += '<div class="portfolio-item">'
            html_projets += (
                '<img src="../static/projets/'
                + cat
                + "/"
                + projet["id"]
                + "/"
                + projet["img"]
                + '" alt="'
                + projet["titre"]
                + '">'
            )
            html_projets += "<h3>" + projet["titre"] + "</h3>"
            html_projets += (
                '<a class="btn-voir-plus" href="/projet/'
                + cat
                + "/"
                + projet["id"]
                + '">Voir le projet</a>'
            )
            html_projets += "</div>"
        html_projets += "</div>"




    html_plastiques = ""
    pplastiques = os.listdir(getdir() + "/static/plastiques")
    dataplastiques = []
    for projet_p in pplastiques:
        # find the json file
        for file in os.listdir(getdir() + "/static/plastiques/" + projet_p):
            if file.endswith(".json"):
                with open(
                    getdir() + "/static/plastiques/" + projet_p + "/" + file,
                    "r",
                    encoding="utf-8",
                ) as outfile:
                    data = json.load(outfile)
                    dataplastiques.append({"img": data["img"], "titre": data["titre"], "id": projet_p})
                break

    for projet in dataplastiques:
        html_plastiques += '<div class="portfolio-item">'
        html_plastiques += (
            '<img src="../static/plastiques/'
            + projet["id"]
            + "/"
            + projet["img"]
            + '" alt="'
            + projet["titre"]
            + '">'
        )
        html_plastiques += "<h3>" + projet["titre"] + "</h3>"
        html_plastiques += (
            '<a class="btn-voir-plus" href="/plastiques/'
            + projet["id"]
            + '">Voir le projet</a>'
        )
        html_plastiques += "</div>"

    return render_template("index.html", projets=html_projets, plastiques=html_plastiques)
                    


@app.route("/draws/<cat>")
def draw(cat):
    # lister les fichiers dans le dossier cat
    plist = os.listdir(getdir() + "/static/Dessins/" + cat)
    # remove all files with no .pnj or .jpg
    plist = [p for p in plist if p.endswith(".png") or p.endswith(".jpg")]
    # trier les fichiers par ordre alphabétique
    plist = sorted(plist)
    html_content = ""



    for p in plist:
        html_content += "<div class='draw'>"
        # si il y a une lettre avec accent dans p
        html_content += (
            '<img src="../static/Dessins/' + cat + "/" + p + '" alt="' + p + '">'
        )
        imgname = p.split(".")
        # remove the last element of the list
        imgname.pop()
        # join the list with a dot
        imgname = ".".join(imgname)

        imgname = imgname.split(";;;")
        # delete the first element of the list
        imgname.pop(0)
        
        print(imgname)
        html_content += "<p>"
        for tmp in imgname:
            html_content += tmp + "<br>"
        html_content += "</p>"
        html_content += "</div>"
    return render_template("draw.html", content=html_content, cat=cat)


@app.route("/plastiques/<id>")
def plastiques(id):
    with open(
        getdir() + "/static/plastiques/" + id + "/projet.json",
        "r",
        encoding="utf-8",
    ) as outfile:
        data = json.load(outfile)

    html_content = ""

    html_content += (
        '<img src="../../static/plastiques/'
        + id
        + "/"
        + data["img"]
        + '" alt="'
        + data["titre"]
        + '">'
    )

    for line in data["desc"]:
        if line.startswith("%") and line.endswith("%"):
            # si la ligne contient 4 %
            if line.count("%") == 3:
                html_content += '<div class="doubleimage">'
                html_content += (
                    '<img src="../../static/plastiques/'
                    + id
                    + "/"
                    + line[1 : line.find("%", 1)]
                    + '" alt="'
                    + line[1 : line.find("%", 1)]
                    + '">'
                )
                html_content += (
                    '<img src="../../static/plastiques/'
                    + id
                    + "/"
                    + line[line.find("%", 1) + 1 : -1]
                    + '" alt="'
                    + line[line.find("%", 1) + 1 : -1]
                    + '">'
                )
                html_content += "</div>"
            else:
                html_content += (
                    '<img src="../../static/plastiques/'
                    + id
                    + "/"
                    + line[1:-1]
                    + '" alt="'
                    + line[1:-1]
                    + '">'
                )
        else:
            html_content += "<p>" + line + "</p>"

    return render_template("projet.html", data=data, content=html_content)



@app.route("/download")
def download():
    return render_template("download.html")


@app.route("/projet/<cat>/<id>")
def projet(cat, id):
    with open(
        getdir() + "/static/projets/" + cat + "/" + id + "/projet.json",
        "r",
        encoding="utf-8",
    ) as outfile:
        data = json.load(outfile)

    html_content = ""

    html_content += (
        '<img src="../../static/projets/'
        + cat
        + "/"
        + id
        + "/"
        + data["img"]
        + '" alt="'
        + data["titre"]
        + '">'
    )

    for line in data["desc"]:
        if line.startswith("%") and line.endswith("%"):
            # si la ligne contient 4 %
            if line.count("%") == 3:
                html_content += '<div class="doubleimage">'
                html_content += (
                    '<img src="../../static/projets/'
                    + cat
                    + "/"
                    + id
                    + "/"
                    + line[1 : line.find("%", 1)]
                    + '" alt="'
                    + line[1 : line.find("%", 1)]
                    + '">'
                )
                html_content += (
                    '<img src="../../static/projets/'
                    + cat
                    + "/"
                    + id
                    + "/"
                    + line[line.find("%", 1) + 1 : -1]
                    + '" alt="'
                    + line[line.find("%", 1) + 1 : -1]
                    + '">'
                )
                html_content += "</div>"
            else:
                html_content += (
                    '<img src="../../static/projets/'
                    + cat
                    + "/"
                    + id
                    + "/"
                    + line[1:-1]
                    + '" alt="'
                    + line[1:-1]
                    + '">'
                )
        else:
            html_content += "<p>" + line + "</p>"

    return render_template("projet.html", data=data, content=html_content)


if __name__ == "__main__":
    # zip static
    # os.system("zip -r static.zip static; mv static.zip static")


    app.run()
