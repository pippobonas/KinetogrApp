import React from 'react';
import { Route, Routes } from 'react-router-dom';

import ShowMoviesList from './components/ShowMoviesList';
import SearchMovie from './components/SearchMovie';

function App() {
  return (
    <Routes>
      <Route path="/" element={<ShowMoviesList />} />
      <Route path="/searchMovie" element={<SearchMovie />} />
    </Routes>
  );
}

export default App;