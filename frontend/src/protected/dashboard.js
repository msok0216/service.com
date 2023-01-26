import Navbar from "./navbar";
import './dashboard.css';
import {useEffect, useState} from 'react';
import {InputGroup, Form, Button} from 'react-bootstrap';
import {Link, Navigate, BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import project_data from './project_data.json';
import ProjectModal from "./projectModal";
// import './App.css';
// import login from 

// const getProjects = (query, projects) => {
//   if (!query) {
//     return projects;
//   }
//   return projects.filter(project => project.name.includes(query));
// }



function Dashboard({username}) {
  const [query, setQuery] = useState('');
  const [data, setData] = useState([]);
  const [modalData, setModal] = useState(null);
  const [showModal, setShowModal] = useState(false);
  const projects = 'yeeyee';
  // const filteredProjects = getProjects(query, projects);

  async function handleInput(e) {
    e.preventDefault();
    setQuery(e.target.value);
    // console.log(modalData);
  }

  useEffect (() => {
    if (query.length > 0) {
      console.log(query);
      let temp = data.filter((project) => {
        return project.name.match(query);
      });

      setData(temp);
  
    }
  }, [query])
  

  function handleModalData(content) {
    setModal(content.content);
    setShowModal(true);

  }


  async function load() {
    setData(project_data);

  
  }
//name location manager description hours

  if (localStorage.getItem('authenticated') && localStorage.getItem('token'))
    return (
      <div>
        {/* <Navbar username={username}/> */}
        <div className="content">
          <div className="searchbar">
            <InputGroup className="search">
              <Form.Control className="search-projects" placeholder="Search for Projects" onChange={handleInput}/>
            </InputGroup>
          </div>
          <hr className="search-separator"/>
          <br/>
          <div className="dashboard-post-container">
            {
              data.map(content => <div key={content.name}  className="dashboard-post" >
                <h5>{content.name}</h5>
                <hr/>
                <div className="dashboard-post-content">
          
                  {content.date} {content.manager}
                  <div className="dashboard-post-description">
                    {/* <textarea rows="5" cols="45"> */}
                    {content.description}
                    {/* </textarea> */}
                  
                  </div>
                </div>
                <span className='project-more'><Button onClick={() => {handleModalData({content});}}>More</Button> <Button>SignUp</Button></span>
                {/* <span className="project-signup"><Button>SignUp</Button></span> */}

              </div>)
            }

            
            {/* {modalData.name} */}
          </div>
          <Button onClick={load}>Click</Button>
        </div>
        {showModal  && <ProjectModal content={modalData} setModal={setModal} setShowModal={setShowModal} showModal={showModal}/>}
      </div>
    );
  else {
    return <div><Navigate to='/'/></div>;
  }
 
 
}


export default Dashboard;
