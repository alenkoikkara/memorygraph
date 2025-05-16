import axios from 'axios';
import { loadEnv } from 'vite';

const env = loadEnv(import.meta.env.MODE, process.cwd(), "");

const apiService = axios.create({
  baseURL: env.VITE_BACKEND_BASE_URL,
});

export default apiService;


export const getSearchResults = async (query: string) => {
  console.log(env.VITE_BACKEND_BASE_URL);
  const response = await apiService.get(`/search?query=${query}`);
  return response.data;
};


