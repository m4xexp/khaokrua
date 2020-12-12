<template>
  <div class="login-container">
    <v-card class="card-login" style="border-radius: 10px; margin-top: 100px">
      <v-row justify="center" class="title">
        <span class="login-title"> เข้าสู่ระบบ </span>
      </v-row>
      <v-form ref="form" lazy-validation>
        <div class="input-email">
          <v-text-field
            color="primary"
            solo
            rounded
            outlined
            v-model="account.email"
            required
            autocomplete="username"
            :rules="emailRules"
            placeholder="Email"
            name="email"
          ></v-text-field>
        </div>

        <div class="input-password">
          <v-text-field
            solo
            rounded
            outlined
            placeholder="Password"
            required
            min="9"
            autocomplete="password"
            :rules="passwordRules"
            v-model="account.password"
            :type="showPassword ? 'text' : 'password'"
            :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="showPassword = !showPassword"
            name="password"
          ></v-text-field>
        </div>

        <div class="action-form">
          <v-btn
            color="success"
            class="mr-4"
            @click="handleLoginClicked"
            id="btnLogin"
            name="btnLogin"
            style="width: 100%"
          >
            เข้าสู่ระบบ
          </v-btn>
        </div>

        <v-row justify="center">
          <p style="margin-right: 10px" class="text">ยังไม่มีบัญชีใช่มั้ย?</p>
          <router-link to="/signup">
            <p class="text">สมัครสมาชิก</p>
          </router-link>
        </v-row>
      </v-form>
    </v-card>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'login',
  components: {},
  data() {
    return {
      showPassword: false,
      account: {
        email: '',
        password: '',
      },
      valid: true,
      passwordRules: [
        (v) => !!v || 'ต้องการรหัสผ่าน',
        (v) => (v && v.length >= 6) || 'รหัสผ่านควรมีมากกว่า 6 ตัว',
      ],
      emailRules: [
        (v) => !!v || 'ต้องการอีเมล',
        (v) => /.+@.+\..+/.test(v) || 'อีเมลต้องมีอยู่',
      ],
    }
  },
  methods: {
    // submit() {
    //   var state = this.$refs.form.validate()
    //   if (state) {
    //     this.$store.dispatch({
    //       type: 'doLogin',
    //       email: this.account.email,
    //       password: this.account.password,
    //     })
    //   }
    // },
    async handleLoginClicked(event) {
      this.$store.commit('SET_DIALOG_LOADING', true)
      event.preventDefault()
      var bodyFormData = new FormData()
      bodyFormData.append('username', this.account.email)
      bodyFormData.append('password', this.account.password)

      var result = await axios({
        method: 'post',
        url: 'http://127.0.0.1:5000/api/login',
        data: bodyFormData,
        headers: { 'Content-Type': 'multipart/form-data' },
      })
      console.log(result)
      if (result.data.Error) {
        this.$store.commit('SET_DIALOG_LOADING', false)
        this.$store.commit('SET_LOGIN_STATE', false)
        this.$store.commit('SET_NAV_DEFAULT', true)
        this.$store.commit('SET_NAV_LOGIN', false)
        this.$store.commit('SET_DIALOG_LOADING', false)
      } else {
        localStorage.setItem('USERNAME', result.data.Message)
        this.$store.commit('SET_LOGIN_STATE', true)
        this.$store.commit('SET_NAV_DEFAULT', false)
        this.$store.commit('SET_NAV_LOGIN', true)
        this.$store.commit('SET_DIALOG_LOADING', false)
      }
    },
  },
}
</script>

<style scope>
@import url('https://fonts.googleapis.com/css2?family=Kanit:wght@200&display=swap');

* {
  list-style: none;
  outline: none;
  font-family: 'Kanit', sans-serif;
  box-sizing: border-box;
}

.login-container {
  height: 100px;
}

.title {
  text-align: center;
  margin-bottom: 1em;
}

.login-title {
  font-size: 36px;
  font-weight: bold;
  text-align: center;
}

.card-login {
  padding: 30px;
  margin: 50px auto;
  max-width: 600px;
}

.action-form {
  width: 50%;
  display: flex;
  flex-direction: column;
  margin: 20px auto;
}

@media only screen and (max-width: 1264px) {
  .card-login {
    max-width: 800px;
  }
}

@media only screen and (max-width: 960px) {
  .card-login {
    width: 600px;
  }
}

@media only screen and (max-width: 600px) {
  .card-login {
    width: 300px;
  }
}
</style>