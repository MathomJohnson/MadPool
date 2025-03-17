import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [rides, setRides] = useState([])

  useEffect(() => {
    fetchRides()
  }, [])

  const fetchRides = async () => {
    const response = await fetch('http://localhost:5000/rides')
    const data = await response.json()
    setRides(data.rides)
    console.log(data.rides)
  }

  return (
    <>
      
    </>
  )
}

export default App
