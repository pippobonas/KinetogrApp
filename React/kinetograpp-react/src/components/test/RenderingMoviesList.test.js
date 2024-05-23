import React from 'react';
import { render, screen } from '@testing-library/react';
import RenderMoviesList from '../RenderingMoviesList';

describe('RenderMoviesList', () => {
  test('renders movies list', () => {
    // Dati di test
    const movies = [
      {
        id: 1,
        title: 'Movie 1',
        director: 'Director 1',
        plot: 'plot 1',
        release_year: 2023,
        poster_path: './path/movie1.png',
        services_available: 'Netflix',
      },
      {
        id: 2,
        title: 'Movie 2',
        director: 'Director 2',
        plot: 'plot 2',
        release_year: 2024,
        poster_path: './path/movie2.png',
        services_available: 'Netflix, Hulu',
      },
    ];

    // Passiamo la lista al componente RenderMoviesList
    render(<RenderMoviesList movies={movies} />);

    // Verifica rendering della lista
    movies.forEach(movie => {
      expect(screen.getByText(movie.title)).toBeInTheDocument();
      expect(screen.getByText(movie.director)).toBeInTheDocument();
      expect(screen.getByText(movie.plot)).toBeInTheDocument();
      expect(screen.getByText(movie.release_year.toString())).toBeInTheDocument();
      expect(screen.getByAltText(`${movie.title} poster`)).toHaveAttribute('src', movie.poster_path);
      expect(screen.getByText(movie.services_available)).toBeInTheDocument();
    });
  });

  test('renders empty movies list', () => {
    // Passiamo una lista vuota al componente RenderMoviesList
    render(<RenderMoviesList movies={[]} />);

    // Verifica messaggio di errore
    expect(screen.getByText('Nessun risultato trovato')).toBeInTheDocument();
  });
});