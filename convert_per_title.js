const json2md = require("json2md");
const fs = require('fs');
const path = require('path');

// Function to process the JSON file and generate Markdown
function convertJSONtoMarkdown(inputFilePath, outputFolderPath) {
  const data = JSON.parse(fs.readFileSync(inputFilePath, 'utf8'));

  // Check if the data is an array or a single object
  const articlesToConvert = Array.isArray(data) ? data : [data]; 

  articlesToConvert.forEach((article, index) => {
    const firstLetters = article.title.split(' ').map(word => word.charAt(0).toUpperCase()).join('');
    const sanitizedTitle = article.title.replace(/[^a-z0-9]/gi, '_').toLowerCase(); // Sanitize title for filename
    const outputFileName = `ctt_${index + 1}_${firstLetters}.md`;
    const outputFilePath = path.join(outputFolderPath, outputFileName);

    
    // Extract only the "content" for the Markdown file
    const markdownContent = `# ${article.title}\n\n${article.content}`;

    fs.writeFileSync(outputFilePath, markdownContent);
    console.log(`Markdown generated successfully at: ${outputFilePath}`);
  });
}

// Function to process a folder of JSON files
function convertFolderToMarkdown(inputFolderPath, outputFolderPath) {
  fs.readdir(inputFolderPath, (err, files) => {
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
      const inputFilePath = path.join(inputFolderPath, file);
      convertJSONtoMarkdown(inputFilePath, outputFolderPath); 
    });
  });
}

// Function to process either a file or a folder
function convert(inputPath, outputPath) {
  const stat = fs.statSync(inputPath);
  if (stat.isDirectory()) {
    convertFolderToMarkdown(inputPath, outputPath);
  } else {
    const outputFolderPath = path.dirname(outputPath); // Use the directory of the output file
    convertJSONtoMarkdown(inputPath, outputFolderPath);
  }
}

// Get input and output paths from command line arguments
const inputPath = process.argv[2];
const outputPath = process.argv[3] || inputPath;

if (!inputPath) {
  console.error("Error: Please provide an input JSON file or folder.");
  console.error("Usage: node convert.js <input.json|input_folder> [output_folder]");
  process.exit(1); 
}

convert(inputPath, outputPath);

module.exports = { convertJSONtoMarkdown, convertFolderToMarkdown };