#!/usr/bin/node


const request = require('request');

if (process.argv.length < 3) {
    console.error('Usage: node starwars_characters.js <Movie ID>');
    process.exit(1);
}

const movieId = process.argv[2];
const baseUrl = 'https://swapi.dev/api/films/';

request(`${baseUrl}${movieId}/`, (error, response, body) => {
    if (error) {
        console.error('Error fetching movie data:', error);
        return;
    }

    if (response.statusCode !== 200) {
        console.error('Failed to fetch movie data. Status code:', response.statusCode);
        return;
    }

    const filmData = JSON.parse(body);
    const characterUrls = filmData.characters;

    characterUrls.forEach((url) => {
        request(url, (error, response, body) => {
            if (error) {
                console.error('Error fetching character data:', error);
                return;
            }

            if (response.statusCode !== 200) {
                console.error('Failed to fetch character data. Status code:', response.statusCode);
                return;
            }

            const characterData = JSON.parse(body);
            console.log(characterData.name);
        });
    });
});
