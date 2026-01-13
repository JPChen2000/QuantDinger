const path = require('path')
const webpack = require('webpack')
const packageJson = require('./package.json')

// ========== git-revision-webpack-plugin兼容性处理 ==========
let GitRevision
try {
  const GitRevisionPlugin = require('git-revision-webpack-plugin')
  // 处理ES模块和CommonJS的差异
  const PluginClass = GitRevisionPlugin.default || GitRevisionPlugin
  GitRevision = new PluginClass()
} catch (e) {
  console.warn('git-revision-webpack-plugin not found, using fallback')
  GitRevision = {
    version: () => 'dev',
    commithash: () => 'unknown',
    branch: () => 'unknown'
  }
}

const buildDate = JSON.stringify(new Date().toLocaleString())

// ========== theme-color-replacer安全加载 ==========
function getThemeColorReplacerPlugin() {
  try {
    const createThemeColorReplacerPlugin = require('./config/plugin.config')
    return createThemeColorReplacerPlugin()
  } catch (e) {
    console.warn('ThemeColorReplacer plugin failed to load:', e.message)
    return { apply: () => {} }
  }
}

function resolve(dir) {
  return path.join(__dirname, dir)
}

function getGitHash() {
  try {
    return GitRevision.version()
  } catch (e) {
    return 'unknown'
  }
}

// ========== vue.config.js配置 ==========
const vueConfig = {
  configureWebpack: {
    plugins: [
      new webpack.IgnorePlugin({
        resourceRegExp: /^\.\/locale$/,
        contextRegExp: /moment$/
      }),
      new webpack.DefinePlugin({
        APP_VERSION: `"${packageJson.version}"`,
        GIT_HASH: JSON.stringify(getGitHash()),
        BUILD_DATE: buildDate
      })
    ]
  },

  chainWebpack: config => {
    config.resolve.alias.set('@$', resolve('src'))

    // SVG loader配置
    const svgRule = config.module.rule('svg')
    config.module.rules.delete('svg')

    config.module.rule('svg')
      .oneOf('svg_as_component')
      .resourceQuery(/inline/)
      .test(/\.(svg)(\?.*)?$/)
      .use('babel-loader')
      .loader('babel-loader')
      .end()
      .use('vue-svg-loader')
      .loader('vue-svg-loader')
      .options({
        svgo: {
          plugins: [
            { prefixIds: true },
            { cleanupIDs: true },
            { convertShapeToPath: false },
            { convertStyleToAttrs: true }
          ]
        }
      })
      .end()
      .end()
      .oneOf('svg_as_regular')
      .merge(svgRule.toConfig())
      .end()
  },

  // ========== CSS配置 ==========
  css: {
    loaderOptions: {
      less: {
        modifyVars: {
          'border-radius-base': '2px'
        },
        javascriptEnabled: true
      }
    }
  },

  devServer: {
    port: 8000,
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
        ws: true,
        changeOrigin: true
      }
    }
  },

  productionSourceMap: false,
  lintOnSave: false,
  transpileDependencies: ['ant-design-vue', '@ant-design-vue']
}

// 安全添加ThemeColorReplacer插件
const themePlugin = getThemeColorReplacerPlugin()
if (themePlugin && themePlugin.apply) {
  vueConfig.configureWebpack.plugins.push(themePlugin)
}

// 设置Node.js兼容性选项
process.env.NODE_OPTIONS = process.env.NODE_OPTIONS || '--openssl-legacy-provider'

module.exports = vueConfig
