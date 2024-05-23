import React from 'react';
import { Route, Routes } from 'react-router-dom';

import ShowMoviesList from './components/ShowMoviesList';

function App() {
  return (
    <Routes>
      <Route path="/" element={<ShowMoviesList />} />
    </Routes>
  );
}

export default App;