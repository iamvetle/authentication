<template>

    <div class="container w-2/12 mx-auto pt-20">
      <h1 class="text-2xl pb-4">Login page</h1>
      <label for="username">Email (username):</label>
      <input type="text" id="username" v-model="username" required class="border block mb-2 border-blue-500">
      <label for="pwd">Password:</label>
      <input type="password" id="pwd" v-model="password" required class="border block border-blue-500">
      
      <button @click="login" class="rounded-sm bg-slate-400 mt-4 text-white px-1 py-1">
        Submit
      </button>

      <hr class="block my-4" />
      
      <p class="mt-5 text-red-700" v-show="loginerror">Invalid credentials</p>
      <p class="mt-5 text-green-700" v-show="loginsucess">Login successfull</p>

      <p class="mt-5">No account?</p>
      <p class="pt-2">Click her to register for a new account</p>
      <button class="bg-slate-200 p-1 rounded-sm mt-3"><router-link to="/register">Register</router-link></button>
    </div>
    
    </template>
    
    <script>
    
    import axios from 'axios';
    
    export default {
      data() {
        return {
          username:"",
          password:"",
          
          authurl: "http://localhost:8888/api/user/auth/",
          loginerror:false,
          loginsucess:false,
        }
      },
      methods: {
        async login() {
            const logindata = {
                username: this.username,
                password: this.password
            };
          try {
              const response = await axios.post(this.authurl, logindata) 
              console.log(`Authentication token: ${response.data.token}`)
              
              localStorage.setItem("token", response.data.token)
              
              this.username = ""
              this.password = ""
              this.loginerror = false
              this.loginsucess = true

              this.$router.replace("/") // Success -> redirect to user home page 
        
            } catch(error) { // Fail -> Stay on site
              console.error("An error occour while trying to log in")
              this.loginerror = true
              this.logingsucess = false
              this.password = ""
          } 
        }
          },
          created () {
          if (localStorage.getItem("token") !== null) { // If the user is already authenticated redirect back to homepage
            this.$router.replace("/")
        }
      }
    }
    
    </script>
    
    <style>
    </style>