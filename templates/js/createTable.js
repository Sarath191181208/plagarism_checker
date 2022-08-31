function createTable(res, root_container) {
    let stuTable = $(`<table id="student-match-score-table" class="styled-table"></table>`)
    root_container.append(stuTable);

    // let stuTable = document.getElementById("student-match-score-table");
    stuTable.innerHTML = "";
    let h = tableHeader("File Name", "File Name", "Match Score");
    stuTable.append(h);

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

    stuTable.append(tableBody);
    stuTable[0].scrollIntoView({
        behavior: 'smooth'
    });

}