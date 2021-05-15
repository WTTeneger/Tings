function Ope(e) {
    id = e.id;

    for (iterator of document.getElementsByName('B_1')) {
        // console.log(iterator);
        iterator.classList.remove('bActive')

    }
    for (iterator of document.getElementsByName('B_2')) {
        // console.log(iterator);
        iterator.style.display = 'none'

    }
    console.log(e);
    document.getElementById("O" + e.id).style.display = 'block';
    e.classList.add('bActive')

    console.log(e, id);

}