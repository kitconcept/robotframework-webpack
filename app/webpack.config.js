const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: './app.js',
  output: {
     path: './dist',
     filename: 'app.bundle.js'
  },
  plugins: [new HtmlWebpackPlugin()],
 };
