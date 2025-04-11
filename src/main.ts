import https from 'https';
import fs from 'fs';
import path from 'path';
import { WebSocketServer, WebSocket } from 'ws';

// Carrega os certificados SSL
const options = {
  key: fs.readFileSync(path.join(__dirname, 'cert', 'key.pem')),
  cert: fs.readFileSync(path.join(__dirname, 'cert', 'cert.pem')),
};

// Cria servidor HTTPS
const server = https.createServer(options, (req: any, res) => {
  // Serve o HTML da pasta 'public'
  let filePath = path.join(__dirname, 'public', req.url === '/' ? 'index.html' : req.url);

  fs.readFile(filePath, (err, content) => {
    if (err) {
      res.writeHead(404);
      res.end('Arquivo não encontrado');
      return;
    }

    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(content);
  });
});

// Cria servidor WebSocket seguro
const wss = new WebSocketServer({ server });

wss.on('connection', (ws: WebSocket) => {
  console.log('Cliente WebSocket conectado.');

  ws.on('message', (data) => {
    console.log('Dados recebidos:', data.toString());
  });

  ws.on('close', () => {
    console.log('Cliente desconectado.');
  });
});

// Inicia o servidor na porta 4000
const PORT = 4000;
server.listen(PORT, () => {
  console.log(`Servidor rodando em https://localhost:${PORT}`);
});
