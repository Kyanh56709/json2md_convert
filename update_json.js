const fs = require('fs');
const path = require('path');

// Function to process a folder of JSON files
function updateJsonFields(folderPath) {
  fs.readdir(folderPath, (err, files) => {
    if (err) {
      console.error("Error reading the folder:", err);
      return;
    }

    const jsonFiles = files.filter(file => path.extname(file).toLowerCase() === '.json');

    if (jsonFiles.length === 0) {
      console.log("No JSON files found in the folder.");
      return;
    }

    jsonFiles.forEach(file => {
      const filePath = path.join(folderPath, file);

      try {
        const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));

        // Update "related_articles" and "tags" to empty arrays if they are empty strings
        if (data.related_articles === "") {
          data.related_articles = [];
        }
        if (data.tags === "") {
          data.tags = [];
        }

        fs.writeFileSync(filePath, JSON.stringify(data, null, 2));
        console.log(`Updated fields in: ${filePath}`);

      } catch (err) {
        console.error(`Error processing ${filePath}:`, err);
      }
    });
  });
}

// Get the folder path from command line arguments
const folderPath = process.argv[2];

if (!folderPath) {
  console.error("Error: Please provide the folder path.");
  console.error("Usage: node update_json.js <folder_path>");
  process.exit(1); 
}

updateJsonFields(folderPath);