import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import store from './store'
// import { ValidatePlugin } from '@vuelidate/core'

const app = createApp(App)

app.use(router) // "Adds the router to the application"
app.use(store)
//app.use(ValidatePlugin)

app.mount('#app')
