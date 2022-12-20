let backendHost;

const hostname = window && window.location && window.location.hostname;

// if (hostname === "localhost") {
//   backendHost = "http://localhost:8080";
// }
backendHost = "http://192.168.2.11";
export const API_BASE_URL = `${backendHost}`;
