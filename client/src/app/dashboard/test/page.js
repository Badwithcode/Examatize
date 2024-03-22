'use client'
import React, { useEffect, useState } from 'react'

const Testpage = () => {
  const [questions, setQuestions] = useState([]);
  const [selectedAnswers, setSelectedAnswers] = useState({});
  useEffect(() => {
    fetchQuestions();
  }, []);

  const fetchQuestions = async () => {
    const response = await fetch('');
    const data = await response.json();
    setQuestions({
      "questions": [
          {
              "difficulty": "Easy",
              "id": 1,
              "options": [
                  "name1",
                  "name2",
                  "name3",
                  "name4"
              ],
              "question": "what is you name",
              "tags": "gchvj"
          },
          {
              "difficulty": "Easy",
              "id": 2,
              "options": [
                  "name1",
                  "name2",
                  "name3",
                  "name4"
              ],
              "question": "what is you name",
              "tags": "hgvj"
          },
          {
              "difficulty": "Medium",
              "id": 3,
              "options": [
                  "name1",
                  "name2",
                  "name3",
                  "name4"
              ],
              "question": "what is you name",
              "tags": "jbh"
          },
          {
              "difficulty": "Hard",
              "id": 4,
              "options": [
                  "name1",
                  "name2",
                  "name3",
                  "name4"
              ],
              "question": "what is you name",
              "tags": "gv"
          }
      ],
      "status": true
  });
  };
  


  return (
    <>
        <div>testpage</div>
        <button>Start test</button>
        
    </>
  )
}

export default Testpage