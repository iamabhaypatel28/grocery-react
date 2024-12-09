import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;

// register a user
export const registerUser = async (userData) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/api/register`, userData);
    return response.data; 
  } catch (error) {
    console.error('Error registering user:', error.response || error.message);
    throw error; 
  }
};


// login a user
export const loginUser = async (userData) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/api/login`, userData);
    console.log("response11111",response.data);
    return response.data; 
  } catch (error) {
    console.error('Error logging in user:', error.response || error.message);
    throw error; 
  }
};
