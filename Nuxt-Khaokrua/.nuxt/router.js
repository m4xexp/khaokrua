import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL } from '@nuxt/ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _a94cda1e = () => interopDefault(import('..\\pages\\add\\index.vue' /* webpackChunkName: "pages/add/index" */))
const _ed094aec = () => interopDefault(import('..\\pages\\dummy\\index.vue' /* webpackChunkName: "pages/dummy/index" */))
const _852b2790 = () => interopDefault(import('..\\pages\\Edit\\index.vue' /* webpackChunkName: "pages/Edit/index" */))
const _37252d86 = () => interopDefault(import('..\\pages\\favorite\\index.vue' /* webpackChunkName: "pages/favorite/index" */))
const _226dbd6e = () => interopDefault(import('..\\pages\\Login\\index.vue' /* webpackChunkName: "pages/Login/index" */))
const _1efdd608 = () => interopDefault(import('..\\pages\\myRecipe\\index.vue' /* webpackChunkName: "pages/myRecipe/index" */))
const _741bae2e = () => interopDefault(import('..\\pages\\profile\\index.vue' /* webpackChunkName: "pages/profile/index" */))
const _3f112454 = () => interopDefault(import('..\\pages\\recipe\\index.vue' /* webpackChunkName: "pages/recipe/index" */))
const _7184400c = () => interopDefault(import('..\\pages\\search\\index.vue' /* webpackChunkName: "pages/search/index" */))
const _381362ec = () => interopDefault(import('..\\pages\\signup\\index.vue' /* webpackChunkName: "pages/signup/index" */))
const _605f3222 = () => interopDefault(import('..\\pages\\index.vue' /* webpackChunkName: "pages/index" */))

// TODO: remove in Nuxt 3
const emptyFn = () => {}
const originalPush = Router.prototype.push
Router.prototype.push = function push (location, onComplete = emptyFn, onAbort) {
  return originalPush.call(this, location, onComplete, onAbort)
}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: '/',
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/add",
    component: _a94cda1e,
    name: "add"
  }, {
    path: "/dummy",
    component: _ed094aec,
    name: "dummy"
  }, {
    path: "/Edit",
    component: _852b2790,
    name: "Edit"
  }, {
    path: "/favorite",
    component: _37252d86,
    name: "favorite"
  }, {
    path: "/Login",
    component: _226dbd6e,
    name: "Login"
  }, {
    path: "/myRecipe",
    component: _1efdd608,
    name: "myRecipe"
  }, {
    path: "/profile",
    component: _741bae2e,
    name: "profile"
  }, {
    path: "/recipe",
    component: _3f112454,
    name: "recipe"
  }, {
    path: "/search",
    component: _7184400c,
    name: "search"
  }, {
    path: "/signup",
    component: _381362ec,
    name: "signup"
  }, {
    path: "/",
    component: _605f3222,
    name: "index"
  }],

  fallback: false
}

function decodeObj(obj) {
  for (const key in obj) {
    if (typeof obj[key] === 'string') {
      obj[key] = decodeURIComponent(obj[key])
    }
  }
}

export function createRouter () {
  const router = new Router(routerOptions)

  const resolve = router.resolve.bind(router)
  router.resolve = (to, current, append) => {
    if (typeof to === 'string') {
      to = normalizeURL(to)
    }
    const r = resolve(to, current, append)
    if (r && r.resolved && r.resolved.query) {
      decodeObj(r.resolved.query)
    }
    return r
  }

  return router
}
