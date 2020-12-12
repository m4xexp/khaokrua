import Vuex from 'vuex'
import { server } from '~/services/constants.js';
import api from "../services/api.js";
import axios from 'axios'

const createStore = () => {
    return new Vuex.Store({
        state: {
            navDefault: true,
            navLogin: false,
            loading: false,
            dialogMessage: "",
            userID: null,
            userData: {
                email:"",
                fname:"",
                lname:"",
                password: "",
                profile_name: "",
                profile_pic: "",
                user_id: ""
            },
            dialogMessage: "",
            stateLoginDialog: false,
            loginState: false,
            SkeletonLoad: false
        },
        getters: {
            getNavDefaultState(state) {
                return state.navDefault
            },
            getNavLoginState(state) {
                return state.navLogin
            },
            getLoadingState(state) {
                return state.loading
            },
            getDialogMsg(state) {
                return state.dialogMessage
            },
            getUserID(state) {
                return state.userID
            },
            getUserData(state) {
                return state.userData
            },
            getDialogState(state) {
                return state.dialogState
            },
            getLoginState(state) {
                return state.loginState
            }

        },
        mutations: {
            SET_NAV_DEFAULT(state, value) {
                state.navDefault = value
            },
            SET_NAV_LOGIN(state, value) {
                state.navLogin = value
            },
            SET_DIALOG_LOADING(state, value) {
                state.loading = value
            },
            SET_DIALOG_MESSAGE(state, msg) {
                state.dialogMessage = msg
            },
            SET_USER_ID(state, userID) {
                state.userID = userID
            },
            SET_USER_DATA(state, userData) {
                state.userData = userData
            },
            SET_LOGIN_STATE(state, value) {
                state.loginState = value
            }

        },
        actions: {
            
            defaultHome({ commit }) {
                commit('SET_NAV_DEFAULT', true)
                commit('SET_NAV_LOGIN', false)

            },

            dialogPopup({ commit }, { value, msg }) {
                commit("SET_DIALOG_STATE", value)
                commit("SET_DIALOG_MESSAGE", msg)
            },

            restoreLogin({ commit }) {
                if (api.isLoggedIn() === true) {
                    const username = localStorage.getItem('USERNAME');
                    commit("SET_USER_ID", username);
                    commit("SET_NAV_DEFAULT", false)
                    commit("SET_NAV_LOGIN", true)
                    commit("SET_LOGIN_STATE", true)
                    commit("SET_DIALOG_LOADING", false)
                    console.log('Login State',this.state.loginState)
                    axios
                        .get('http://127.0.0.1:5000/api/user/' + this.state.userID)
                        .then((res) => {
                            commit("SET_USER_DATA", res.data[0])
                            console.log('user Data', this.state.userData)
                        })

                } else {
                    commit("SET_NAV_DEFAULT", true)
                    commit('SET_NAV_LOGIN', false)
                    commit("SET_LOGIN_STATE", false)
                    commit("SET_DIALOG_LOADING", false)
                }
            },

            logout({ commit }) {
                api.logoff()
                commit("SET_USER_ID", null);
                commit("SET_NAV_DEFAULT", true)
                commit('SET_NAV_LOGIN', false)
                commit("SET_LOGIN_STATE", false)
                
                // router.push({ name: "Home" })
            },
        },

    })
}

export default createStore