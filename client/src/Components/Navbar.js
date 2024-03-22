'use client'
import Link from 'next/link'
import { useRouter } from 'next/navigation'
import React, { useEffect, useState } from 'react'
import dp from '../Components/dppro.jpg'
import Image from 'next/image'

const Navbar = () => {

  const route = useRouter()
  const [TestDropdown, setTestDropdown] = useState(false)
  const [ManageDropDown, setManageDropDown] = useState(false)
  const [ProfileDropdown, setProfileDropdown] = useState(false)

  const [Role, setRole] = useState('')
  const [IsLoading, setIsLoading] = useState(true)

  useEffect(()=>{

    async function fetchdata(){
      const resp = await fetch('/api/token',{
        method: 'GET',
        headers: {
          'Authorization': 'Bearer '+localStorage.getItem('token')
        }
      })
      const data = await resp.json()
      if(data.status){
        setRole(data.role)
        setIsLoading(false)
      } else {
        route.replace('/login')
      }
    }
    fetchdata()
  },[])
  
  

  const handlelogout = ()=>{
    fetch('/api/logout', {
      method: 'GET',
      headers: {
        'Authorization': 'Bearer ' + localStorage.getItem('token')
      }
    })
    .then(response => response.json())
    .then(data => {
      if (data.status === true) {
        localStorage.removeItem('token');
        route.replace('/login');
      }
    })
    .catch(err => {
      console.error(err);
    });
    console.log("logout");
  }
    
    if (IsLoading) {
      return (
        <div>Loading...</div>
      );
    }

  return (
    <div>
      <nav className=" bg-[#ffffff] rounded-b-[40px] py-100px mx-[3%] ">
        <div className={" max-w-screen-xl rounded-lg flex flex-wrap items-center justify-between mx-auto p-4 "}>
            <div id='logodiv' className="flex items-center space-x-3 rtl:space-x-reverse">
                <img src="https://flowbite.com/docs/images/logo.svg" className="h-8" alt="Examatize Logo" />
                <span className=" text-3xl font-semibold whitespace-nowrap text-[#444242]">Examatize</span>
            </div>
            <div className='flex gap-32 items-center'>
                <div id='optionsdiv' className='text-[#444242]'>
                  {Role === 'student' && 
                    <div className='flex gap-10 text-[20px] '>
                      <p>
                      <Link href='/dashboard/upcoming'>Upcoming</Link>
                      </p>
                      <div className=' bg-black h-8 w-[1px]'></div>
                      <p>
                      <Link href='/dashboard/previous'>Previous</Link>
                      </p>
                      <div className=' bg-black h-8 w-[1px]'></div>
                      <p>
                      <Link href='/dashboard/test'>Test</Link>
                      </p>
                    </div>
                  }
                </div>
                  {Role === 'teacher' && 
                    <div className='flex gap-10 text-[20px] text-[#444242]]'>
                      <div className='flex gap-20'>
                      <div className='relative' onMouseEnter={()=>setTestDropdown(true)} onMouseLeave={()=>setTestDropdown(false)}><button>Test</button>
                      {TestDropdown && 
                        <div className='absolute p-2 border-2 border-[#504c4c] bg-[#ffffff] px-2 py-2 text-[black] font-bold rounded-[4px]  '>
                          <p>
                          <Link onClick={()=>setTestDropdown(false)} href='/dashboard/upcoming'>Upcoming</Link>
                          </p>
                          <p>
                          <Link onClick={()=>setTestDropdown(false)} href='/dashboard/previous'>Previous</Link>
                          </p>
                          <p>
                          <Link onClick={()=>setTestDropdown(false)} href='/dashboard/alltest'>All Test</Link>
                          </p>
                        </div>}
                        </div>
                        <div className=' bg-black h-8 w-[1px]'></div>
                        <div className='relative' onMouseEnter={()=>setManageDropDown(true)} onMouseLeave={()=>setManageDropDown(false)}><button>Manage</button>
                      {ManageDropDown && 
                        <div className='absolute p-2 w-max border-2 border-[#504c4c] bg-[#ffffff] px-2 py-2 text-[black] font-bold rounded-[4px] '>
                          <p>
                          <Link onClick={()=>setManageDropDown(false)} href='/dashboard/addstudent'>Manage Student </Link>
                          </p>
                          <p>
                          <Link onClick={()=>setManageDropDown(false)} href='/dashboard/managetest'>Manage Tests</Link>
                          </p>
                        </div>}
                        </div>
                      </div>
                    </div>
                  }
                <div id='profilediv' className='text-white'>
                    <div className='relative text-[20px]' onMouseEnter={()=>setProfileDropdown(true)} onMouseLeave={()=>setProfileDropdown(false)}>
                      <Image src={dp} alt='dp' width={40} height={40} className='rounded-full'/> 
                    {
                      ProfileDropdown &&
                      <div className='absolute border-2 border-[#504c4c] bg-[#ffffff] px-2 py-2 text-[black] font-bold rounded-[4px] '>
                        <p>
                        <Link onClick={()=>setProfileDropdown(false)} href='/profile'>Profile</Link>
                        </p>
                        <p>
                        <button onClick={()=>handlelogout()}>Logout</button>
                        </p>
                      </div>
                    }
                    </div>
                </div>
            </div>
        </div>
      </nav>
    </div>
  )
}

export default Navbar