import { createRouter, createWebHistory } from 'vue-router'
import UserPage from './components/UserPage.vue'
import Login from './components/Login.vue'


const routes = [
{ 
	path: '/', 
	name:'userpage', 
	component: UserPage 
},
{ 
	path: '/login', 
	name:"login", 
	component: Login 
}
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});



export default router
