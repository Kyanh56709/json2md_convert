const json2md = require("json2md");
const fs = require('fs');

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
  const allMarkdownContent = data.map(convertArticleToMarkdown).join('\n'); 
  fs.writeFileSync(outputFilePath, allMarkdownContent);
  console.log(`Markdown generated successfully at: ${outputFilePath}`);
}

// Get input and output file paths from command line arguments
const inputFilePath = process.argv[2];
const outputFilePath = process.argv[3] || inputFilePath.replace('.json', '.md');

// Check if an input file is provided
if (!inputFilePath) {
  console.error("Error: Please provide an input JSON file.");
  console.error("Usage: npm run convert <input.json> [output.md]");
  process.exit(1); 
}

convertJSONtoMarkdown(inputFilePath, outputFilePath);

module.exports = { convertJSONtoMarkdown }; // Export for potential testing