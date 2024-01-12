import { createBrowserRouter } from "react-router-dom";
import {Dashboard,UpcomingTest,PreviousTest} from "../pages/Index"

const router = createBrowserRouter([
    {
      path:"/",
      element:<Dashboard/>
    },
    {
      path:"/upcomingtest",
      element:<UpcomingTest/>
    },
    {
      path:"/previoustest",
      element:<PreviousTest/>
    },
])
export {router}