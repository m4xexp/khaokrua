export { default as Popup } from '../..\\components\\Popup\\popup.vue'
export { default as AddIngred } from '../..\\components\\AddRecipe\\AddIngred.vue'
export { default as AddSteps } from '../..\\components\\AddRecipe\\AddSteps.vue'
export { default as Loader } from '../..\\components\\Core\\Loader.vue'
export { default as Nav } from '../..\\components\\Core\\Nav.vue'
export { default as NavLogin } from '../..\\components\\Core\\NavLogin.vue'
export { default as NavLogSearch } from '../..\\components\\Core\\NavLogSearch.vue'
export { default as PageNotFound } from '../..\\components\\Core\\PageNotFound.vue'

export const LazyPopup = import('../..\\components\\Popup\\popup.vue' /* webpackChunkName: "components_Popup/popup" */).then(c => c.default || c)
export const LazyAddIngred = import('../..\\components\\AddRecipe\\AddIngred.vue' /* webpackChunkName: "components_AddRecipe/AddIngred" */).then(c => c.default || c)
export const LazyAddSteps = import('../..\\components\\AddRecipe\\AddSteps.vue' /* webpackChunkName: "components_AddRecipe/AddSteps" */).then(c => c.default || c)
export const LazyLoader = import('../..\\components\\Core\\Loader.vue' /* webpackChunkName: "components_Core/Loader" */).then(c => c.default || c)
export const LazyNav = import('../..\\components\\Core\\Nav.vue' /* webpackChunkName: "components_Core/Nav" */).then(c => c.default || c)
export const LazyNavLogin = import('../..\\components\\Core\\NavLogin.vue' /* webpackChunkName: "components_Core/NavLogin" */).then(c => c.default || c)
export const LazyNavLogSearch = import('../..\\components\\Core\\NavLogSearch.vue' /* webpackChunkName: "components_Core/NavLogSearch" */).then(c => c.default || c)
export const LazyPageNotFound = import('../..\\components\\Core\\PageNotFound.vue' /* webpackChunkName: "components_Core/PageNotFound" */).then(c => c.default || c)
