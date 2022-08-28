function uploadFolderPath(folderPath) {

}
function compute() {
    console.log("compute")
    var data = 56;
    el.demo(data)(setValue)
}

function setValue(res) {
    console.log("res", res);
    document.getElementById("abc").innerHTML = res
}