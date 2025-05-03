import axios from 'axios';

const API_URL = 'http://localhost:8001/api';

const apiService = axios.create({
  baseURL: API_URL,
});

export default apiService;


export const getSearchResults = async (query: string) => {
  const response = await apiService.get(`/search?query=${query}`);
  return response.data;
};


