import './App.scss';
import {BrowserRouter, Routes, Route} from "react-router-dom";
import {AppProvider} from "./context/AppContext";
import CarouselComponent from "./components/CarouselComponent";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Gallery from "./components/Gallery";
import Contacts from "./components/Conatcts";
import NoPage from "./components/NoPage";
import Live from "./components/Live";
import Charity from "./components/Garden/Charity";


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
                            <Route exact path="/projects" element={<Gallery content={'projects'}/>}/>
                            <Route exact path="/contacts" element={<Contacts/>}/>
                            <Route exact path="/live" element={<Live/>}/>
                            <Route exact path="/charity" element={<Charity/>}/>
                            <Route path="*" element={<NoPage/>}/>
                        </Routes>

                    <Footer/>

                </div>

            </BrowserRouter>
        </AppProvider>

    );
}

export default App;
