var slide = document.currentScript.getAttribute('slide_scene');
function loadFile(filePath) {
  var result = null;
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.open("GET", filePath, false);
  xmlhttp.send();
  if (xmlhttp.status==200) {
    result = xmlhttp.responseText;
  }
  console.log("load")
  return result;
}
frags = loadFile(`videos/${slide}.txt`)
document.write(`
<section data-background-video="videos/${slide}.mp4" data-background-color="#000000" id="vid" type="videoslide">
 ${frags}
</section>`)