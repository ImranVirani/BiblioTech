from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mla')
def mla():
    return render_template('MLA.html')

@app.route('/mla', methods=['GET', 'POST'])
def mla_post():
    if (request.form['urlOfSource'] == "") or (request.form['articleTitle'] == ""):
        return render_template('error.html')
    citationType = "mla"
    authorFirstName = request.form['authorFirstName'] + "."
    authorLastName = request.form['authorLastName'] + ","
    articleTitle = request.form['articleTitle']
    publisherName = request.form['publisherName'] + ","
    dayPublished = request.form['dayPublished']
    monthPublished = request.form['monthPublished']
    yearPublished = request.form['yearPublished'] + ","
    urlOfSource = request.form['urlOfSource'] + "."
    dateOfAccess = request.form['dateOfAccess'] + "."
    return render_template('result.html', authorFirstName = authorFirstName, authorLastName = authorLastName, articleTitle = articleTitle, publisherName=publisherName, dayPublished=dayPublished, monthPublished=monthPublished, yearPublished=yearPublished, urlOfSource=urlOfSource, dateOfAccess=dateOfAccess, citationType=citationType)
@app.route('/apa')
def apa():
    return render_template('apa.html')

@app.route('/apa', methods=['GET', 'POST'])
def apa_post():
    if (request.form['urlOfSource'] == "") or (request.form['articleTitle'] == ""):
        return render_template('error.html')
    # IMPORTANT: FORMATTING HAS NOT BEEN DONE YET
    citationType= "apa"
    authorFirstName = request.form['authorFirstName']
    authorFirstName = authorFirstName[0] + "."
    authorLastName = request.form['authorLastName'] + ","
    articleTitle = request.form['articleTitle']
    publisherName = request.form['publisherName'] + ","
    dayPublished = request.form['dayPublished']
    monthPublished = request.form['monthPublished']
    yearPublished = request.form['yearPublished']
    urlOfSource = request.form['urlOfSource']
    return render_template('result.html', authorFirstName = authorFirstName, authorLastName = authorLastName, articleTitle = articleTitle, publisherName=publisherName, dayPublished=dayPublished, monthPublished=monthPublished, yearPublished=yearPublished, urlOfSource=urlOfSource, citationType=citationType)

@app.route('/chicago')
def chicago():
    return render_template('chicago.html')

@app.route('/chicago', methods=['GET', 'POST'])
def chicago_post():
    if (request.form['urlOfSource'] == "") or (request.form['articleTitle'] == ""):
        return render_template('error.html')
    # IMPORTANT: FORMATTING HAS NOT BEEN DONE YET
    citationType= "chicago"
    authorFirstName = request.form['authorFirstName'] + "."
    authorLastName = request.form['authorLastName'] + ","
    articleTitle = request.form['articleTitle']
    publisherName = request.form['publisherName'] + ","
    dayPublished = request.form['dayPublished']
    monthPublished = request.form['monthPublished']
    yearPublished = request.form['yearPublished'] + ","
    urlOfSource = request.form['urlOfSource'] + "."
    dateOfAccess = request.form['dateOfAccess'] + "."
    return render_template('result.html', authorFirstName = authorFirstName, authorLastName = authorLastName, articleTitle = articleTitle, publisherName=publisherName, dayPublished=dayPublished, monthPublished=monthPublished, yearPublished=yearPublished, urlOfSource=urlOfSource, dateOfAccess=dateOfAccess, citationType=citationType)