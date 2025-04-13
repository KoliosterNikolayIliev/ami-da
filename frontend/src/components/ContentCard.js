import React, {useState} from 'react';
import Card from 'react-bootstrap/Card';
import Modal from 'react-bootstrap/Modal';
import {AppContext} from "../context/AppContext";
import YouTubeIframeComponent from "./YouTubeIframe";
import TextWithLinks from "./TextWithLinks";


function ContentCard({item, aspect_ratio='normal', description, playName, playNameBg, descriptionBg, content, dateBg, dateUs}) {
    const {language} = React.useContext(AppContext);
    const [isLoading, setIsLoading] = useState(true);
    //content==='images'?true:false
    const [showModal, setShowModal] = useState(false);
    //"""<iframe width="560" height="315" src="https://www.youtube.com/embed/Mau7HEoGmTU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>"""
    const iframeObject = {};
    if (content === 'videos') {
        const parser = new DOMParser();
        const doc = parser.parseFromString(item, 'text/html');
        const iframeElement = doc.getElementsByTagName('iframe')[0];


        for (let i = 0; i < iframeElement.attributes.length; i++) {
            const {name, value} = iframeElement.attributes[i];
            // Set width and height to "100%" if found
            iframeObject[name] = (name === 'width' || name === 'height') ? '100%' : value;
        }
    }

    const handleItemLoad = () => {
        setIsLoading(false);
    };

    const handleModalClose = () => {
        setShowModal(false);
    };

    const handleModalShow = () => {
        setShowModal(true);
    };
    console.log(item)
    return (
        <>
            <Card style={{border: content === 'projects' && 'none'}}>
                <div style={{position: 'relative'}}>
                    {isLoading && (
                        <div className="custom_spinner_container">
                            <div className="custom_spinner"></div>
                        </div>
                    )}
                    {content === 'images' || content === 'projects' ? <Card.Img
                            variant="top"
                            src={item}
                            className="custom_img_card_img"
                            style={{
                                opacity: isLoading ? 0 : 1,
                                cursor: content === 'images' ? 'pointer' : 'auto',
                                width: content === 'projects' ? '60%' : '100%',
                                height: content === 'projects' && '100%',
                                objectPosition: aspect_ratio ==='portrait'?'top' : 'center',
                            }}
                            onLoad={handleItemLoad}
                            onClick={handleModalShow}
                        /> :
                        <YouTubeIframeComponent
                            handleItemLoad={handleItemLoad}
                            width={iframeObject.width}
                            height={iframeObject.height}
                            src={iframeObject.src}
                            title={iframeObject.title}
                            allow={iframeObject.allow}
                            allowFullScreen='allowFullScreen'
                        />
                    }
                </div>
                <Card.Body>
                    <Card.Title>{language === 'en' ? playName : playNameBg}</Card.Title>
                    <Card.Text className='text-start'>
                        {language === 'en' ? <TextWithLinks text={description}/> :
                            <TextWithLinks text={descriptionBg}/>}
                    </Card.Text>
                </Card.Body>
                {content === "projects" &&
                    <Card.Footer>
                        <small
                            className="text-muted">{language === 'en' ? 'Performance date: ' : 'Следващо представление: '}</small>
                        <small className="text-muted">{language === 'en' ? dateUs : dateBg}</small>
                    </Card.Footer>
                }
            </Card>
            {content === "images" &&
                <Modal style={{cursor: 'pointer'}} show={showModal} onHide={handleModalClose} onClick={handleModalClose}
                       size="lg">

                    <Modal.Body>
                        <img
                            src={item}
                            alt="Full size"
                            className="custom_modal_img"
                            style={{maxWidth: '100%', maxHeight: '100%'}}
                        />
                    </Modal.Body>
                </Modal>
            }
        </>
    );
}

export default ContentCard;