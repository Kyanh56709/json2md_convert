const json2md = require("json2md");
const fs = require('fs');
const path = require('path');

// Function to convert a single article to Markdown
function convertArticleToMarkdown(article) {
  return json2md([
    { h1: article.title },
    { p: `By: ${article.author.name} (${article.author.email})` },
    { p: `Published on: ${article.date_published}` },
    { p: article.summary },
    { h2: "Content" },
    { p: article.content }, 
    { h2: "Categories" },
    { ul: article.categories },
    { h2: "Tags" },
    { ul: article.tags },
    { h2: "Related Articles" },
    { ul: article.related_articles.map(a => ({ link: { title: a.title, source: a.link } })) },
    { hr: '' } // Separator between articles
  ]);
}

// Function to process the JSON file and generate Markdown
function convertJSONtoMarkdown(inputFilePath, outputFilePath) {
  const data = JSON.parse(fs.readFileSync(inputFilePath, 'utf8'));

  // Check if the data is an array or a single object
  const articlesToConvert = Array.isArray(data) ? data : [data]; 

  const allMarkdownContent = articlesToConvert.map(convertArticleToMarkdown).join('\n'); 
  fs.writeFileSync(outputFilePath, allMarkdownContent);
  console.log(`Markdown generated successfully at: ${outputFilePath}`);
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
      const outputFileName = file.replace('.json', '.md');
      const outputFilePath = path.join(outputFolderPath, outputFileName);

      convertJSONtoMarkdown(inputFilePath, outputFilePath); 
    });
  });
}

// Function to process either a file or a folder
function convert(inputPath, outputPath) {
  const stat = fs.statSync(inputPath);
  if (stat.isDirectory()) {
    convertFolderToMarkdown(inputPath, outputPath);
  } else {
    convertJSONtoMarkdown(inputPath, outputPath);
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