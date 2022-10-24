const container = document.querySelector('#container');
const fileInput = document.querySelector('#file-input');

const nets = faceapi.nets;

async function init() {

    await Promise.all([
        faceapi.nets.ssdMobilenetv1.loadFromUri('/models'),
        faceapi.nets.faceLandmark68Net.loadFromUri('/models'),
        faceapi.nets.faceRecognitionNet.loadFromUri('/models')
    ])
}

init()

fileInput.addEventListener('change', async (e) => {
    const file = fileInput.files[0];
    document.body.append('loaded...');

    const image = await faceapi.bufferToImage(file)
    const canvas = faceapi.createCanvasFromMedia(image)

    const size = {
        width: canvas.width,
        height: canvas.height
    }

    const detection = await faceapi.detectAllFaces(image).withFaceLandmarks().withFaceDescriptors()
    const resizedDetections = faceapi.resizeResults(detection, size)

    for (const detection of resizedDetections) {
        const box = detection.detection.box
        const drawBox = new faceapi.draw.DrawBox(box, {
            label: 'Face'
        })
        drawBox.draw(canvas)
    }

    
    container.innerHTML = ''
    container.append(image);
    container.append(canvas);
})