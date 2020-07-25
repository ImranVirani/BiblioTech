function displayEntry() {
    var authorFirstName = document.getElementById("authorFirstName").value;
    var authorLastName = document.getElementById("authorLastName").value;
    var articleTitle = document.getElementById("articleTitle").value;
    var publisherName = document.getElementById("publisherName").value;
    var dayPublished = document.getElementById("dayPublished").value;
    var monthPublished = document.getElementById("monthPublished").value;
    var yearPublished = document.getElementById("yearPublished").value;
    var urlOfSource = document.getElementById("urlOfSource").value;
    var dateOfAccess = document.getElementById("dateOfAccess").value;

    if (formatType = "mla") {
        document.getElementById("result-entry").innerHTML = authorLastName + ", " + authorFirstName + '. "' + articleTitle + '." ' + "<em>" + publisherName + "</em>" + " " + dayPublished + " " + monthPublished + " " + yearPublished + " " + urlOfSource + " " + "Accessed " + dateOfAccess;

    }
    // Checks to see which type of citations is being done
    if (formatType = "apa") {
        document.getElementById("result-entry").innerHTML = authorLastName + ", " + authorFirstName[0] + " (" + yearPublished + "," + " " + monthPublished + " " + dayPublished + "). " + "<em>" + articleTitle + "</em>." + " " + publisherName + ". " + urlOfSource

    }
    // Chicago has to be done
    if (formatType = "chicago") {
        document.getElementById("result-entry").innerHTML = authorLastName + ", " + authorFirstName + '. "' + articleTitle + '." ' + "<em>" + publisherName + "</em>" + " " + dayPublished + " " + monthPublished + " " + yearPublished + " " + urlOfSource + " " + "Accessed " + dateOfAccess;

    }
}
document.getElementById("submit-button").addEventListener("click", displayEntry);