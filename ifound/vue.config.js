module.exports = {
  publicPath:
    process.env.NODE_ENV === "production"
      ? "/"
      : "/",
      
  pwa: {
    name: "iFound",
    shortName: "iFound",
    themeColor: "#5200DC",
    msTileColor: "#57EF53",
    workboxOptions: {
      skipWaiting: true
    }
  }
};