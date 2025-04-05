import axios from "axios";

const API_BASE_URL = import.meta.env.VITE_API_URL;
const ENDPOINTS = {
  OPERADORAS: "operadoras/",
};

export const getOperadoras = async () => {
  const response = await axios.get(`${API_BASE_URL}${ENDPOINTS.OPERADORAS}`);  
  return response.data;
};

export const getFields = async () => {
  const response = await axios.get(`${API_BASE_URL}${ENDPOINTS.OPERADORAS}/fields`);
  return response.data;
};
