AOS.init();
let globalData = null;

const views = {
    "Table": 1,
    "ProgressBar": 2,
    "SinglePage": 3
}
let view = views.ProgressBar;

function isValidData(data) {
    return !(data === null || data.length < 2)
}

function toggleView() {
    if (!(isValidData(globalData))) return;
    if (view === views.Table) view = views.ProgressBar
    else if (view === views.ProgressBar) view = views.Table

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

function singlePage(query_text, url, matchScore) {
    return $(`
    <span>
        ${query_text} <br>
        ${url} <br>
        ${matchScore} <br>
    </span>
    `);
}


function createSinglePage(data, root_container) {
    let singlePageContainer = $(`<div id="single-page-container"></div>`);
    root_container.append(singlePageContainer)
    singlePageContainer.innerHTML = "";

    data.forEach(ele => {
        console.log(ele);
        const [query_text, url, matchScore] = ele;
        //create a simple text viewver 
        singlePageContainer.append(singlePage(query_text, url, matchScore));
    });

    singlePageContainer[0].scrollIntoView({
        behavior: 'smooth'
    });
}

function createView() {
    if (!isValidData(globalData)) return;

    displayToggleViewButton(); // to change the icon of the button

    let container = $("#view-data-center")
    container.fadeOut(20);
    container.empty() // clearing the whole container

    if (view == views.Table) {
        createTable(globalData, container);
    }
    else if (view == views.ProgressBar) {
        createProgressBars(globalData, container);
    }
    else if (view == views.SinglePage) {
        createSinglePage(globalData, container);
    }
    container.fadeIn();
}

async function UploadFile() {
    $("#loading-container").addClass("show");
    $("#loading-container")[0].scrollIntoView();

    try {
        let absPath = await eel.selectFile()();
        console.log(absPath);
        let data = await eel.parseFileAndSearch(absPath)();
        console.log(data);

        if (data == null) {
            alert("No valid data found In the given file !")
            throw new Error("No valid data found In the given file !")
        }
        view = views.SinglePage;
        globalData = data;
        createView();

    }
    finally {
        $("#loading-container").removeClass("show");
    }
}

async function UploadFolder() {
    alert("Choose a file in the selection menu to select the entire folder.")
    $("#loading-container").addClass("show");
    $("#loading-container")[0].scrollIntoView();
    view = views.ProgressBar;

    try {
        let absPath = await eel.selectFolder()();
        console.log(absPath);
        let data = await eel.uploadFolder(absPath)();
        console.log(data);

        if (!isValidData(data)) {
            alert("No valid data found In the given folder !")
            throw new Error("No valid data found In the given folder !")
        }
        globalData = data;
        createView(); // creating the view to view the data from globalData
    }
    finally {
        $("#loading-container").removeClass("show");
    }


}