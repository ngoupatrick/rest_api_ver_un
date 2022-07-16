function loads() {
    var uname = document.getElementById('uname').value;
    var psw = document.getElementById('psw').value;

    var url = "https://nanpson.pythonanywhere.com/login";

    var xhr = new XMLHttpRequest();
    xhr.open("POST", url);

    xhr.setRequestHeader("Authorization", "Basic " + window.btoa(uname + ":" + psw));
    xhr.onload = function() {
        if (this.status == 200) {
            //document.getElementById("rep").innerHTML = this.response;
            getUsers()
        } else {

            alert("HTTP ERROR " + this.status);
        }
    };
    xhr.send();
    return false;
}

const savepatient = () => {
    var name_ = document.getElementById('nom').value
    var sexe = document.getElementById('sexe').value

    var data = new FormData();
    data.append("nom", name_);
    data.append("sexe", sexe);

    var myHeaders = new Headers();
    myHeaders = new Headers({
        "Content-Type": "application/json",
        //"Content-Length": content.length.toString(),
        "X-Custom-Header": "ProcessThisImmediately",
        "x-access-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWlkIjoiNzUwZjBhYzMtN2I5MC00YjgwLTgzZGUtMmQ1ZWE0ZTQ4NTBhIiwiZXhwIjoxNjU3OTE4MjgwfQ.o9gCIhN14FijVG8ZpDKb1N05sH1QJm_CP_R3REbpZ-o",
    });
    var myInit = {
        method: 'POST',
        headers: myHeaders,
        //mode: 'cors',
        body: data,
        cache: 'default'
    };
    var url = 'https://nanpson.pythonanywhere.com/V1/patient';
    fetch(url, { method: "POST", body: data });

    /*
    var myRequest = new Request(url, myInit);
    fetch(myRequest)
        .then(function(response) {
            alert("ici 1")
            console.log(response.json())
            return response.json()
        })
        .then(function(data) {
            alert("ici 2")
            console.log(data)
            rep = document.getElementById("rep")
            rep.innerHTML = data
        }).catch(error => console.error('Error:', error));
    
    rep = document.getElementById("rep")
    rep.innerHTML = sexe;*/
}

const getUsers = () => {
    var myHeaders = new Headers();
    myHeaders = new Headers({
        "Content-Type": "application/json",
        //"Content-Length": content.length.toString(),
        "X-Custom-Header": "ProcessThisImmediately",
        "x-access-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWlkIjoiNzUwZjBhYzMtN2I5MC00YjgwLTgzZGUtMmQ1ZWE0ZTQ4NTBhIiwiZXhwIjoxNjU3OTE4MjgwfQ.o9gCIhN14FijVG8ZpDKb1N05sH1QJm_CP_R3REbpZ-o",
    });
    var myInit = {
        method: 'GET',
        headers: myHeaders,
        //mode: 'cors',
        cache: 'default'
    };
    var url = 'https://nanpson.pythonanywhere.com/V1/users'
    var myRequest = new Request(url, myInit);
    fetch(myRequest) // Fetch for all scores. The response is an array of objects that is sorted in decreasing order
        .then(res => res.json())
        .then(users => {
            createUserboardTable() // Clears scoreboard div if it has any children nodes, creates & appends the table
                // Iterates through all the objects in the scores array and appends each one to the table body
            for (const user_ of users) {
                let userIndex = users.indexOf(user_) + 1 // Index of score in score array for global ranking (these are already sorted in the back-end)
                appendUsers(user_, userIndex) // Creates and appends each row to the table body
            }
        })
}

const createUserboardTable = () => {
    const scoreDiv = document.querySelector("#scoreboard") // Find the scoreboard div in our html
    let tableHeaders = ["No", "Nom", "Prenom", "Tel", "Sexe", "Adresse", "Created"]
    while (scoreDiv.firstChild) scoreDiv.removeChild(scoreDiv.firstChild) // Remove all children from scoreboard div (if any)
    let scoreboardTable = document.createElement('table') // Create the table itself
    scoreboardTable.className = 'scoreboardTable'
    let scoreboardTableHead = document.createElement('thead') // Creates the table header group element
    scoreboardTableHead.className = 'scoreboardTableHead'
    let scoreboardTableHeaderRow = document.createElement('tr') // Creates the row that will contain the headers
    scoreboardTableHeaderRow.className = 'scoreboardTableHeaderRow'
        // Will iterate over all the strings in the tableHeader array and will append the header cells to the table header row
    tableHeaders.forEach(header => {
        let scoreHeader = document.createElement('th') // Creates the current header cell during a specific iteration
        scoreHeader.innerText = header
        scoreboardTableHeaderRow.append(scoreHeader) // Appends the current header cell to the header row
    })
    scoreboardTableHead.append(scoreboardTableHeaderRow) // Appends the header row to the table header group element
    scoreboardTable.append(scoreboardTableHead)
    let scoreboardTableBody = document.createElement('tbody') // Creates the table body group element
    scoreboardTableBody.className = "scoreboardTable-Body"
    scoreboardTable.append(scoreboardTableBody) // Appends the table body group element to the table
    scoreDiv.append(scoreboardTable) // Appends the table to the scoreboard div
}

// The function below will accept a single score and its index to create the global ranking
const appendUsers = (user, userIndex) => {
    const scoreboardTable = document.querySelector('.scoreboardTable') // Find the table we created
    let scoreboardTableBodyRow = document.createElement('tr') // Create the current table row
    scoreboardTableBodyRow.className = 'scoreboardTableBodyRow'
        // Lines 72-85 create the 5 column cells that will be appended to the current table row
    let userNo = document.createElement('td')
    userNo.innerText = userIndex
    let userName = document.createElement('td')
    userName.innerText = user.nom
    let userPrenom = document.createElement('td')
    userPrenom.innerText = user.prenom
    let userTel = document.createElement('td')
    userTel.innerText = user.tel
    let userSexe = document.createElement('td')
    userSexe.innerText = user.sexe
    let userAdresse = document.createElement('td')
    userAdresse.innerText = user.adresse
    let userCreated = document.createElement('td')
    userCreated.innerText = user.created
    scoreboardTableBodyRow.append(userNo, userName, userPrenom, userTel, userSexe, userAdresse, userCreated) // Append all 5 cells to the table row
    scoreboardTable.append(scoreboardTableBodyRow) // Append the current row to the scoreboard table body
}