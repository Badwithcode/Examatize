import React, { useState } from "react";

const UploadFile = () => {
  const [file, setFile] = useState();

  const handleChange = (event) => {
    event.preventDefault();
    setFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (!file) {
      console.log("No file selected");
      return;
    }

    const formData = new FormData();
    formData.append('details', file);

    try {
      const response = await fetch("/api/addstudent", {
        method: "POST",
        body: formData,
        headers:{
          'Authorization':`Bearer ${localStorage.getItem('token')}`
        }
      });
      if (response.ok) {
        console.log("File uploaded successfully");
      } else {
        console.log("Failed to upload file");
      }
    } catch (error) {
      console.error("Error uploading file:", error);
      console.log("Failed to upload file");
    }
  };

  return (
    <div className="mx-40">
      <div className="bg-blue-100 mx-40 my-10 px-40 py-20 border-black border-1 rounded-3xl">
        <div>Drop file here</div>
        <div className="App">
          <form onSubmit={handleSubmit}>
            <h1>React File Upload</h1>
            <input type="file" onChange={handleChange} />
            <button
              type="submit"
              className="bg-blue-500 h-10 hover:bg-blue-400 text-white font-bold py-2 px-4 rounded-full"
            >
              Upload
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default UploadFile;
