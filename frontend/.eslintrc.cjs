module.exports = {
  extends: ["plugin:vue/vue3-recommended", "prettier"],
  parser: "vue-eslint-parser",
  parserOptions: {
    parser: "@typescript-eslint/parser",
    ecmaVersion: 2020,
    sourceType: "module",
  },
  plugins: ["vue"],
};
