'use client'
import Testbox from '@/Components/Testbox'
import React, {useEffect, useState} from 'react'
import styles from '../../../css/upcoming.module.scss'

const Page=()=> {

  const [testbox, settestbox] = useState();
  const [IsLoading, setIsLoading] = useState(true)
  useEffect(()=>{
    fetch('/api/upcoming',{
      method: 'GET',
      headers: {
        'Authorization': 'Bearer '+localStorage.getItem('token')
      }
    })
    .then((resp)=>
      resp.json()
    )
    .then((data)=>{
      settestbox(data.Batches)
      setIsLoading(false)
    })
    .catch((err)=>{
      console.log("Error : "+err)
    })
  },[])
  console.log(testbox)
  
  if(IsLoading){
    return <div>Loading...</div>
  }

  return (
    <div>
      <div className={styles.upcoming+" mt-3 mx-8 bg-slate-100 bg-opacity-85 min-h-[644px]"}>
      <p className={" text-[40px] flex justify-center text-[#767373] text-center  text-stroke-10"}>UPCOMING TEST</p>
      <div className="flex flex-row flex-wrap justify-center">
        {testbox && testbox.map((test, index) => {
          return <Testbox key={index} test={test}/>
        })}
      </div> 
    </div>
    </div>
  )
}

export default Page