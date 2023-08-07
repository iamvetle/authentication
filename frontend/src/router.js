import { createRouter, createWebHistory } from 'vue-router'
import UserPage from './components/UserPage.vue'
import Login from './components/Login.vue'
import Logout from './components/Logout.vue'
//import Register from './components/Register.vue'


const routes = [
{
	path:'/',
	name:'mypage',
	component:UserPage,
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
},
// {
// 	path: '/register', 
// 	name: "register", 
// 	component: Register 
// }
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});



export default router
