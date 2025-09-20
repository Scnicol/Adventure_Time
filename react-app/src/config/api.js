// API Configuration utility
const getApiBaseUrl = () => {
  // For mobile apps, we need to use the full URL instead of relative paths
  const baseUrl = process.env.REACT_APP_API_BASE_URL;

  if (baseUrl) {
    return baseUrl;
  }

  // Fallback for development
  return 'http://localhost:5000';
};

export const API_BASE_URL = getApiBaseUrl();

// Helper function to build full API URLs
export const buildApiUrl = (endpoint) => {
  const baseUrl = API_BASE_URL;
  const cleanEndpoint = endpoint.startsWith('/') ? endpoint : `/${endpoint}`;
  return `${baseUrl}${cleanEndpoint}`;
};

// Environment info
export const isDevelopment = process.env.REACT_APP_ENVIRONMENT === 'development';
export const isProduction = process.env.REACT_APP_ENVIRONMENT === 'production';
