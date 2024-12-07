import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;

// Function to register a user
export const registerUser = async (userData) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/api/register`, userData);
    return response.data; // Return response for further use
  } catch (error) {
    console.error('Error registering user:', error.response || error.message);
    throw error; // Throw error for error handling
  }
};
