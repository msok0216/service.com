// import React, {useEffect, useRef} from 'react';
import  { Button, Modal, ModalBody, ModalFooter, ModalHeader, ModalTitle } from'react-bootstrap';

// import './index.css';
// const Modal = ({isOpen, toggleModal, closeOnOutsideClick, children}) => {
//     const modalRef = useRef(null);
    
//     useEffect(() => {
//        const handleClickOutside = (event) => {
//             if (closeOnOutsideClick && modalRef.current && !modalRef.current.contains(event.target)) {
//               toggleModal();
//             }
//        }
//        // Bind the event listener
//        document.addEventListener('mousedown', handleClickOutside);
//        return() => {
//              // Unbind the event listener
//              document.removeEventListener('mousedown', handleClickOutside);
//        };
// }, [modalRef, closeOnOutsideClick, toggleModal];
// return (
//     <div className="modal" style={isOpen ? {display: 'none'} : null}>
//        <div className="modal__wrapper" ref={modalRef}>
//            {children}
//        </div>
//     </div>
//   )
// }

function ProjectModal({content, setModal, setShowModal, showModal}) {

    // useEffect = () => {
    //     // console.log(content.name);
    //     console.log(showModal);
    // }

    // if ( return ;
    
    if (showModal)
    return (
        <Modal className='project-modal' show={content != null} size='lg' onHide={() => {setShowModal(false)}}>

                <ModalHeader closeButton>
                    <ModalTitle>{content.name}</ModalTitle>
                </ModalHeader>

                <ModalBody className='project-modal-body'>
                    <p>
                        {/* {JSON.stringify(content)} */}
                        {content.description}
                    </p>

                </ModalBody>

                <ModalFooter>
                    <Button onClick={()=>{setShowModal(false)}}>SignUp</Button>
                    {/* <Button onClick={()=>{setShowModal(false)}}>Close</Button> */}
                </ModalFooter>

        </Modal>
    )
}



export default ProjectModal;