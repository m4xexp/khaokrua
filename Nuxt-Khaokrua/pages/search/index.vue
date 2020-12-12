<template>
  <div class="home-container">
    <v-row style="margin: 50px 20px auto; justify-content: center">
      <v-card class="search-text-field" elevation="1">
        <v-autocomplete
          v-model="model"
          hint="
                เช่น ต้มยำกุ้ง, ข้าวผัด, ผัดกะเพราหมูสับไข่ดาว
              "
          :items="states"
          :readonly="!isEditing"
          label="ทำไรกินดีน้า"
          persistent-hint
          prepend-icon="search"
          @keydown.enter="searchRecipe"
        >
        </v-autocomplete>
      </v-card>
    </v-row>

    <v-row
      no-gutters
      class="md-6"
      style="
        width: 97%;
        margin-left: 20px;
        margin-top: 20px;
        display: flex;
        justify-content: center;
      "
    >
      <v-sheet color="white" height="150" class="sheet-fav-menu">
        <v-breadcrumbs
          :items="breadcrumbs"
          style="position: absolute; left: 2em; top: 7em"
        >
          <template v-slot:item="{ item }">
            <v-breadcrumbs-item :href="item.href" :disabled="item.disabled">
              {{ item.text.toUpperCase() }}
            </v-breadcrumbs-item>
          </template>
        </v-breadcrumbs>
        <h1 style="text-align: left; margin-top: 1em">ผลการค้นหา</h1>
      </v-sheet>
    </v-row>

    <!-- Card menu -->

    <div class="menu-card-box">
      <v-layout row wrap class="menu-card-cober-each-card">
        <!-- Main favorite card -->

        <v-flex
          xs12
          sm6
          md4
          lg3
          v-for="recipe in result"
          :key="recipe.title"
          class="menu-card-each-card"
        >
          <!-- Card -->

          <v-card class="mx-auto" max-width="400" id="card-recipe">
            <!-- Img for recipe card -->

            <div class="card-recipe-zoom" style="overflow: hidden">
              <v-img
                class="card-recipe-img"
                height="200"
                :src="recipe.photo_recipe"
              ></v-img>
            </div>

            <div class="btn-fav-recipe">
              <div>
                <v-icon class="btn-fav-recipe-icon" style=""
                  >favorite_border</v-icon
                >
              </div>
            </div>

            <v-card-title style="font-size: 28px">{{
              recipe.title
            }}</v-card-title>

            <v-card-text class="card-data">
              <div class="box-card-data">
                <div class="card-data-cook-time">
                  <v-icon left>schedule</v-icon>
                  <span style="vertical-align: middle"
                    >{{ recipe.serve }} ชั่วโมง</span
                  >
                </div>
                <div class="card-data-cook-time" style="margin-left: 15px">
                  <v-icon left>group</v-icon>
                  <span style="vertical-align: middle">สำหรับ 2 ที่</span>
                </div>
              </div>

              <v-row align="center" class="mx-0">
                <v-rating
                  :value="recipe.serve"
                  color="amber"
                  dense
                  half-increments
                  readonly
                  size="14"
                ></v-rating>

                <div class="grey--text ml-4">{{ recipe.serve }} (413)</div>
              </v-row>
            </v-card-text>

            <v-card-actions>
              <v-btn block dark text style="background-color: #ff7043">
                <span>ทำอาหาร</span>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Home',

  components: {},

  pagination() {
    return {
      page: 1,
    }
  },

  data: () => ({
    loading: false,
    selection: 1,
    menus: [
      {
        Name: 'ต้มยำกุ้ง',
        Author: 'KhaoKrua',
        time: '1',
        rate: 4.7,
        src:
          'https://d12man5gwydfvl.cloudfront.net/wp-content/uploads/2019/06/shutterstock_430308484.jpg',
      },
      {
        Name: 'ข้าวผัด',
        Author: 'KhaoKrua',
        time: '1',
        rate: 4.7,
        src:
          'https://i.pinimg.com/originals/8b/52/0c/8b520ccac4a4372d62d33770ece3c529.jpg',
      },
      {
        Name: 'กะเพราทะเล',
        Author: 'KhaoKrua',
        time: '1',
        rate: 4.7,
        src: 'https://f.ptcdn.info/206/064/000/ps7ec58xwloZzLEw1eDJ-o.jpg',
      },
      {
        Name: 'พิซซ่า',
        Author: 'KhaoKrua',
        time: '1',
        rate: 4.7,
        src:
          'https://caffedolcemissoula.com/wp-content/uploads/2019/09/Pizza.jpg',
      },
    ],
    tags: [
      { tagName: 'Drink' },
      { tagName: 'Main Disc' },
      { tagName: 'Burger' },
      { tagName: 'Noodle' },
      { tagName: 'Fruit' },
      { tagName: 'Cheese' },
      { tagName: 'Cream' },
      { tagName: 'Soft Drink' },
      { tagName: 'Steak' },
      { tagName: 'Milk' },
      { tagName: 'Ice cream' },
    ],
    isEditing: true,
    model: null,
    states: [

    ],
    breadcrumbs: [
      {
        text: 'หน้าแรก',
        disabled: false,
        href: '/',
      },
      {
        text: 'ค้นหา',
        disabled: true,
        href: 'search',
      },
    ],
    result: [],
  }),
  methods: {
    async searchRecipe() {
      console.log('geting recipe ...')
      this.$store.commit('SET_DIALOG_LOADING', true)
      await axios.get('http://127.0.0.1:5000/api/search/').then((res) => {
        this.result = res.data
        console.log('data here', this.result)
      })
      console.log('finished ...')
      this.$store.commit('SET_DIALOG_LOADING', false)
    },
    async fetchRecipe() {
      console.log('seaching recipe ...')
      await axios.get('http://127.0.0.1:5000/api/search/keyword').then((res) => {
        this.states = res.data
        console.log('search here', res.data)
      })
      console.log('search finished ...')
    },
    EnterSearch() {
      console.log('Search is work!')
    },
  },
  mounted() {
    this.fetchRecipe()
  },
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Kanit:wght@200&display=swap');

