import ContentCard from "./ContentCard";
import noImage from '../public/no_image.png'
import LogoLoader from './LogoLoader'
import {Container, Row, Col} from 'react-bootstrap';
import {useContext, useEffect, useState} from "react";
import {AppContext} from "../context/AppContext";
import axios from "axios";

function Gallery({content}) {
    const [err, setErr] = useState(false);
    const {images, setImages} = useContext(AppContext);
    const {videos, setVideos} = useContext(AppContext);
    const {plays, setPlays} = useContext(AppContext);
    const baseUrl = `${process.env.REACT_APP_API_BASE_URL}`
    const paths = {
        'images': `${process.env.REACT_APP_API_IMAGES}`,
        'videos': `${process.env.REACT_APP_API_VIDEOS}`,
        'projects': `${process.env.REACT_APP_API_PROJECTS}`
    }
    // const endpoint = '/api/plays'
    const endpoint = paths[content]
    useEffect(() => {
        function assembleUrls(plays) {
            let projects = plays;
            projects = projects.map((play) => {
                if (play.poster_url !== "no_image") {
                    return {
                        ...play,
                        poster_url: baseUrl + play.poster_url
                    };
                }
                return play; // If poster_url is "no_image", don't change it
            });
            return projects;
        }

        if (
            (content === 'images' && !images) ||
            (content === 'videos' && !videos) ||
            (content === 'projects' && !plays)
        ) {

            axios.get(baseUrl + endpoint)
                .then(response => {
                    if (content === 'images') {
                        setImages(response.data)
                    } else if (content === 'videos') {
                        setVideos(response.data)
                    } else if (content === 'projects') {
                        setPlays(assembleUrls(response.data))
                    }
                })
                .catch(error => setErr(true));
        }
    }, [setImages, setVideos, endpoint, content, images, plays, setPlays, videos, baseUrl]);

    if (err) {
        console.log(err)
        return <div className={'inner_main_container'}>
            <LogoLoader/>
        </div>;
    }
    const _items = {
        'images': images,
        'videos': videos,
        'projects': plays
    }
    const items = _items[content]
    if (items === null) {
        return (
            <div className={'inner_main_container'}>
                <LogoLoader/>
            </div>
        );
    }
    let itemsWithFullUrl = items
    if (content === 'images') {
        itemsWithFullUrl = items.map(
            (image) => ({
                ...image,
                image_field_url: baseUrl + image.image_field_url
            }));
    }


    itemsWithFullUrl.sort((a, b) => {
        const playNameA = a.play_name.toLowerCase();
        const playNameB = b.play_name.toLowerCase();

        if (playNameA < playNameB) {
            return -1;
        }
        if (playNameA > playNameB) {
            return 1;
        }
        return 0;
    });

    return (
        <div className={'base_container'}>
            <Container>
                <Row>
                    {itemsWithFullUrl.map(item => (
                        <Col key={item.id} xs={12} sm={6} md={content==='images'|| content==='videos'?3:6} style={{marginBottom: '1.5rem'}}>
                            <ContentCard
                                key={item.id}
                                item={content === 'images' ? item.image_field_url :
                                    (content === 'projects' ? (item.poster_url !== 'no_image' ? item.poster_url : noImage) : item.embedded_video)}
                                description={item.description}
                                playName={item.play_name}
                                playNameBg={item.play_name_bg}
                                descriptionBg={item.description_bg}
                                content={content}
                                dateBg={new Date(item.next_play).toLocaleString('bg-BG', {day: '2-digit',month: '2-digit', year: 'numeric',  hour: '2-digit', minute: '2-digit', hour12: false })}
                                dateUs={new Date(item.next_play).toLocaleString('en-US', {day: '2-digit',month: '2-digit', year: 'numeric',  hour: '2-digit', minute: '2-digit', hour12: false })}
                            />
                        </Col>
                    ))}
                </Row>
            </Container>
        </div>
    );
}

export default Gallery;
