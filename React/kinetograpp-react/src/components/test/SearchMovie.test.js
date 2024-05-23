import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import axios from 'axios';
import MockAdapter from 'axios-mock-adapter';
import SearchMovie from '../SearchMovie';

// Mock per axios
const mock = new MockAdapter(axios);

// Risposta con i dati di test
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

describe('SearchMovie', () => {
  // Test per la ricerca con successo
  test('renders searched movie info', async () => {
    render(<SearchMovie />);

    // Verifica rendering del form di ricerca
    await waitFor(() => {
      expect(screen.getByText(/Inserisci il titolo del film/i)).toBeInTheDocument();
      expect(screen.getByText('Cerca')).toBeInTheDocument();
    });

    // Simulazione ricerca
    fireEvent.change(screen.getByRole('textbox'), {
      target: { value: 'Movie 1' },
    });
    fireEvent.click(screen.getByText('Cerca'));

    // Verifica rendering risultati della ricerca
    await waitFor(() => {
      expect(screen.getByText(/Movie 1/i)).toBeInTheDocument();
      expect(screen.getByText(/Movie 2/i)).toBeInTheDocument();
    });

    // Verifica che il messaggio di errore non sia presente
    await waitFor(() => {
      expect(screen.queryByText('Nessun risultato trovato.')).not.toBeInTheDocument();
    });
  });

  // Test per la ricerca senza successo
  test('renders error message when no movies are found', async () => {
    // Risposta quando il film non è stato trovato
    mock.onPost('http://localhost:5000/searchMovie').reply(200, { results: [] });

    render(<SearchMovie />);

    // Attesa rendering del form di ricerca
    await waitFor(() => {
      expect(screen.getByText(/Inserisci il titolo del film/i)).toBeInTheDocument();
      expect(screen.getByText('Cerca')).toBeInTheDocument();
    });

    // Simulazione ricerca
    fireEvent.change(screen.getByRole('textbox'), {
      // Inseriamo il titolo di un film che non è presente
      target: { value: 'Test Movie' },
    });
    fireEvent.click(screen.getByText('Cerca'));

    // Verifica messaggio di errore
    await waitFor(() => {
      expect(screen.getByText('Nessun risultato trovato.')).toBeInTheDocument();
    });
  });

  afterEach(() => {
    mock.reset();
  });
});