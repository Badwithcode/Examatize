import React from 'react'
import { Link } from 'react-router-dom'

const Dashboard = () => {
  return (
    <div className='m-2 bg-gray-200'>
      <h2>Dashboard</h2>
      <div>
          <Link to="/upcomingtest">Upcoming test</Link>
      </div>
      <div>
          <Link to="/previoustest">Prev test</Link>
      </div>
    </div>
  )
}

export {Dashboard}