<template>
  <div class="home-container">
    <v-row no-gutters class="wraper-header-menu">
      <v-col height="150" class="col-header">
        <v-sheet class="sheet-header-menu" color="white">
          <span class="header-text">
            เมนูเเนะนำสำหรับคุณ
          </span>
        </v-sheet>
      </v-col>

      <!-- Tag box -->

      <v-col height="150" class="col-tag">
        <v-sheet class="sheet-tag-menu">
          <v-chip-group active-class="primary--text" class="chip-tag-group">
            <v-chip
              large
              color="red"
              outlined
              link
              v-for="tag in tags"
              :key="tag.tagName"
            >
              {{ tag.tagName }}
            </v-chip>
          </v-chip-group>
        </v-sheet>
      </v-col>
    </v-row>

    <!-- Card menu -->

    <div class="menu-card-box">
      <v-layout row wrap class="menu-card-cober-each-card">
        <v-flex
          xs12
          sm6
          md4
          lg3
          v-for="recipe in data"
          :key="recipe.recipe_id"
          class="menu-card-each-card"
        >
          <!-- Card -->

          <v-card
            :name="data[0]"
            :loading="loading"
            class="mx-auto"
            max-width="400"
            id="card-recipe"
          >
            <template slot="progress">
              <v-progress-linear
                color="deep-purple"
                height="10"
                indeterminate
              ></v-progress-linear>
            </template>

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
                <v-icon class="btn-fav-recipe-icon" @click="addFavoriteRecipe(recipe.recipe_id)"
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
                  value= 5,
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
              <v-btn
                block
                dark
                text
                link
                @click="ClickRecipe(recipe.recipe_id)"
                style="background-color: #ff7043"
              >
                <span>ทำอาหาร</span>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </div>

    <!-- Button All recipe -->

    <div class="wraper-btn-see-all-recipe">
      <v-btn large color="success" class="btn-see-all-recipe">
        <span class="all-recipe-text">สูตรอื่นๆ</span>
      </v-btn>
    </div>
  </div>
</template>

<script>
// import Pagination from "./Pagination.vue";
// import Searchrecipe from "./SearchRecipe.vue";
import axios from 'axios'

