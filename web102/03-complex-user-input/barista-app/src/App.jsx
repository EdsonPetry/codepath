import { useState } from 'react'
import './App.css'
import BaristaForm from './components/BaristaForm'


function App() {
  const [coffee, setCoffee] = useState(0)

  return (
    <div>
        <div className = 'title-container'>

        <h1 className='title'>On my grind</h1>
        <p>So you think you can barista? Lets put that to the test</p>

        </div>

        <BaristaForm/>
    </div>
    
  );

}

export default App
