<template>
    <div class="w-4/12 container mx-auto">
        <h2 class="text-2xl text-center pb-9 mt-14">Successfully logged out</h2>
        <button class="p-1 mt- block mx-auto bg-slate-400 rounded-sm">
            <router-link to="/login">Login here</router-link>
        </button>
    </div>
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