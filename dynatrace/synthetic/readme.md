# Upload de pieces jointes
Ce script provient des forums Dynatrace

```bash
var cssselector = "input[type=file]"; //Replace with your file upload input selector
var data = "data&colon;text/plain;base64, RmlsZXVwbG9hZHRlc3Q="; //Convert your file into base64 format and assign it to the data variable. Make sure that file size should be minimum as we will be adding this code to our synthetic script.
var filename = "fileuploadtest.txt"; //Replace with the filename with the extension
const parts = data.split(';base64,');
const imageType = parts[0].split(':')[1];
const decodedData = window.atob(parts[1]);
const uInt8Array = new Uint8Array(decodedData.length);
for (let i = 0; i < decodedData.length; ++i) {
    uInt8Array[i] = decodedData.charCodeAt(i);
}
var blob = new Blob([uInt8Array], {
    type: imageType
});
var element = document.querySelector(cssselector);
var file = new File([blob], filename, {
    type: imageType
});
var container = new DataTransfer();
container.items.add(file);
element.files = container.files;
var evt = document.createEvent("HTMLEvents");
evt.initEvent("change", false, true);
element.dispatchEvent(evt);
```
Le fichier sera fourni codé en BASE64

# Liens utiles
```bash
https://docs.dynatrace.com/docs/platform-modules/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events
```
