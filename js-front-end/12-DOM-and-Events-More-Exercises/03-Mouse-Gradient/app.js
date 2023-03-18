function attachGradientEvents() {
    const box = document.getElementById('gradient');
    const result = document.getElementById('result');

    box.addEventListener('mousemove', moveIn);
    box.addEventListener('mouseout', moveOut);

    function moveIn(e) {
        let percentX = e.offsetX / (e.target.clientWidth);
        let percentY = 1 - (e.offsetY / (e.target.clientHeight));
        percentX = Math.trunc(percentX * 100);
        percentY = Math.trunc(percentY * 100);
        result.textContent = `X: ${percentX}% Y: ${percentY}%`;
    }
     function moveOut(e) {
        result.textContent = '';
     }
}