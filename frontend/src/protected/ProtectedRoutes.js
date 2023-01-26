import Dashboard from "./dashboard";
import Login from "../login";
import {Navigate, Outlet} from 'react-router-dom';
import { useState } from "react";


const useAuth =  () => {
    // const user = (async () => {
    //     const token  = localStorage.getItem('token');
    //     // const username = localStorage.getItem('username');
    //     let verified = false;
    //     // console.log(token);
    //     const request = {
    //       method: 'PUT',
    //       headers: {"Content-Type": "application/json; charset=utf-8"},
    //       body: JSON.stringify({
    //         "token": token,
    //         // "username": username
    //       })
    //     };
    //     await fetch(`/user/authenticate`, request).then(response =>{
    //         if (response.status === 200) verified = true;
    //         // return response.json();
    //     });
    //     console.log('verified: ' + verified);
    //   return verified;

    // });
    // // return true;
    // console.log('yeeyee');
    // return user() && localStorage.getItem('authenticated');

    const authenticated = localStorage.getItem('authenticated');
    // console.log(authenticated);
    return authenticated;
}

const ProtectedRoutes = ({verified}) => {
    // const isAuth = useAuth();
    // console.log(localStorage.getItem('token'));
    return useAuth() ? <Outlet /> : <Navigate to='/'/>
}

export default ProtectedRoutes;
