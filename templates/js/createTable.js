function createTable(res) {

    if (res === null) {
        alert("No valid data found In the given folder !")
        return;
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