const https = require('https');

module.exports = async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  const apiKey = process.env.CRICAPI_KEY;

  if (!apiKey) {
    return res.status(500).json({ error: 'CRICAPI_KEY not set in Vercel environment variables' });
  }

  const url = `https://api.cricapi.com/v1/currentMatches?apikey=${apiKey}&offset=0`;

  return new Promise((resolve) => {
    https.get(url, (apiRes) => {
      let data = '';
      apiRes.on('data', chunk => data += chunk);
      apiRes.on('end', () => {
        try {
          const json = JSON.parse(data);
          res.status(200).json(json);
        } catch (e) {
          res.status(500).json({ error: 'Failed to parse CricAPI response' });
        }
        resolve();
      });
    }).on('error', (err) => {
      res.status(500).json({ error: 'Failed to reach CricAPI: ' + err.message });
      resolve();
    });
  });
};
