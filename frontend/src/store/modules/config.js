export const config = {headers: {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*'
  }}

export const tokenConfig = { headers: {
  'Content-Type': 'application/json',
  'Access-Control-Allow-Origin': '*',
  'Authorization': `Bearer: ${jwt}`
  }
}