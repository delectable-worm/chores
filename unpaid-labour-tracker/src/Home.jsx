import { useState } from 'react'
import './App.css'
import { useNavigate } from 'react-router-dom'

export default function Home() {
  const navigate = useNavigate()
  const [name, setName] = useState('')
  const [hh_name, setHHName] = useState('')

  const handleCreate = () => {
    localStorage.setItem('hhname', hh_name)
    localStorage.setItem('name', name);
    navigate('/dashboard')
  }

  const handleJoin = () => {
    localStorage.setItem('label', 'value')
    localStorage.setItem('label', 'value')
    navigate('/dashboard')
  }

  return (
    <>
      <div>
        <h1>hello</h1>
        <input type="text" value = {hh_name} onChange={(e)=>setHHName(e.target.value)} placeholder="Household" id="hhname" name = "hhname"></input><br></br>
        <input type="text" value = {name} onChange={(e)=>setName(e.target.value)} placeholder="Your name" id="name" name = "name"></input><br></br>
        <input type="submit" value="Join" onClick={handleJoin}></input><br></br>
        <input type="submit" value="Create" onClick={handleCreate}></input>
      </div>
    </>
  )
}

//export default Home
