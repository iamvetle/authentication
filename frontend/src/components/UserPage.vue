<!-- This is only going to be rendered if a user is logged in -->

<template>
<p>kpokadsd</p>
<div v-if="state === false">
    <h1>You are not logged in. You have to be logged in to see anything on this page</h1>
    <p>You can go here to log in:</p>
    <router-link to="/login">Log in link</router-link>
</div>

<div v-if="state">
    <!-- Content here -->
    <p>ass</p>
</div>

</template>

<script>

import { mapState } from 'vuex'

export default {
    data () {
        return {
            state: localStorage.getItem("token")
        }
    },
    computed: {
        ...mapState(["authenticated", "token"])
    }
}
</script>

<style>
</style>