function uploadFolderPath(folderPath) {

}
function compute() {
    abs_folder_path = "E:/Sarath/python/Plagarism_cheker/data"
    e = '.txt'
    eel.uploadFolder(abs_folder_path, e)(setValue)
}

function setValue(res) {
    let stuTable = document.getElementById("student-match-score-table");
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

}