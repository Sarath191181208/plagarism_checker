AOS.init();

function test() {
    alert("Choose a file in the selection menu to select the entire folder.")
    eel.selectFolder()(absPath => { eel.uploadFolder(absPath)(updateScores) });
}

function updateScores(res) {
    if (res === null) {
        alert("No valid data found In the given folder !")
    }

    let stuTable = document.getElementById("student-match-score-table");
    stuTable.innerHTML = "";
    let h = tableHeader("File Name", "File Name", "Match Score");
    stuTable.appendChild(h);

    let tableBody = document.createElement('tbody');
    res.forEach(ele => {
        const [fileName1, fileName2, matchScore] = ele;
        tableBody.appendChild(
            tr(
                td(fileName1),
                td(fileName2),
                td(matchScore)
            )
        );
    });

    stuTable.appendChild(tableBody);
    stuTable.scrollIntoView({
        behavior: 'smooth'
    });
}