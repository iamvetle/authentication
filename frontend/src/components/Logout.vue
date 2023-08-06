<template>
    <p>Successfully logged out</p>
    <router-link to="/login">login here</router-link>
</template>

<script>
export default {
    data() {
        return {
            
        }
    },
    created () {
        function logout() {
            localStorage.removeItem("token");
            console.log("You are logged out: token removed")
        }
        logout()
    }
}
</script>

<style></style>