'use client'
import Image from 'next/image'  
import styles from '../css/testbox.module.scss'

const Testbox = ({test}) => {
  var currentDate = new Date(test.Strattime);
  
  // Get the day of the month (1-31)
  var dayOfMonth = currentDate.getDate();
  
  // Get the month name with three letters
  var monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
  var monthIndex = currentDate.getMonth();
  var month = monthNames[monthIndex];
  return (
        <div className={styles.testbox+" border-[.7px] mx-4 my-5  w-260px min-w-[260px] max-w-[260px] border-[#fefefe] rounded-[20px]  h-[298px] relative overflow-hidden "}>
              <div className= {styles.title+' flex flex-col text-[#ffffff] text-[30px] font-bold absolute top-[60%] left-[3%] mix-blend-'}>{test.name} <br/> {test.subject}
              <span className={' text-[#ffffff] font-bold text-[15px]'}>{test.teacher}</span> 
              </div>
              <div className={' absolute text-[#000000] flex flex-col items-center  justify-center  bg-white rounded-[20px] min-w-[67px] max-w-[67px] h-[80px] bottom-[68%] left-[68%]'}>
                <span className={" font-semibold text-[18px]"}>{dayOfMonth}</span>
                <span className={" font-semibold text-[20px] text-[#63b9f7]"}>{month}</span>
              </div>
              <Image src="https://telecomtalk.info/wp-content/uploads/2024/02/satellite-communications-top-use-cases-in-india.jpg" width={100} height={100} alt="math" className=" w-full h-full object-cover" />
        </div>
  )}
export default Testbox