export default {
  name: 'Favorite',

  components: {},

  data: () => ({
    loading: false,
    selection: 1,
    menus: [
      {
        Name: 'Beef Welling Ton',
        Author: 'KhaoKrua',
        time: '2',
        rate: 1,
        src:
          'https://www.thedorsetmeatcompany.co.uk/theme-content/uploads/2020/08/Beef-Wellington_004.jpg',
      },
      {
        Name: 'ต้มยำกุ้ง',
        Author: 'KhaoKrua',
        time: '1',
        rate: 4.7,
        src:
          'https://d12man5gwydfvl.cloudfront.net/wp-content/uploads/2019/06/shutterstock_430308484.jpg',
        link: 'tomyum',
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
      {
        Name: 'ชาเขียวปั่น',
        Author: 'KhaoKrua',
        time: '1',
        rate: 4.7,
        src:
          'https://www.pholfoodmafia.com/wp-content/uploads/2019/03/Matcha-Frappe-big.jpg',
      },
      {
        Name: 'สปาเก็ตตี้',
        Author: 'KhaoKrua',
        time: '1',
        rate: 4.7,
        src:
          'https://i.pinimg.com/564x/ab/18/4b/ab184bd478b50aa6468b59b5d90c00e3.jpg',
      },
      {
        Name: 'แฮมเบอร์เกอร์',
        Author: 'KhaoKrua',
        time: '1',
        rate: 4.7,
        src: 'https://blogs.psychcentral.com/nlp/files/2013/09/overeating.jpg',
      },
    ],
    idDummy: [],
    count: 0,
    tags: [
      { tagName: 'เครื่องดื่ม' },
      { tagName: 'เมนูไข่' },
      { tagName: 'แฮมเบอร์เกอร์' },
      { tagName: 'ก๋วยเตี๋ยว' },
      { tagName: 'ผลไม้' },
      { tagName: 'เมนูชีส' },
      { tagName: 'ไอศครีม' },
      { tagName: 'คอกเทล' },
      { tagName: 'สเต้ก' },
      { tagName: 'นม' },
      { tagName: 'ของหวาน' },
    ],

    data: [],
  }),
  methods: {

    ClickRecipe(id){
      console.log(id)
      this.$router.push({path: 'recipe' , query: {rid: id}});
    },

    letCook() {

    },

    async getAllRecipeData() {
      console.log('geting recipe ...')
      this.$store.commit("SET_DIALOG_LOADING", true)
      await axios
        .get(
          'http://127.0.0.1:5000/api/recipe'
        )
        .then((res) => {
          this.data = res.data
          console.log('title',this.data.recipe_id) 
        })
        .catch((err) => {
          console.log(err)
        })
      this.$store.commit("SET_DIALOG_LOADING", false)
      console.log('finished get')
    },

    async addFavoriteRecipe(recipe_id) {
      this.$store.commit("SET_DIALOG_LOADING", true)
      await axios
        .post(
          'http://127.0.0.1:5000/api/addfavorite/' + recipe_id +'/' + this.$store.getters.getUserID
        )
        .then((res) => {
          console.log(res) 
        })
        .catch((err) => {
          console.log(err)
        })
      this.$store.commit("SET_DIALOG_LOADING", false)
    },




  },
  async mounted() {
    await this.getAllRecipeData()
  }
  
}
</script>

<style lang="scss" >
@import url('https://fonts.googleapis.com/css2?family=Kanit:wght@200&display=swap');

* {
  list-style: none;
  outline: none;
  font-family: 'Kanit', sans-serif;
  box-sizing: border-box;
}

.home-container {
  margin: 5px auto;
  width: 90%;
  position: relative;
}

.wraper-header-menu {
  margin-top: 60px;
  text-align: center;
}

.header-text{
  font-weight: bold;
  font-size: 34px;
}

.sheet-header-menu {
  border-radius: 10px 10px 0px 0px;
  padding: 50px;
  height: 100%;
  width: 500px;
}

.col-tag{
  padding: 200px;
}

.sheet-tag-menu {
  border-radius: 10px;
  height: 70%;
  width: 700px;
  position: relative;
  margin: 15px 90px 15px 0px;
  padding: 20px;
}

.chip-tag-group {
  margin-top: 10px;
}

.wraper-btn-see-all-recipe {
  height: 100px;
  padding: 50px;
  background-color: white;
  position: relative;
  border-radius: 0px 0px 10px 10px;
}

.wraper-btn-see-all-recipe .btn-see-all-recipe {
  position: absolute;
  left: 50%;
  right: 50%;
  transform: translate(-50%, -50%);
  width: 200px;
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
  &:hover {
    background: red;
    color: white;
    transform: scale(1.1);
  }
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
  padding: 20px;
  border-radius: 0px 10px 0px 0px;
}

.menu-card-box-2 {
  background-color: white;
  margin-top: 50px;
  margin-left: 20px;
  margin-right: 20px;
  padding: 20px;
  border-radius: 0px 10px 10px 10px;
}

.card-data .box-card-data {
  display: flex;
  justify-content: flex-start;
  margin: 10px auto;
}

@media only screen and (max-width: 1264px) {
  .sheet-tag-menu {
    height: 70%;
    width: 450px;
    position: relative;
    padding-top: 15px;
    padding-right: 30px;
    margin-right: 35px;
  }
  .sheet-header-menu {
    border-radius: 10px 10px 0px 0px;
    padding: 50px;
    height: 100%;
    width: 400px;
  }
}

@media only screen and (max-width: 960px) {
  .sheet-tag-menu {
    height: 70%;
    width: 350px;
    position: relative;
    margin: 30px 20px 15px 0px;
    padding-top: 30px;
  }
  .sheet-header-menu {
    border-radius: 10px 10px 0px 0px;
    padding: 50px;
    height: 100%;
    width: 300px;
  }
}

@media only screen and (max-width: 600px) {
  .sheet-tag-menu {
    height: 70%;
    width: 100%;
    position: relative;
    padding-top: 30px;
  }
  .sheet-header-menu {
    border-radius: 10px;
    padding: 30px;
    height: 100%;
    width: 100%;
  }
  .header-text{
    font-size: 28px;
  }
  .menu-card-box{
    border-radius: 10px 10px 0px 0px;
  }
}

</style>


