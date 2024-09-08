#!/usr/bin/node

const axios = require('axios');

if (process.argv.length < 3) {
    console.error('Usage: node 0-starwars_characters.js <Movie ID>');
    process.exit(1);
}

const movieId = process.argv[2];
const baseUrl = 'https://swapi.dev/api/films/';

axios.get(`${baseUrl}${movieId}/`)
    .then(response => {
        const filmData = response.data;
        const characterUrls = filmData.characters;

        characterUrls.forEach(url => {
            axios.get(url)
                .then(response => {
                    const characterData = response.data;
                    console.log(characterData.name);
                })
                .catch(error => {
                    console.error('Error fetching character data:', error);
                });
        });
    })
    .catch(error => {
        console.error('Error fetching movie data:', error);
    });
