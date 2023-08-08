<!-- This is only going to be rendered if a user is logged in -->

<template>
<div v-if="token !== null" class="container w-3/12 mx-auto"> <!-- Has account: User content-->
    <div class="absolute p-1 top-5 left-8 bg-blue-300 rounded-sm ">
        <router-link to="/logout">logout</router-link>
    </div>
    <h1 class="mt-14 mb-6 text-3xl">Hello {{ first_name }} </h1>
    <p class="py-2 "><span class="font-bold">First name:</span> {{ first_name }}</p>
    <p class="py-2 "><span class="font-bold">Last name:</span> {{ last_name }}</p>
    <p class="py-2 "><span class="font-bold">Email:</span> {{ email }}</p>
    <p class="py-2 "><span class="font-bold">Phone number:</span> {{ phone }}</p>

</div>

<div v-else class="container mx-auto"> <!-- No account -->
    <h1 class="text-center py-5 text-3xl">Cool site</h1>
    <h2 class="text-center mt-7 text-lg clear-both">You have to have an account to be a enter this website.</h2>
    <button class="block mx-auto mt-5 bg-slate-500 p-2 rounded-sm">
        <router-link to="/login">login</router-link>
    </button>

    <button disabled class="mx-auto mt-5 bg-slate-200 rounded-sm text-sm">
        <router-link v-show="false" to="/register">register</router-link>
    </button>
    <p class="mx-auto mt-1" v-show="false"> If you don't have an account, you can click here to register.</p>
    
</div>

</template>

<script>
import axios from 'axios';

export default {
    data () {
        return {
            token: undefined,
            email:"",
            first_name:"",
            last_name:"",
            phone: "",
        }
    },
    created () {
        this.token = localStorage.getItem("token")
        console.log("Token: ", this.token)
        if (this.token !== null) {  // DOES have a token

            axios.get("http://localhost:8888/api/user/", {
                headers: {
                'Authorization': `Token ${this.token}`
                }
            })
            .then((response) => {
                console.log(response.data)
                this.email = response.data.email
                this.first_name = response.data.first_name
                this.last_name = response.data.last_name
                this.phone = response.data.phone
            })
            .catch((error) => {
                console.error(error)
            })
        }
    }
}
</script>

<style>
</style>