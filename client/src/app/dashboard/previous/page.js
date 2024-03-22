import React from 'react'
import styles from '../../../css/previous.module.scss'
import Pretestbox from '@/Components/pretestbox'
function page() {
  return (
    <div className={styles.previous+" mt-3 mx-8 rounded-2xl"}>
      <p className={" text-[40px] flex justify-center text-[#767373] text-center  text-stroke-10"}>Previous Test</p>
      <Pretestbox/>
      <Pretestbox/>
      <Pretestbox/>
      </div>
  )
}

export default page