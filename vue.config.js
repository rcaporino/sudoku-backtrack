module.exports = {
    devServer: {
      overlay: false,
    },
    configureWebpack: {
      module: {
        rules: [
          {
            test: /\.(pdf)(\?.*)?$/,
            use: [
              {
                loader: 'url-loader',
                options: {
                  name: 'files/[name].[hash:8].[ext]'
                }
              }
            ]
          }
        ]
      }
    }
  }