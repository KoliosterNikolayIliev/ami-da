import axios from "axios";

const getCharityData = () => {
    return axios.get(`${process.env.REACT_APP_API_BASE_URL}${process.env.REACT_APP_API_CHARITY}`)
}

export default getCharityData;