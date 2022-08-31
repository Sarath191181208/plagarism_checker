

function createProgressBars(data, root_container) {

    let progressContainer = $(`<div id="progress-container"></div>`);
    root_container.append(progressContainer)
    progressContainer.innerHTML = "";

    data.forEach(ele => {
        const [fileName1, fileName2, matchScore] = ele;
        progressContainer.append(progressBar(fileName1, fileName2, matchScore));
    });

    progressContainer[0].scrollIntoView({
        behavior: 'smooth'
    });

}

function progressBar(txt1, txt2, progressVal) {
    return $(`
    <div class="indiv-progress-bar-container">

        <div class="progress" data-percentage="${progressVal}">
            <div class="progress-value">
                    <div class="percentage-val">${progressVal}%</div>
            </div>
            <span class="progress-left">
                <span class="progress-bar"></span>
            </span>
            <span class="progress-right">
                <span class="progress-bar"></span>
            </span>
        </div>

        <div class="progress-txt-container">
            <div class="text1">${txt1}</div>
            <div class="text2">${txt2}</div>
        </div>

    </div>
    `);
}