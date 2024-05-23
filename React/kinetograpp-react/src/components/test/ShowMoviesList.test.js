import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import axios from 'axios';
import ShowMoviesList from '../ShowMoviesList';

// Mock per axios
jest.mock('axios');

describe('ShowMoviesList', () => {
  test('fetch movies list and display movies list', async () => {
    // Dati di test restituiti dalla chiamata API
    const movies = [
      {
        id: 1,
        title: 'Movie 1',
        director: 'Director 1',
        release_year: 2023,
      },
      {
        id: 2,
        title: 'Movie 2',
        director: 'Director 2',
        release_year: 2024,
      },
    ];

    // Risposta con i dati di test
    axios.get.mockResolvedValueOnce({ data: movies });

    render(<ShowMoviesList />);

    // Verifica rendering della lista
    await waitFor(() => {
      movies.forEach(movie => {
        expect(screen.getByText(movie.title)).toBeInTheDocument();
        expect(screen.getByText(movie.director)).toBeInTheDocument();
        expect(screen.getByText(movie.release_year)).toBeInTheDocument();
      });
    });
  });

  test('API errors', async () => {
    // Risposta in caso di errore nel recupero della lista
    axios.get.mockRejectedValueOnce(new Error('Errore durante il recupero dei dati'));

    render(<ShowMoviesList />);

    // Verifica messaggio di errore
    await waitFor(() => {
      expect(screen.getByText('Nessun risultato trovato')).toBeInTheDocument();
    });
  });
});