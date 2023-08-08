<template>
    <div>
      <form @submit.prevent="submitForm">
        <div>
          <label for="first_name">First Name:</label>
          <input class="border" v-model="first_name" id="first_name"/>
          <div v-if="v$.first_name.$error">
            First name is required.
          </div>
        </div>
  
        <div>
          <label for="last_name">Last Name:</label>
          <input class="border" v-model="last_name" id="last_name" />
          <div v-if="v$.last_name.$error">
            Last name is required.
          </div>
        </div>
  
        <div>
          <label for="email">Email:</label>
          <input class="border" v-model="email" id="email" type="email" />
          <div v-if="v$.email.$error">
            Please enter a valid email address.
          </div>
        </div>

        <div>
            <label for="phone">Phone:</label>
            <input class="border" v-model="phone" id="phone" />
        </div>
  
        <div>
          <label for="password">Password:</label>
          <input class="border" v-model="password" id="password" type="password" />
          <div v-if="v$.password.$error">
            Password must be at least 6 characters long.
          </div>
        </div>

        <div>
        <label for="confirmPassword">Confirm Password:</label>
        <input class="border" v-model="confirmPassword" id="confirmPassword" type="password" />
        <div class="text-red-500" v-if="v$.confirmPassword.$error">
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

export default {
  setup () {
    return {
      v$: useVuelidate()
    }
    },    
    data() {
        return {
            first_name:"",
            last_name:"",
            email:"",
            phone:"",
            password:"",
            confirmPassword:"",
        }
  },
  validations () {
    return {
        first_name:{ required, $autoDirty: true },
        last_name:{ required, $autoDirty: true },
        email: { required, email, $autoDirty: true  },
        phone: { }, 
        password:{ required, minLength: minLength(6), $autoDirty: true },
        confirmPassword: {sameAsPassword: sameAs(this.password), $autoDirty: true },
      }
  },
  methods: {
    async submitForm() {
        
        if (! await this.v$.$validate()) {
            console.log("Wrong form data:")
        } else {
            console.log("Form data:")
        }
    }
  }
}

</script>