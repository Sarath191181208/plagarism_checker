function td(str) {
    let _td = document.createElement('td');
    _td.innerHTML = str;
    return _td;
}

function th(str) {
    let _th = document.createElement('th');
    _th.innerHTML = str;
    return _th
}

function thead(obj) {
    let _thead = document.createElement('thead');
    _thead.appendChild(obj);
    return _thead;
}

function tr(...arguments) {
    let _tr = document.createElement('tr');
    arguments.forEach(ele => {
        _tr.appendChild(ele)
    });

    return _tr;
}

function tableHeader(...arguments) {
    return thead(tr(...arguments.map(th)));
}
