var debug = process.env.NODE_ENV !== "production"
var webpack = require('webpack')

module.exports = {
  context: __dirname + "/static/dist",
  // devtool: debug ? "inline-sourcemap" : "#source-map",
  devtool: debug ? "inline-sourcemap" : false,
  entry: {
    index: ["babel-polyfill", __dirname + "/static/dist/js/index.js"],
  },
  output: {
    path:__dirname + "/static/dist/prod",
    filename: "[name].js",
    // sourceMapFilename: "bundle.map"
  },
  module: {
    loaders: [
      {
        test: /\.js?$/,
        exclude: /(node_modules|bower_components)/,
        loader: "babel-loader",
        query: {
          presets: ["es2015", "stage-0"],
          // plugins: ["transform-class-properties", "transform-decorators-legacy"]
        }
      }
    ]
  },
  plugins: debug ? [] : [
    new webpack.optimize.OccurrenceOrderPlugin(),
    new webpack.optimize.UglifyJsPlugin({ mangle: false, sourcemap: false }),
    // new webpack.optimize.UglifyJsPlugin({ mangle: false, sourcemap: true }),
  ],
};
