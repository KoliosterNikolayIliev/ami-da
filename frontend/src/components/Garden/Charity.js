import React, {useContext, useEffect, useState} from "react";
import {AppContext} from "../../context/AppContext";
import YouTubeIframeComponent from "../YouTubeIframe";
import "./Charity.css"; // Import the CSS file

function Charity() {
    const {language} = React.useContext(AppContext);
    const {charityData} = useContext(AppContext);
    const [dataIsLoaded, setDataIsLoaded] = useState(false);

    useEffect(() => {
        if (charityData.length > 0) {
            setDataIsLoaded(true);
        }else{
            setDataIsLoaded(false);
        }

    }, [charityData.length]);

    const parser = dataIsLoaded ? new DOMParser():undefined;
    const doc = dataIsLoaded ? parser.parseFromString(charityData[0].embedded_video, 'text/html'):undefined;
    const iframeElement = dataIsLoaded ? doc.getElementsByTagName('iframe')[0] : undefined;

    return (
        dataIsLoaded ? (<div className={'base_container'} style={{display: "block"}}>
            <h2>{language === 'en' ? charityData[0].heading_en : charityData[0].heading_bg}</h2>
            <p>
                {language === 'en' ? charityData[0].main_text_en : charityData[0].main_text_bg}
            </p>
            <h3>{language === 'en' ? charityData[0].payment_heading_en : charityData[0].payment_heading_bg}</h3>
            <div className="aligned-left">
                {(
                    language === 'en'
                        ? charityData[0].payment_info_en
                        : charityData[0].payment_info_bg
                )
                    .split(', ') // Split the text into an array based on ', '
                    .map((line, index) => (
                        <div key={index}>{line}</div> // Render each part in its own <div>
                    ))}
            </div>
            <img src={charityData[0].picture} className={'charity-image'} alt="charity"></img>
            <div className="video-container-charity">
                <div style={{
                    height: '100%',
                    width: '80%',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    flexWrap: 'wrap'
                }}>
                    <YouTubeIframeComponent
                        style={{height: '100%'}}
                        width={'100%'}
                        height={'100%'}
                        src={iframeElement.src}
                        title={'LIVE'}
                        // allow={iframeObject.allow}
                        allowFullScreen='allowFullScreen'
                    />
                </div>
            </div>
        </div>) : <div className={'base_container'} style={{display: "block"}}></div>
    );
}

export default Charity;