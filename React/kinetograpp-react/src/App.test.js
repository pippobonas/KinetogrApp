import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import axios from 'axios';
import MockAdapter from 'axios-mock-adapter';
import App from './App';

// Mock per Axios
const mock = new MockAdapter(axios);

// Richiesta lista dei film
mock.onGet('http://localhost:5000/moviesList').reply(200, [
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
]);

// Ricerca film per titolo
mock.onPost('http://localhost:5000/searchMovie').reply(200, {
  results: [
    {
      id: 1,
      title: 'Movie 1',
    },
    {
      id: 2,
      title: 'Movie 2',
    },
  ]
});

// Inizializza MemoryRouter alla rotta /
test('renders ShowMoviesList for "/" route', async () => {
  render(
    <MemoryRouter initialEntries={['/']}>
      <App />
    </MemoryRouter>
  );

  // Attesa rendering elementi di test
  await waitFor(() => {
    expect(screen.getByText(/Movie 1/i)).toBeInTheDocument();
    expect(screen.getByText(/Movie 2/i)).toBeInTheDocument();
  });
});