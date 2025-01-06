document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault();

    var localUrl = document.getElementById('local_url').value;
    var stopBtn = document.getElementById('stopBtn');
    var publicUrlDiv = document.getElementById('public_url');

    fetch('/deploy', {
        method: 'POST',
        body: new URLSearchParams({ 'local_url': localUrl })
    })
    .then(response => response.json())
    .then(data => {
        if (data.public_url) {
            publicUrlDiv.innerHTML = `Your public URL: <a href="${data.public_url}" target="_blank">${data.public_url}</a>`;
            stopBtn.style.display = 'inline-block';
        } else if (data.error) {
            publicUrlDiv.innerHTML = `Error: ${data.error}`;
        }
    });

    // Stop the tunnel when the button is clicked
    stopBtn.addEventListener('click', function() {
        fetch('/stop', { method: 'POST' })
            .then(response => response.json())
            .then(data => {
                if (data.status) {
                    publicUrlDiv.innerHTML = data.status;
                    stopBtn.style.display = 'none';
                }
            });
    });
});
