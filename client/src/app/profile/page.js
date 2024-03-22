'use client'
import React, { useEffect, useState } from 'react'

const Page = () => {
  const [data, setdata] = useState([])
  const [isLoading, setIsLoading] = useState(true)
  useEffect(() => {
    fetchdata()
  }, [])
  async function fetchdata(){
    try{
    //   const resp=await fetch('http://127.0.0.1:5000/profile',{
    //   method: 'GET',
    //   headers: {
    //     'Authorization': 'Bearer '+localStorage.getItem('token')
    //   }
    // })
    
    // const response=await resp.json();
    const response={
      "status": true,
      "User": {
          "roll_no": "21EC087",
          "user_name": "student",
          "email": "student.2021eceb@sece.ac.in",
          "phone": 9940117877,
          "batch": 2025,
          "dept": "ECE",
          "role": "student"
      }
  }
  
    console.log(response)
    setdata(response.User)
    setIsLoading(false)
  }
  catch(err){
    console.log(err)
  }


}
  if(isLoading) return <div><p>Loading...</p></div>
  if(!isLoading){
    return (
      <>
      <div className='pl-10 pt-10  w-[30%] '>

        <div className='shadow-2xl rounded-2xl flex flex-col items-center'>
        <div className=''>
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" className="px-2 w-10 h-10 flex justify-center items-center ">
            <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z" />
          </svg>
        </div>
        <div>

          <div className=' p-2 my-2 text-center'>
            <p className='px-4 '>Name:</p>
            <p className='py-2'>{data.user_name}</p>
          </div>
          <div className='   p-2 my-2 text-center'>
            <p  className='px-4 '>Email:</p>
            <p className='py-2'>{data.email}</p>
          </div>
          <div className=' px-2 py-2 my-1 text-center'>
            <p  className='px-4 '>Phone:</p>
            <p className='py-2'>{data.phone}</p>
          </div>
          <div className=' px-2 py-2 my-1 text-center'>
            <p  className='px-4 '>Batch:</p>
            <p className='py-2'>{data.batch}</p>
          </div>
          <div className=' px-2 py-2 my-1 text-center'>
            <p  className='px-4 '>Department:</p>
            <p className='py-2'>{data.dept}</p>
          </div>
          <div/>

        </div>
      </div>
      </div>

      </>
  
    )
  }
}

export default Page