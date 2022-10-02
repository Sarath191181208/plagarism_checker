AOS.init();
let globalData = null;

const views = {
    "Table": 1,
    "ProgressBar": 2
}
let view = views.ProgressBar;

function isValidData(data) {
    return !(data === null || data.length < 2)
}

function toggleView() {
    if (!(isValidData(globalData))) return;
    if (view === views.Table) view = views.ProgressBar
    else if (view === views.ProgressBar) view = views.Table

    displayToggleViewButton(); // to change the icon of the button
    createView(); // to react to change the state
}

function getImgAttr() {
    let svg_folder_path = "./images/icons/"
    let svg_icon;
    if (view === views.Table) svg_icon = "circle-notch-solid.svg";
    else svg_icon = "table-solid.svg"
    return svg_folder_path + svg_icon;
}

function displayToggleViewButton() {
    let toggleViewBtn = $("#toggle-view-btn");
    toggleViewBtn.children().attr('src', getImgAttr())
}

function createView() {
    if (!isValidData(globalData)) return;

    let container = $("#view-data-center")
    container.fadeOut(20);
    container.empty() // clearing the whole container

    if (view == views.Table) {
        createTable(globalData, container);
    }
    else {
        createProgressBars(globalData, container);
    }
    container.fadeIn();
}

async function test() {
    alert("Choose a file in the selection menu to select the entire folder.")
    $("#loading-container").addClass("show");
    $("#loading-container")[0].scrollIntoView();

    try {
        let absPath = await eel.selectFolder()();
        console.log(absPath);
        let data = await eel.uploadFolder(absPath)();
        console.log(data);
        
        if (!isValidData(data)) {
            alert("No valid data found In the given folder !")
            throw  new Error("No valid data found In the given folder !")
        }
        globalData = data;
        createView(); // creating the view to view the data from globalData
    }
    finally {
        $("#loading-container").removeClass("show");
    }


}

displayToggleViewButton();
// displayToggleViewButton();