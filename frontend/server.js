/* eslint-disable no-console */
const express = require("express");
const next = require("next");
const { createProxyMiddleware } = require("http-proxy-middleware");

const devProxy = {
  "/api": {
    target: "http://localhost:5000",
    changeOrigin: true,
  },
};
const port = parseInt(process.env.PORT, 10) || 3000;
const env = process.env.NODE_ENV;
const dev = env !== "production";
const app = next({
  dir: ".",
  dev,
});
const handle = app.getRequestHandler();
let server;
app
  .prepare()
  .then(() => {
    server = express();
    if (dev && devProxy) {
      Object.keys(devProxy).forEach((context) => {
        server.use(createProxyMiddleware(context, devProxy[context]));
      });
    }
    server.all("*", (req, res) => handle(req, res));
    server.listen(port, (err) => {
      if (err) {
        throw err;
      }
      console.log(`Ready on port ${port} [${env}]`);
    });
  })
  .catch((err) => {
    console.log("An error occurred, unable to start the server");
    console.log(err);
  });
