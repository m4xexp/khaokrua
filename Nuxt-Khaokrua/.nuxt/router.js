import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL } from '@nuxt/ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _8c134c98 = () => interopDefault(import('..\\pages\\add\\index.vue' /* webpackChunkName: "pages/add/index" */))
const _64017c8d = () => interopDefault(import('..\\pages\\dummy\\index.vue' /* webpackChunkName: "pages/dummy/index" */))
const _fb330456 = () => interopDefault(import('..\\pages\\Edit\\index.vue' /* webpackChunkName: "pages/Edit/index" */))
const _165528a3 = () => interopDefault(import('..\\pages\\favorite\\index.vue' /* webpackChunkName: "pages/favorite/index" */))
const _6d617968 = () => interopDefault(import('..\\pages\\Login\\index.vue' /* webpackChunkName: "pages/Login/index" */))
const _03a45db6 = () => interopDefault(import('..\\pages\\myRecipe\\index.vue' /* webpackChunkName: "pages/myRecipe/index" */))
const _1777d62c = () => interopDefault(import('..\\pages\\profile\\index.vue' /* webpackChunkName: "pages/profile/index" */))
const _95617a9e = () => interopDefault(import('..\\pages\\recipe\\index.vue' /* webpackChunkName: "pages/recipe/index" */))
const _3d7bfe57 = () => interopDefault(import('..\\pages\\search\\index.vue' /* webpackChunkName: "pages/search/index" */))
const _5a346ce7 = () => interopDefault(import('..\\pages\\signup\\index.vue' /* webpackChunkName: "pages/signup/index" */))
const _5c880502 = () => interopDefault(import('..\\pages\\index.vue' /* webpackChunkName: "pages/index" */))

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
    component: _8c134c98,
    name: "add"
  }, {
    path: "/dummy",
    component: _64017c8d,
    name: "dummy"
  }, {
    path: "/Edit",
    component: _fb330456,
    name: "Edit"
  }, {
    path: "/favorite",
    component: _165528a3,
    name: "favorite"
  }, {
    path: "/Login",
    component: _6d617968,
    name: "Login"
  }, {
    path: "/myRecipe",
    component: _03a45db6,
    name: "myRecipe"
  }, {
    path: "/profile",
    component: _1777d62c,
    name: "profile"
  }, {
    path: "/recipe",
    component: _95617a9e,
    name: "recipe"
  }, {
    path: "/search",
    component: _3d7bfe57,
    name: "search"
  }, {
    path: "/signup",
    component: _5a346ce7,
    name: "signup"
  }, {
    path: "/",
    component: _5c880502,
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
