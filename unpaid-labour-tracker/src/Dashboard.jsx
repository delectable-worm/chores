import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
export default function Dashboard() {
  const navigate = useNavigate()
  const [task, setTask] = useState('')
  const [tasks, setTasks] = useState([])
  const person = localStorage.getItem('name');
  const household = localStorage.getItem('hhname');
  const handleSetTasks = () => {
    setTasks([...tasks, task])
    setTask('')
  }
  const goToAnalytics= () => {
    navigate('/analytics')
  }


  return (
    <div className="flex flex-col items-center justify-center min-h-screen text-white">
      <h1 className="text-4xl font-bold mb-4">Welcome {person} !</h1>
      <p className="text-lg">Log tasks as {person} for household {household}</p>
      <input type="text" name="task" id="task" value={task} onChange={(e)=>setTask(e.target.value)}></input>
      <button onClick={handleSetTasks}>Log tasks</button>
      <ul>
        {tasks.map((t, index) => (
          <li key={index}>
            {t}
          </li>
        ))}
      </ul>
      <br></br>
      <button onClick={goToAnalytics} value="See Analytics">See Analytics</button>
      
    </div>
  )
}

//export default Dashboard
