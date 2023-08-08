<template>
    <div>
      <form @submit.prevent="submitForm">
        <div>
          <label for="firstName">First Name:</label>
          <input class="border" v-model="form.firstName" id="firstName" />
          <div v-if="!v$.form.firstName.$pending && !v$.form.firstName.required">
            First name is required.
          </div>
        </div>
  
        <div>
          <label for="lastName">Last Name:</label>
          <input class="border" v-model="form.lastName" id="lastName" />
          <div v-if="!v$.form.lastName.$pending && !v$.form.lastName.required">
            Last name is required.
          </div>
        </div>
  
        <!-- <div>
          <label for="username">Username:</label>
          <input v-model="form.username" id="username" />
          <div v-if="!v$.form.username.$pending && !v$.form.username.minLength">
            Username must be at least 3 characters long.
          </div>
        </div> -->
  
        <div>
          <label for="email">Email:</label>
          <input class="border" v-model="form.email" id="email" type="email" />
          <div v-if="!v$.form.email.$pending && !v$.form.email.email">
            Please enter a valid email address.
          </div>
        </div>
  
        <div>
          <label for="password">Password:</label>
          <input class="border" v-model="form.password" id="password" type="password" />
          <div v-if="!v$.form.password.$pending && !v$.form.password.minLength">
            Password must be at least 6 characters long.
          </div>
        </div>
  
        <button class="bg-slate-200" type="submit">Register</button>
      </form>
    </div>
  </template>
  
<script>
  import { required, minLength, email } from '@vuelidate/validators';
  import { useVuelidate } from '@vuelidate/core';
    
  export default {
    data() {
      return {
        form: {
          firstName: '',
          lastName: '',
          // username: '',
          email: '',
          password: '',
        },
      };
    },
    validations: {
      form: {
        firstName: { required },
        lastName: { required },
        // username: { minLength: minLength(3) },
        email: { email },
        password: { minLength: minLength(6) },
      },
    },
    setup() {
      const v$ = useVuelidate();
      return { v$ };
    },
    methods: {
      submitForm() {
        this.v$.form.$touch();  // This triggers the validation for all fields
        if (this.v$.form.$invalid) {
          alert('Please fix the errors before submitting.');
        } else {
          console.log('Form data:', this.form);
        }
      }
    },
  };
</script>
  
  