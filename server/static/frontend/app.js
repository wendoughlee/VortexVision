// static/frontend/app.js

// Setup camera
// navigator.mediaDevices.getUserMedia({ video: true })
//     .then(stream => {
//         document.getElementById('camera').srcObject = stream;
//     })
//     .catch(err => console.error('Camera error:', err));

// Upload files
function uploadFiles() {
    const files = document.getElementById('upload').files;
    for (const file of files) {
        const formData = new FormData();
        formData.append('file', file);

        fetch('/upload/', { method: 'POST', body: formData })
            .then(response => response.json())
            .then(data => {
                const img = document.createElement('img');
                img.src = '/uploads/' + data.filename;
                img.width = 200;
                document.getElementById('imageContainer').appendChild(img);
            });
    }
}
