<!-- This is only going to be rendered if a user is logged in -->

<template>
<div v-if="token">
    <!-- Content here -->
    <p>Hello {{ this.username }}</p>
    <router-link to="/logout">logout</router-link>
</div>

<div v-else>
    <h1>You are not logged in. You have to be logged in to see anything on this page</h1>
    <p>You can go here to log in:</p>
    <router-link to="/login">Log in link</router-link>
</div>



</template>

<script>
import axios from 'axios';



export default {
    data () {
        return {
            token: localStorage.getItem("token"),
             username: localStorage.getItem("username")

        }
    },
    created () {
        if (this.token) {  

            axios.get("http://localhost:8888/api/users/me/", {
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