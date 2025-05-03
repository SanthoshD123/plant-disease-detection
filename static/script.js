document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('upload-form');
    const fileInput = document.getElementById('file-input');
    const loading = document.getElementById('loading');
    const result = document.getElementById('result');
    const imagePreview = document.getElementById('image-preview');

    fileInput.addEventListener('change', function(e) {
        const file = e.target.files[0];
        if (file) {
            if (file.size > 5 * 1024 * 1024) { // 5MB limit
                alert('File is too large. Please choose a file smaller than 5MB.');
                this.value = ''; // Clear the file input
                return;
            }
            const reader = new FileReader();
            reader.onload = function(e) {
                imagePreview.innerHTML = `<img src="${e.target.result}" alt="Preview">`;
            }
            reader.readAsDataURL(file);
        }
    });

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        const formData = new FormData(form);

        loading.classList.remove('d-none');
        result.innerHTML = '';

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const contentType = response.headers.get("content-type");
            if (!contentType || !contentType.includes("application/json")) {
                throw new Error("Oops, we haven't got JSON!");
            }

            const data = await response.json();

            result.innerHTML = `
                <h3>Prediction: ${data.prediction}</h3>
                <p>Confidence: ${(data.confidence * 100).toFixed(2)}%</p>
            `;
        } catch (error) {
            console.error('Error:', error);
            result.innerHTML = `<h3>Error: ${error.message}</h3>`;
        } finally {
            loading.classList.add('d-none');
        }
    });
});