setTimeout(() => {

let button = document.getElementById('toggleSide');
button.addEventListener('click', e => {
    let panel = document.getElementById('right-column');
    let map = document.getElementById('left-column');
    if (panel.style.display == 'none') {
        map.className = "six columns";
        panel.style.display = 'block';
    }
    else {
        map.className = "nine columns";
        panel.style.display = 'none';
    }
});

}, 5000);

