import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
export default function Analytics() {
  const navigate = useNavigate()
  const goToDash = () => {
    navigate('/dashboard')
  }
  return (
    <div className="flex flex-col items-center justify-center min-h-screen text-white">
      <h1 className="text-4xl font-bold mb-4">Welcome!</h1>
      <p className="text-lg">Analytics</p><br></br>
      <p>in your household u contribute to 30% of the chores. this is a good amount</p><br></br>
      <p>see a better breakdown of the chores below</p>
      <br></br>
      <button onClick={goToDash}>Back to Task Logger</button>
    </div>
  )
}

