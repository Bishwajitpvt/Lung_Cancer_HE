import fs from "fs";
import data from "./data.json" assert { type: "json" };

const downloadFile = async (url, dir) => {
  const filename = unescape(url.split("?")[0].split("/").reverse()[0]);
  if (fs.existsSync(`./${dir}/${filename}`)) {
    return;
  }
  const file = await fetch(url);
  const blob = await file.blob();
  const buff = Buffer.from(await blob.arrayBuffer());
  fs.writeFile(`./${dir}/${filename}`, buff, (err) => {
    if (err) {
      console.log("Cannot Download: " + filename);
    } else {
      console.log("Downloaded: " + filename);
    }
  });
};

for (let key in data) {
  const dir = key;
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir);
  }
  for (let url of data[dir]) {
    downloadFile(url, dir);
  }
}
