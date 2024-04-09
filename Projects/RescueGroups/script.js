const apiKey = 'deHtVSSY';
const apiUrl = 'https://api.rescuegroups.org/v5';

// Function to fetch animals
async function fetchAnimals() {
    const url = `${apiUrl}/animals`;
    
    try {
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${apiKey}`,
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error(`Failed to fetch animals: ${response.status} ${response.statusText}`);
        }

        const data = await response.json();
        // Process the data as needed
        console.log(data);
    } catch (error) {
        console.error('Error fetching animals:', error);
    }
}

