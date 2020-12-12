<template>
  <div class="signup-container">
    <v-card class="card-signup" style="border-radius: 10px; margin-top: 30px">
      <v-row justify="center" class="title">
        <span class="signup-title"> สมัครสมาชิก </span>
      </v-row>
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-row>
          <v-col cols="12" md="6">
            <v-text-field
              solo
              outlined
              rounded
              v-model="user.fname"
              :rules="nameRules"
              label="ชื่อ"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="6">
            <v-text-field
              solo
              outlined
              rounded
              v-model="user.lname"
              :rules="nameRules"
              label="นามสกุล"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="6">
            <v-text-field
              solo
              outlined
              rounded
              v-model="user.profile_name"
              :rules="nameRules"
              label="ชื่อที่ใช้แสดง"
              required
            ></v-text-field>
          </v-col>
        </v-row>

        <div class="input-email">
          <v-text-field
            color="primary"
            solo
            rounded
            outlined
            v-model="user.email"
            required
            autocomplete="username"
            :rules="emailRules"
            placeholder="อีเมล"
            name="email"
          ></v-text-field>
        </div>

        <div class="input-password">
          <v-text-field
            solo
            rounded
            outlined
            placeholder="รหัสผ่าน"
            required
            min="9"
            autocomplete="password"
            :rules="passwordRules"
            v-model="user.password"
            :type="showPassword ? 'text' : 'password'"
            :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="showPassword = !showPassword"
            name="password"
          ></v-text-field>
        </div>

        <div class="input-confirm-password">
          <v-text-field
            solo
            rounded
            outlined
            placeholder="ยืนยันรหัสผ่าน"
            required
            min="9"
            autocomplete="password"
            :rules="passwordRules"
            v-model="passwordCon"
            :type="showPassword ? 'text' : 'password'"
            :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="showPassword = !showPassword"
            name="conPassword"
          ></v-text-field>
        </div>

        <div class="action-form">
          <v-btn
            color="success"
            class="mr-4"
            @click="handleRegisterClicked"
            id="btnLogin"
            name="btnLogin"
            style="width: 100%"
          >
            สมัครสมาชิก
          </v-btn>
        </div>
      </v-form>
    </v-card>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'signup',
  components: {},
  data() {
    return {
      showPassword: false,
      user: {
        fname: '',
        lname: '',
        profile_name: '',
        profilePic: '',
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
      passwordCon: '',
    }
  },
  methods: {
    submit() {
      var state = this.$refs.form.validate()
      if (state) {
        this.$store.dispatch({
          type: 'doLogin',
          email: this.user.email,
          password: this.user.password,
        })
      }
    },
    async handleRegisterClicked(event) {
      this.$store.commit("SET_DIALOG_LOADING", true)
      event.preventDefault()
      var bodyFormData = new FormData()
      bodyFormData.append('fname', this.user.fname);
      bodyFormData.append('lname', this.user.lname);  
      bodyFormData.append(
        'profilePic',
        'https://yt3.ggpht.com/ytc/AAUvwnh7XuN_QJ45cyqPzRBj42MLK9v0wwGqc62sc-OayA=s900-c-k-c0x00ffffff-no-rj'
      );
      bodyFormData.append('email', this.user.email);
      bodyFormData.append('password', this.user.password);
      bodyFormData.append('profile_name', this.user.profile_name);

      await axios({
        method: 'post',
        url: 'http://127.0.0.1:5000/api/register',
        data: bodyFormData,
        headers: { 'Content-Type': 'multipart/form-data' },
      })
        .then(function (response) {
          //handle success
          console.log('register result', response)
        })
        .catch(function (err) {
          //handle error
          console.log(err)
        })
        this.$store.commit("SET_DIALOG_LOADING", false)
    },
  },
}
</script>

<style scope>
.signup-container {
  height: 100px;
}

.title {
  text-align: center;
  margin-bottom: 1em;
}

.signup-title {
  font-size: 36px;
  font-weight: bold;
  text-align: center;
}

.card-signup {
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
  .card-signup {
    max-width: 800px;
  }
}

@media only screen and (max-width: 960px) {
  .card-signup {
    width: 600px;
  }
}

@media only screen and (max-width: 600px) {
  .card-signup {
    width: 300px;
  }
}
</style>