const fs = require('fs');

// Function to update the JSON structure
function updateJsonStructure(jsonData) {
    return jsonData.map(article => {
        // Ensure 'tags' is an array
        if (typeof article.tags === 'string') {
            article.tags = [];
        }

        // Ensure 'related_articles' is an array
        if (typeof article.related_articles === 'string') {
            article.related_articles = [];
        }

        return article;
    });
}

// Main function to read, process, and write the JSON file
function main() {
    const inputFile = process.argv[2]; // Take the file name from the command line argument
    const outputFile = 'updated_' + inputFile;

    // Read the JSON file
    fs.readFile(inputFile, 'utf8', (err, data) => {
        if (err) {
            console.error('Error reading the file:', err);
            return;
        }

        try {
            const jsonData = JSON.parse(data);
            const updatedJsonData = updateJsonStructure(jsonData);

            // Write the updated JSON to a new file
            fs.writeFile(outputFile, JSON.stringify(updatedJsonData, null, 4), 'utf8', (err) => {
                if (err) {
                    console.error('Error writing the file:', err);
                    return;
                }
                console.log('File has been updated and saved as:', outputFile);
            });
        } catch (jsonErr) {
            console.error('Error parsing JSON:', jsonErr);
        }
    });
}

// Run the main function
main();