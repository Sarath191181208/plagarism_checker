AOS.init();

async function test() {
    alert("Choose a file in the selection menu to select the entire folder.")
    $("#loading-container").addClass("show");
    eel.selectFolder()(absPath => {
        eel.uploadFolder(absPath)(data => {
            createTable(data);
            $("#loading-container").removeClass("show");
        });
    });
}