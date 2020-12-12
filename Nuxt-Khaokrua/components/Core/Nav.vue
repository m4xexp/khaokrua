<template>
  <div>
    <v-app-bar
      prominent
      absolute
      app
      dark
      class="header-nav"
      src="../../assets/Nav/cover_khaokrua.jpg"
    >

      <!-- Logo KhaoKrua -->

      <div class="header-nav-logo">
        <div class="nav-logo">
          <nuxt-link to="/">
            <v-img
              id="logo"
              class="shrink mr-2"
              contain
              src="../../assets/Nav/KhaoKrua_logo.png"
              transition="scale-transition"
              width="180"

            />
          </nuxt-link>
        </div>
      </div>


      <div class="search-field" style="">
          <v-text-field
            light
            style="width: 600px"
            value="Beef Wellington"
            label="ทำอะไรกินดีน้า"
            solo
            append-icon="search"
          ></v-text-field>
        <!-- <div class="btn-search-icon">
          <v-btn
            large
            height="50px"
            color="red darken-1"
            style="margin: 0 auto; left: 0px; bottom: 8px"
            class="btn-search"
          >
            <v-icon large alt="searchRecipt">search</v-icon>
          </v-btn>
        </div> -->
      </div>
      <ul class="nav-menu">
        <li class="btn-add-recipe">
          <nuxt-link to="/add">
            <v-icon>add</v-icon>
            <span>เพิ่มสูตรอาหาร</span>
          </nuxt-link>
        </li>

        <li class="btn-fav-recipe">
          <nuxt-link to="/favorite">
            <v-icon left>favorite</v-icon>
            <span>เมนูโปรด</span>
          </nuxt-link>
        </li>

        <!-- Profile Menu -->

        <li class="btn-login">
            <nuxt-link to="/login">
            <v-icon left>face</v-icon>
            <span>เข้าสู่ระบบ</span>
            </nuxt-link>
        </li>
        
      </ul>
    </v-app-bar>

  </div>
</template>

<script>
export default {
  data: () => ({
    image: [{ logoPath: '' }],

  }),
  methods: {

    
 }
}
</script>



<style lang="scss" scoped>


#logo {
  width: 10%;
}


.header-nav-logo {
  display: flex;
  position: absolute;
  justify-content: center;

}

.header-nav-logo .nav-logo {
  margin: 20px;
}

.header-nav .search-field {
  display: flex;
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: rgb(0, 0, 0, 0.1);
  max-width: 1000px;
  height: 80px;
  width: 47.5%;
  padding: 15px;
  // justify-content: space-between;
  border-radius: 8px;
}

@media only screen and (max-width: 1024px) {
  .header-nav .search-field {
    display: flex;
    position: absolute;
    top: 100%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: rgb(0, 0, 0, 0.1);
    max-width: 1000px;
    height: 80px;
    width: 70%;
    padding: 15px;
    justify-content: space-between;
    border-radius: 8px;
  }
}

@media only screen and (max-width: 768px) {
  .header-nav .search-field {
    display: flex;
    position: absolute;
    top: 100%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: rgb(0, 0, 0, 0.1);
    max-width: 1000px;
    height: 80px;
    width: 94%;
    padding: 15px;
    justify-content: space-between;
    border-radius: 8px;
  }
}

.search-field .search .btn-search-icon {
  position: absolute;
}

.header-nav .nav-menu {
  float: right;
  margin: 0 auto;
  margin-right: 0;
  /* background-color: yellow; */
}

ul li a {
  text-decoration: none;
}

ul li {
  cursor: pointer;
}

li a span {
  font-size: 16px;
  color: rgb(255, 255, 255);
}

li div span {
  font-size: 16px;
  color: rgb(255, 255, 255);
}

.header-nav ul li {
  margin: 3px 5px;
  display: inline-block;
  & > .btn-profile{
    display: none;
  }
}

span {
  vertical-align: middle;
}

.header-nav-menu .nav-menu .btn-add-recipe {
  /* background-color: blue; */
  height: 15%;
}

.header-nav-menu .nav-menu .btn-fav-recipe {
  /* background-color: blue; */
  height: 15%;
}

.header-nav-menu .nav-menu .btn-profile {
  margin: 0;
  display: none;
  /* background-color: black; */
}
</style>