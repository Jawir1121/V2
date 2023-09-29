// Import modul-modul yang diperlukan
const http = require('http');
const https = require('https');
const fs = require('fs');
const url = require('url');

// Argumen dari baris perintah
const args = process.argv.slice(2);

// Fungsi untuk melakukan permintaan HTTP/HTTPS
function makeRequest(targetUrl, proxyListFile, mode) {
  try {
    // Membaca daftar proxy dari file
    const proxies = fs.readFileSync(proxyListFile, 'utf-8').split('\n').filter(Boolean);

    // Membaca target URL
    const parsedUrl = url.parse(targetUrl);

    // Pilih salah satu proxy secara acak
    const randomProxy = proxies[Math.floor(Math.random() * proxies.length)];
    const proxyParts = randomProxy.split(':');

    const proxyHostname = proxyParts[0];
    const proxyPort = parseInt(proxyParts[1], 10);

    // Konfigurasi permintaan HTTP/HTTPS
    const options = {
      hostname: proxyHostname,
      port: proxyPort,
      path: parsedUrl.path,
      method: 'GET',
      headers: {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.91 Mobile Safari/537.36' // Ganti dengan User-Agent yang Anda inginkan
      }
    };

    const client = mode === 'https' ? https : http;
    const req = client.request(options, (res) => {
      res.setEncoding('utf8');
      res.on('data', (chunk) => {
        console.log(chunk);
      });
    });

    req.on('error', (err) => {
      console.error('Request error:', err);
    });

    req.end();
  } catch (err) {
    console.error('Error:', err);
  }
}

// Menangani argumen dari baris perintah
const argsMap = {};
for (let i = 0; i < args.length; i++) {
  const argParts = args[i].split('=');
  if (argParts.length === 2) {
    argsMap[argParts[0].trim()] = argParts[1].trim();
  }
}

const targetUrl = argsMap['--target'];
const proxyListFile = argsMap['--proxy'];
const mode = argsMap['--mode'];

if (!targetUrl) {
  console.error('Target URL is missing. Usage: node HTTP-BROWSER.js --target=<URL>');
} else if (!proxyListFile) {
  console.error('Proxy list file is missing. Usage: node HTTP-BROWSER.js --proxy=<proxy_list_file>');
} else {
  makeRequest(targetUrl, proxyListFile, mode);
}
