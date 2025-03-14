import { useEffect, useState } from "react";
import axios from "axios";

import logo from './flow_logo.png';
import './App.css';

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    axios.get("http://localhost:5000/api/message")
        .then(response => setMessage(response.data.message))
        .catch(error => console.error("Error fetching data:", error));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p className='flask_message'>
          {message || "Loading..."}
        </p>
      </header>
    </div>
  );
}

export default App;
