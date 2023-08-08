<template>
    <div>
      <form @submit.prevent="submitForm">
        <div>
          <label for="form.first_name">First Name:</label>
          <input class="border" v-model="form.first_name" id="first_name"/>
          <div v-if="v$.form.first_name.$error">
            First name is required.
          </div>
        </div>
  
        <div>
          <label for="form.last_name">Last Name:</label>
          <input class="border" v-model="form.last_name" id="last_name" />
          <div v-if="v$.form.last_name.$error">
            Last name is required.
          </div>
        </div>
  
        <div>
          <label for="form.email">Email:</label>
          <input class="border" v-model="form.email" id="email" type="email" />
          <div v-if="v$.form.email.$error">
            Please enter a valid email address.
          </div>
        </div>

        <div>
            <label for="form.phone">Phone number:</label>
            <input class="border" v-model="form.phone" id="phone" />
        </div>
  
        <div>
          <label for="form.password">Password:</label>
          <input class="border" v-model="form.password" id="password" type="password" />
          <div v-if="v$.form.password.$error">
            Password must be at least 6 characters long.
          </div>
        </div>

        <div>
        <label for="form.confirmPassword">Confirm Password:</label>
        <input class="border" v-model="form.confirmPassword" id="confirmPassword" type="password" />
        <div class="text-red-500" v-if="v$.form.confirmPassword.$error">
          The passwords do not match.
        </div>
      </div>
  
        <button class="bg-slate-200" type="submit">Register</button>
      </form>
    </div>
  </template>
  
<script>

import { useVuelidate } from '@vuelidate/core'
import { required, email, sameAs, minLength } from '@vuelidate/validators' 
import axios from 'axios'

export default {
  setup () {
    return {
      v$: useVuelidate()
    }
    },    
    data() {
        return {
          url:"http://localhost:8888/api/user/register/",
          form: {
            first_name:"",
            last_name:"",
            email:"",
            phone:"",
            password:"",
            confirmPassword:"",
        }
        }
  },
  validations () {
    return {
      form: {
        first_name:{ required, $autoDirty: true },
        last_name:{ required, $autoDirty: true },
        email: { required, email, $autoDirty: true  },
        phone: {}, 
        password:{ required, minLength: minLength(6), $autoDirty: true },
        confirmPassword: {sameAsPassword: sameAs(this.form.password), $autoDirty: true },
      }
    }
  },
  methods: {
    async submitForm() {
        
        if (! await this.v$.$validate()) {
            console.log("Wrong form data:")
        } else {

            axios.post(this.url, this.form)
            .then((response) => {
              console.log("Successfull. Response: ", response.data)
            })
            .catch((error) => {
              console.error("Unsuccessfull. Response: ", error)
            })

            this.form.first_name = ""
            this.form.last_name = ""
            this.form.email = ""
            this.form.phone = ""
            this.form.password = ""
            this.form.confirmPassword = ""
        
            this.v$.$reset()

            this.$router.push('/login')
          }
    }
  }
}

</script>