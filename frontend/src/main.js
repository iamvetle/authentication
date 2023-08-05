import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router.js'

const app = createApp(App)

app.use(router) // "Adds the router to the application"

app.mount('#app')
