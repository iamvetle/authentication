<template>

<div class="container w-3/12 mx-auto pt-20">
  <h1 class="text-2xl pb-4">Login page</h1>
  <label for="username">Username:</label>
  <input type="text" id="username" v-model="username" required class="border block mb-2 border-blue-500">
  <label for="pwd">Password:</label>
  <input type="password" id="pwd" v-model="password" required class="border block border-blue-500">
  <button @click="login" class="rounded-sm bg-slate-400 mt-4 text-white px-1 py-1" >Submit</button>
</div>

</template>

<script>

import axios from 'axios'

export default {
  data() {
    return {
      username:"",
      password:"",
      authurl: "http://localhost:8888/api-token-auth/"
    }
  },
  methods: {
    async login() {
        const data = {
            "username": this.username,
            "password": this.password
        };
      try {
        response = await axios.post(this.authurl, data)
          console.log("Post request successfull", response.data)
          const token = response.data.token
          console.log(`Authentication token: ${token}`)
          localStorage.setItem("token", token)
          
          this.username = ""
          this.password = ""
          // redirect to user home page 
        } catch(error) {
            console.error("An error occour while trying to log in", error)
            this.username = "failed"
            this.password = "failed"
        // return login failed or something
      } 
    },
    logout() {
        localStorage.removeItem("token");
        console.log("You are logged out: token removed")
    }
}
}

</script>

<style>
</style>