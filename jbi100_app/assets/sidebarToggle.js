setTimeout(() => {

let button = document.getElementById('toggleSide');
button.addEventListener('click', e => {
    let panel = document.getElementById('right-column');
    if (panel.style.display == 'none') {
        panel.style.display = 'block';
    }
    else {
        panel.style.display = 'none';
    }
});

}, 5000);

