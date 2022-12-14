// Select size input
// When size is submitted by the user, call makeGrid()
// Clear the grid after submit

let gridSize = document.querySelector('#sizePicker');

gridSize.addEventListener('submit', function (event) {
    let height = document.querySelector('#inputHeight');
    let width = document.querySelector('#inputWidth');
    event.preventDefault();
    document.querySelector('#pixelCanvas').innerHTML = '';
    makeGrid(height.value, width.value);   
})

// Create grid based on user input, add selected color to cells
function makeGrid(heightValue, widthValue) {
    let table = document.querySelector('#pixelCanvas');
    let color = document.querySelector('#colorPicker');
    for (var r = 1; r <= heightValue; r++) {
        let addRow = table.insertRow(-1);
        for (var c = 1; c <= widthValue; c++) {  
            let addCell = addRow.insertCell(0);
            addCell.addEventListener('click', function() {
                addCell.style.backgroundColor = color.value;
            });  
        }
    }               
}
