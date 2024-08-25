/*
Author: Plinder
Program name: NES music index
*/


// Adds count of rows beneath "Rows" header in table
function addCountColumn() {
    const rows = document.querySelectorAll("table tbody tr");
    let count;

    count = rows.length;
    for (let c = 0; c < count; c += 1) {
        rows[c].insertCell(0).innerText = rows.length - c;
    }
}


function shiftThe() {
    const cells = document.querySelectorAll("table tbody tr td");
    const the = ", The";

    for (let c = 0; c < cells.length; c += 1) {
        if (cells[c].innerText.includes(the)) {
            let moveThe =
                cells[c].innerText.substring(cells[c].innerText.length - 3);
            let newString = cells[c].innerText.replace(moveThe, "");
            newString = moveThe.concat(" ", newString);
            newString = newString.slice(0, -2);  // Remove comma and space
            cells[c]. innerText = newString;
        }
        // Can write an else here for "A ", maybe rework above, put in a function
    }
}


window.addEventListener("DOMContentLoaded", addCountColumn);
window.addEventListener("DOMContentLoaded", shiftThe);
