document.getElementById('submitCoordinates').addEventListener('click', async () => {
    const latitude = document.getElementById('latitude').value;
    const longitude = document.getElementById('longitude').value;

    // Backend'e POST isteği gönder
    const response = await fetch('/classify', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            latitude: latitude,
            longitude: longitude
        })
    });

    // Gelen yanıtı işleyin
    const data = await response.json();
    document.getElementById('resultsDisplay').innerText = `Sonuç: ${data.result}`;
});
