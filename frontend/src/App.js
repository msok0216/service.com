import Login from "./login";
import { useState, useEffect} from "react";
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Register from "./register";
import Dashboard from "./protected/dashboard";
import Navbar from "./protected/navbar";
import ProtectedRoutes from "./protected/ProtectedRoutes";
import Profile from "./protected/profile";
import Post from "./protected/post";
import Connections from "./protected/connections";

function App() {
  const [verified, setVerified] = useState(false);
  const [token, setToken] = useState(null);
  const [username, setUsername] = useState(null);
  const [session, setSession] = useState(false);
  // if (!verified)



  return (
    <div className="App">
      {/* <Login setVerified={setVerified}/> */}
      <Router>
        {localStorage.getItem('authenticated') && <Navbar/>}
        <Routes>
          <Route path="/" element={<Login confirmUsername={setUsername} setSession={setSession} session={session}/>}>
          </Route>
          <Route path="/register" exact element={<Register />}/>
          <Route element={<ProtectedRoutes session={session} setSession={setSession}/>}>
            <Route path={`/dashboard`} exact element={<Dashboard session={session} setSession={setSession}/>}/>
            <Route path={`/profile`} exact element={<Profile session={session} setSession={setSession}/>}/>
            <Route path={`/post`} exact element={<Post session={session} setSession={setSession}/>}/>
            <Route path={`/connections`} exact element={<Connections session={session} setSession={setSession}/>}/>
          </Route>
        </Routes>
      </Router>
    </div>
  );
  // else return (<Home/>);
 
}


export default App;
