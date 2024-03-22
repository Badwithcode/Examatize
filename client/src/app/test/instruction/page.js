import React from 'react'
import styles from "../../../css/dashboard.module.scss";
const instruction = () => {
  return (
    <div className={styles.dashboard+" h-[100vh]"}>
      <div className='text-center text-[40px] pt-[10px]  '>Test Title</div>
      <div className='h-[90%] w-[80%] bg-white mx-[10%] rounded-[50px] '>
        <div className='flex flex-row w-[100%] h-full'>

        <div className=' border-black border-2  ml-[50px] mt-[1%] w-[70%]'>
          
          <div className='text-red-500 text-3xl'>Please Read the instructiom</div>
          <div>
              <div className='text-3xl'>Instruction</div>
              <p>
                1.lremfdxfdgchjk dxrcfghjk cfghjk<br></br>
                1.lremfdxfdgchjk dxrcfghjk cfghjk<br></br>
                1.lremfdxfdgchjk dxrcfghjk cfghjk<br></br>
                1.lremfdxfdgchjk dxrcfghjk cfghjk<br></br>
                1.lremfdxfdgchjk dxrcfghjk cfghjk<br></br>
                1.lremfdxfdgchjk dxrcfghjk cfghjk<br></br>
                1.lremfdxfdgchjk dxrcfghjk cfghjk<br></br>
                1.lremfdxfdgchjk dxrcfghjk cfghjk<br></br>
                

              </p>
        </div>

        <div className='mt-[10px]'>
          <div className='text-3xl'>Test Details</div>
          <p>
            Time:1hr<br></br>
            Timing 9:00 to 10:00<br></br>
            No of questions<br></br>
            marks alloted<br></br>
            

          </p>

          </div>
        </div>
        

        
        <div className='border-black border-2  w-[50%] bg-[#B1B9C4] mr-[50px] mt-[1%]'>r</div>
        </div>
      </div>

    </div>
  )
}

export default instruction
