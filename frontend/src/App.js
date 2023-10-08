import './App.scss';
import {BrowserRouter, Routes, Route} from "react-router-dom";
import {AppProvider} from "./context/AppContext";
import CarouselComponent from "./components/CarouselComponent";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Gallery from "./components/Gallery";
import Performances from "./components/Performances";
import Contacts from "./components/Conatcts";
import NoPage from "./components/NoPage";
import Live from "./components/Live";


function App() {
    return (
        <AppProvider>
            <BrowserRouter basename={''}>
                <div className="App">

                    <Header/>

                        <Routes>
                            <Route exact path="/" element={<CarouselComponent/>}/>
                            <Route exact path="/image-gallery" element={<Gallery content={'images'}/>}/>
                            <Route exact path="/video-gallery" element={<Gallery content={'videos'}/>}/>
                            <Route exact path="/projects" element={<Performances/>}/>
                            <Route exact path="/contacts" element={<Contacts/>}/>
                            <Route exact path="/live" element={<Live/>}/>
                            <Route path="*" element={<NoPage/>}/>
                        </Routes>

                    <Footer/>

                </div>

            </BrowserRouter>
        </AppProvider>

    );
}

export default App;
