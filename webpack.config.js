const path = require('path')
const webpack = require('webpack')

module.exports = {
  entry: [
    './static/billing/src/js/app.js',
    './static/billing/src/css/app.scss'
  ],
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'static/billing/dist'),
  },
  module:{
    rules:[
      {
        enforce: 'pre',
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'jshint-loader'
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
      },
      {
        test: /\.scss$/,
        use: [
          {
            loader: 'style-loader',
          },
          {
            loader: 'css-loader',
          },
          {
            loader: 'sass-loader',
          },
        ],
      },
    ]
  },
};
