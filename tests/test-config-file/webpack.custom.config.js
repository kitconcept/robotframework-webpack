const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: './app.js',
  output: {
     path: './custom',
     filename: 'app.custom.bundle.js'
  },
  plugins: [new HtmlWebpackPlugin()],
 };