* {
  margin: 0;
  padding: 0;
  outline: none;
  font-family: 'Kanit', sans-serif;
  box-sizing: border-box;
}

.home-container {
  margin: 5px auto;
  width: 90%;
  position: relative;
}

.search-text-field {
  //   background-color: rgb(255, 255, 255);
  width: 70%;
  padding: 10px;
  //   border-radius: 15px;
}

.v-sheet.v-card .search-text-field {
  border-radius: 40px;
}

.sheet-fav-menu {
  border-radius: 10px 10px 0px 0px;
  padding: 80px;
  margin-top: 0 auto;
  width: 100%;
}

.icon-in-add-fav {
  position: absolute;
  text-align: center;
  width: 100%;
  left: 50%;
  right: 50%;
  transform: translate(-50%, -50%);
  top: 40%;
}

.text-in-add-fav {
  position: absolute;
  text-align: center;
  width: 100%;
  left: 50%;
  right: 50%;
  transform: translate(-50%, -50%);
  top: 50%;
  font-weight: bold;
  margin: 20px auto;
}

.menu-card-cober-each-card .menu-card-each-card {
  padding: 15px 15px 15px 15px;
}

.menu-card-each-card .btn-fav-recipe .btn-fav-recipe-icon {
  position: absolute;
  left: 80%;
  bottom: 43%;
  background: red;
  color: white;
  font-size: 1.2em;
  font-weight: bold;
  padding: 15px;
  border-radius: 50%;
  transition: 0.3s ease-in-out;
}

.menu-card-each-card .btn-fav-recipe .btn-fav-recipe-icon:hover {
  transform: scale(1.1);
}

.header-menu-card-box {
  background-color: white;
  height: 150px;
  margin-top: 50px;
  padding: 20px;
  border-radius: 10px 10px 0px 0px;
  width: 30%;
}

.header-menu-card-box .header-text {
  margin: 30px auto;
  background-color: white;
  text-align: center;
}

#card-recipe {
  transition: 0.25s ease;
  overflow: hidden;
  // cursor: pointer;
}

#card-recipe:hover {
  transform: scale(1.05);
  box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.6);
}

#card-recipe .card-recipe-img {
  transition: 0.25s ease;
}

#card-recipe:hover .card-recipe-img {
  transform: scale(1.2);
}

.menu-card-box {
  background-color: white;
  margin-left: 20px;
  margin-right: 20px;
  padding: 20px;
}

.card-data .box-card-data {
  display: flex;
  justify-content: flex-start;
  margin: 10px auto;
}

@media only screen and (max-width: 376px) {
  #card-add-recipe {
    width: 250px;
  }
}

@media only screen and (max-width: 376px) {
  .sheet-fav-menu {
    margin-right: 30px;
    width: 91%;
  }
}

@media only screen and (max-width: 1920px) {
  #card-add-recipe {
    width: 300px;
  }
}

@media only screen and (max-width: 1024px) {
  #card-add-recipe {
    width: 258.52px;
  }
}

@media only screen and (max-width: 1024px) {
  .sheet-fav-menu {
    margin-right: 15px;
    width: 99%;
  }
}

@media only screen and (max-width: 768px) {
  #card-add-recipe {
    width: 287.6px;
  }
}
</style>


