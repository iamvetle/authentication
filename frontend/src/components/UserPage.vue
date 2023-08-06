<!-- This is only going to be rendered if a user is logged in -->

<template>
<div v-if="token !== null" class="container mx-auto"> <!-- User content-->
    <div class="absolute p-1 top-5 left-8 bg-blue-300 rounded-sm">
        <router-link to="/logout">logout</router-link>
    </div>
    <h1 class="mt-14 text-3xl text-center">Hello </h1>
    <p class="mt-6 text-center text-lg">Information about you</p>
    <p class="py-2 text-center">First name: _</p>
    <p class="py-2 text-center">Last name: _</p>
    <p class="py-2 text-center">username: _</p>
    <p class="py-2 text-center">email: _</p>
    <p class="py-2 text-center">***: _</p>


</div>

<div v-else class="container mx-auto">
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

        }
    },
    created () {

        if (localStorage.getItem("token")) {  

            axios.get("http://localhost:8888/api/user/", {
                headers: {
                'Authorization': `Token ${this.token}`
                }
            })
            .then((response) => {
                console.log(response.data)
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