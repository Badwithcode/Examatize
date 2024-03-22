import React from 'react'
import Image from 'next/image'

const Pretestbox = () => {
  return (
    <div className='bg-slate-100 bg-opacity-85 m-3 rounded-xl overflow-hidden'>
    <div className=' flex flex-row p-3'>
        <Image className="rounded-xl" src="https://media.licdn.com/dms/image/D5612AQH2dxUXGbxw4w/article-cover_image-shrink_720_1280/0/1695723783211?e=2147483647&v=beta&t=1GWrSfifYglJOGGNdCmy6heUbJtLncMgfFFWM2Gb7os" alt="test" width={260} height={350} />
        <div className='m-2 w-full flex flex-col bg-white p-6 rounded-xl'>
            <div className='flex flex-row justify-between '>
                <div>
                    <span className=" text-2xl text-[#3988e8] font-semibold ">Test Name: </span>
                    <span>CIA 1</span>
                </div>
                <div>
                    <span className=" text-2xl text-[#3988e8] font-semibold ">Subject: </span>
                    <span>Embedded & IOT</span>
                </div>
                <div>
                    <span className=" text-2xl text-[#3988e8] font-semibold ">Subject Code: </span>
                    <span>U19EC202</span>
                </div>
                <div>
                    <span className=" text-2xl text-[#3988e8] font-semibold ">Teacher: </span>
                    <span>Govindha Govinda</span>
                </div>
            </div>
            <div>
            <span className=" text-2xl text-[#3988e8] font-semibold ">Test Date: </span>
            <span>12-10-2021</span>
            </div>
            <div>
            <span className=" text-2xl text-[#3988e8] font-semibold">Start Time: </span>
            <span>2.00 am</span>
            </div>
            <div>
            <span className=" text-2xl text-[#3988e8] font-semibold">End Time: </span>
            <span>4.00 am</span>
            </div>
            <div>
            <span className=" text-2xl text-[#3988e8] font-semibold">Status: </span>
            <span>Attended</span>
            </div>
            <div>
            <span className=" text-2xl text-[#3988e8] font-semibold">Time Taken: </span>
            <span>2 hrs 3 min 12 sec</span>
            </div>
            <div>
            <span className=" text-2xl text-[#3988e8] font-semibold">Score: </span>
            <span>10/10</span>
            </div>
        </div>
    </div>
    </div>
  )
}

export default Pretestbox