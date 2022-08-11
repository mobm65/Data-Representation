function doAJAX(method, url, data, callback) {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        callback(JSON.parse(this.responseText));
    }
    xhttp.open(method, url, true);
    if(data) {
        xhttp.setRequestHeader("Content-Type", "application/json");
        xhttp.send(JSON.stringify(data));
    }
    else {
        xhttp.send();
    }
}

function writeDataToTablebody(data) {
    var tbody = document.getElementById('tablebody');
    tbody.textContent = '';
    for(var i in data) {
        let id = data[i].id;

        var tr = tbody.appendChild(document.createElement('tr'));
        tr.appendChild(document.createElement('td')).textContent = id;
        tr.appendChild(document.createElement('td')).textContent = data[i].name;
        tr.appendChild(document.createElement('td')).textContent = data[i].director;
        tr.appendChild(document.createElement('td')).textContent = data[i].filmgenre;
        tr.appendChild(document.createElement('td')).textContent = data[i].filmclassification;

        var deleteButtonTd = tr.appendChild(document.createElement('td'));
        var deleteButton = tr.appendChild(document.createElement('input'));
        deleteButton.type = 'button';
        deleteButton.value = 'delete';
        deleteButton.onclick = () => deleteFilm(id);
    }
}

function getFilms() {
    doAJAX("GET", "http://127.0.0.1:5000/film", null, writeDataToTablebody);
}

function addFilm() {
    var newFilm = {
        name: document.getElementById('name').value,
        director: document.getElementById('director').value,
        filmgenre: document.getElementById('filmgenre').value,
        filmclassification: document.getElementById('filmclassification').value
    };

    doAJAX("POST", "http://127.0.0.1:5000/film", newFilm, data => {
        getFilms();
    });
}

function deleteFilm(id) {
    doAJAX("DELETE", "http://127.0.0.1:5000/film/" + id, null, data => {
        getFilms();
    });
}

window.onload = getFilms
