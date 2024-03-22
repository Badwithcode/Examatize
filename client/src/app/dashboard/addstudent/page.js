"use client";
import UploadFile from "@/Components/UploadFile";
import { useRouter } from "next/navigation";
import React, { useEffect, useState } from "react";

const Page = () => {
  const route = useRouter();
  const [Role, setRole] = useState("");
  const [IsLoading, setIsLoading] = useState(true);

  useEffect(() => {
    fetchdata();
  }, []);

  async function fetchdata() {
    const resp = await fetch("/api/token", {
      method: "GET",
      headers: {
        Authorization: "Bearer " + localStorage.getItem("token"),
      },
    });
    const response = await resp.json();
    setIsLoading(false);
    if (response.role === "teacher") {
      setRole(response.role);
    } else {
      route.push("/dashboard/upcoming");
    }
  }

  async function getTemplate() {
    const resp = await fetch("/api/downloadtemplate", {
      method: "GET",
      headers: {
        Authorization: "Bearer " + localStorage.getItem("token"),
      },
    });
    const blob = await resp.blob();
    const url = window.URL.createObjectURL(blob);
    const link = document.createElement("AddStudentTemplate");
    link.href = url;
    link.download = "AddStudentTemplate.xlsx";
    link.click();
  }

  if (IsLoading) {
    return <div>Loading...</div>;
  }
  if (!IsLoading) {
    return (
      <>
        <div className="">
        <div className="flex justify-center mt-8">
          <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full" onClick={getTemplate}>
          
          Download Template
          </button>
        </div>
        
        <div className="">
          <UploadFile/>
        </div>
        </div>
      </>
    );
  }
};

export default Page;
