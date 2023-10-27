export const config = {headers: {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*'
  }}

export const tokenConfig = (token) => {
  return {
    headers:{
      ...config.headers,
      'Authorization': `Bearer: ${token}`
    }
  }
}