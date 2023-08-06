import { createRouter, createWebHistory } from 'vue-router'
import UserPage from './components/UserPage.vue'
import Login from './components/Login.vue'
import Logout from './components/Logout.vue'


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
},
{
	path: '/logout', 
	name: "logout", 
	component: Logout 
}
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});



export default router
