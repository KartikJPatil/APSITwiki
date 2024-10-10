// Get the URL hash
const hash = window.location.hash;

// Check if the hash contains #Lx where x is the line number
const lineMatch = hash.match(/#L(\d+)/);
if (lineMatch) {
    // Extract the line number from the match
    const lineNumber = parseInt(lineMatch[1]);

    // Redirect to searchresult.html passing the line number as a query parameter
    window.location.href = `searchresult.html?line=${lineNumber}`;

    // Highlight the line number in the redirected link for 2 seconds
    setTimeout(() => {
        // Get the line number from the query parameter in the redirected URL
        const params = new URLSearchParams(window.location.search);
        const redirectedLineNumber = parseInt(params.get('line'));

        // Highlight the line number in the redirected link
        // Replace this with your own code to highlight the line
        console.log(`Highlighting line ${redirectedLineNumber}`);
    }, 2000);
}
