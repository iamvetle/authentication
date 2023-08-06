import { createStore } from 'vuex'

export default createStore({
    state: {
        authenticated: false,
        token: null,
        userdata: null
    },
    mutations: {
        authenticate(state, status) {
            state.authenticated = status
        },
        tokenChange(state, token) {
            state.token = token
        }
    }
})