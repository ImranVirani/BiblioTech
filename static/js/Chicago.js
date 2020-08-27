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
    var entryNumber = 1;
    // Replace with Chichago formatting
    var entry = document.getElementById("result-entry").innerHTML = authorLastName + ", " + authorFirstName + '. "' + articleTitle + '." ' + "<em>" + publisherName + "</em>" + ", " + monthPublished + " " + dayPublished + " " + yearPublished + ", " + urlOfSource + ", " + "Accessed " + dateOfAccess + ".";
}
document.getElementById("submit-button").addEventListener("click", displayEntry);
