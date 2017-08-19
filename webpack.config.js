const path = require('path');
const webpack = require('webpack');
const ExtractTextPlugin = require("extract-text-webpack-plugin");

module.exports = {
  entry: {
    app:['./static/billing/src/js/app.js',
      './static/billing/src/css/app.scss',],
  },
  output: {
    filename: '[name].min.js',
    path: path.resolve(__dirname, 'static/billing/dist'),
  },
  module:{
    rules:[
      {
        test: /\.scss$/,
        exclude: /node_modules/,
        use: ExtractTextPlugin.extract([
              {
                loader: 'css-loader?minimize',
              }, // translates CSS into CommonJS modules
              {
                loader: 'postcss-loader', // Run post css actions
                options: {
                  plugins: function () { // post css plugins, can be exported to postcss.config.js
                    return [
                      require('precss'),
                      require('autoprefixer')
                    ];
                  }
                }
              },
              {
                loader: 'sass-loader' // compiles SASS to CSS
              },
          ]),
      },
    ],
  },
  plugins: [
      new ExtractTextPlugin("[name].min.css"),
      new webpack.optimize.UglifyJsPlugin({
        compress: { warnings: false }
      }),
      new webpack.ProvidePlugin({
        $: "jquery",
        jQuery: "jquery",
        "window.jQuery": "jquery",
        'Popper': 'popper.js',
      }),
  ],
  watch: true,
};
