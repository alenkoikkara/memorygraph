import axios from 'axios';

const apiService = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

export default apiService;


export const getSearchResults = async (query: string) => {
  console.log(import.meta.env.VITE_API_URL);
  const response = await apiService.get(`/search?query=${query}`);
  return response.data;
};
