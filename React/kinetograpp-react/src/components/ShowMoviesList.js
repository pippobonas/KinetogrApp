import React, { useState, useEffect } from 'react';
import RenderingMoviesList from './RenderingMoviesList'
import axios from 'axios';

const ShowMoviesList = () => {
  // Dichiarazione contenitore della lista dei film
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    // Recupero lista dei film
    axios.get('http://localhost:5000/moviesList')
      .then(response => {
        setMovies(response.data);
      })
      .catch(error => {
        console.error('Errore durante il recupero dei dati:', error);
      });
  }, []);

  return (
    // Passa il contenitore al componente che si occupa del rendering della lista dei film
    <RenderingMoviesList movies={movies} />
  );
};

export default ShowMoviesList;