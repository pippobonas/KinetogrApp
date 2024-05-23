import React from 'react';

function RenderMoviesList({ movies }) {
  return (
    <div>
      {movies.length === 0 ? (
        <p>Nessun risultato trovato</p>
      ) : (
        movies.map(movie => (
          <div className='movie-card' key={movie.id}>
            <p className='card-title'>{movie.title}</p>
            <p className='card-director'>{movie.director}</p>
            <p className='card-plot'>{movie.plot}</p>
            <p className='card-year'>{movie.release_year}</p>
            <img className='card-poster' src={movie.poster_path} alt={`${movie.title} poster`} />
            <p className='card-services'>{movie.services_available}</p>
          </div>
        ))
      )}
    </div>
  );
}

export default RenderMoviesList;