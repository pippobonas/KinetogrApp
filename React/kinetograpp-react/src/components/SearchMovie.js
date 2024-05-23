import React, { useState } from 'react';
import RenderingMoviesList from './RenderingMoviesList';
import axios from 'axios';

const SearchMovie = () => {
  const [searchTitle, setSearchTitle] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [searched, setSearched] = useState(false);

  const handleSearch = async (event) => {
    event.preventDefault();
    try {
      // Ricerca del film per titolo
      const response = await axios.post('http://localhost:5000/searchMovie', { title: searchTitle });
      const results = response.data.results || [];
      setSearchResults(results);
    }
    catch (error) {
      console.error('Errore durante la ricerca dei film:', error.message);
      setSearchResults([]);
    }
    // Ricerca effettuata
    setSearched(true);
  };

  return (
    <div>
      {/* Form per la ricerca */}
      <h2>Ricerca Film per Titolo</h2>
      <form onSubmit={handleSearch}>
        <div>
          Inserisci il titolo del film:
          <input
            type="text"
            value={searchTitle}
            onChange={(e) => setSearchTitle(e.target.value)}
          />
          <button type="submit">
            Cerca
          </button>
        </div>
      </form>

      {/* Mostra i risultati della ricerca */}
      {searched && searchResults.length > 0 ? (
        <RenderingMoviesList movies={searchResults} />
      ) : (
        searched && <p>Nessun risultato trovato.</p>
      )}
    </div>
  );
};

export default SearchMovie;