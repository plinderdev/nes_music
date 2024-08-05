// remove comma from last span with comma; td, give id


// Adds count of rows beneath "Rows" header in table
function addCountColumn() {
    const rows = document.querySelectorAll(
        "table tbody tr");
    let count;

    count = rows.length;
    for (let c = 0; c < count; c += 1) {
        rows[c].insertCell(0).innerText = rows.length - c;
    }

    // showCount(count);
}


window.addEventListener("DOMContentLoaded", addCountColumn);
