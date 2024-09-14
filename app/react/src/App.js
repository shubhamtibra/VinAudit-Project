import React from 'react';
import './App.css';
import VehicleForm from './components/VehicleForm';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>VinAudit Vehicle Listing</h1>
      </header>
      <main>
        <div className="vehicle-form-container">
          <VehicleForm />
        </div>
      </main>
      <footer>
        <p>&copy; 2023 VinAudit Pvt Ltd</p>
      </footer>
    </div>
  );
}

export default App;
