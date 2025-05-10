import { Routes, Route } from 'react-router-dom'
import Home from './Home'
import Dashboard from './Dashboard'
import Analytics from './Analytics'

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/analytics" element={<Analytics />} />
    </Routes>
  )
}

