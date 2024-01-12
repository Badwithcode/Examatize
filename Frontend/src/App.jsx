import { useState } from "react";
import { UpcomingTest, PreviousTest, Profile } from "./pages/Index";

import {RouterProvider,Route,Link} from "react-router-dom";
import { router } from "./router/index";

function App() {
  return (
    <>
      <RouterProvider router={router}/>
    </>
  );
}

export default App;
