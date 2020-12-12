<template>
  <div class="recipe-container">
    <v-row no-gutters class="md-6">
      <v-sheet class="header-sheet-recipe-menu">
        <v-breadcrumbs class="recipe-breadcrumbs" large :items="breadcrumbs">
          <template v-slot:item="{ item }">
            <v-breadcrumbs-item :href="item.href" :disabled="item.disabled">
              {{ item.text.toUpperCase() }}
            </v-breadcrumbs-item>
          </template>
        </v-breadcrumbs>

        <h1 class="header-recipe-text">{{ DataRecipe.title }}</h1>

        <div class="recipe-header-info">
          <v-row>
            <v-col md="6">
              <div class="author-box">
                <v-card class="author-img" max-width="344" style="margin: 20px">
                  <v-img
                    lazy-src="DataRecipe."
                    max-height="150"
                    max-width="150"
                    :src="DataRecipe.profile_pic"
                  ></v-img>
                </v-card>
                <div class="auther-text">
                  <div class="menu-rating">
                    <v-rating
                      value="4.8"
                      color="amber"
                      dense
                      half-increments
                      readonly
                      size="14"
                    ></v-rating>

                    <div class="grey--text ml-4">(413)</div>
                  </div>

                  <h4 id="recipeBy">
                    สูตรโดย
                    <span
                      ><a class="author-link" href="#">{{
                        DataRecipe.profile_name
                      }}</a></span
                    >
                  </h4>
                </div>
              </div>
              <!-- End Author box -->
            </v-col>
            <v-col md="6">
              <v-sheet style="padding: 20px;"  >
                <span style="font-size: 20px">
                  {{DataRecipe.description}}
                </span>
              </v-sheet>
            </v-col>
          </v-row>
        </div>
      </v-sheet>
    </v-row>

    <v-row no-gutters class="md-6">
      <v-sheet class="content-sheet-recipe-menu">
        <div class="wrapper-recipe-card">
          <v-card class="recipe-card-img" max-width="400">
            <div class="recipe-img">
              <v-img :src="DataRecipe.photo_recipe"> </v-img>
            </div>
          </v-card>
        </div>
        <div class="wraper-addto-fav-icon">
          <v-btn
            class="addto-fav-icon"
            color="success"
            @click="addFavoriteRecipe"
            ><span><v-icon>favorite_border</v-icon></span>
            เพิ่มในเมนูโปรด</v-btn
          >
        </div>
      </v-sheet>
    </v-row>

    <v-row no-gutters class="md-6" id="wraper-data-recipe">
      <div class="recipe-share-area-res">
        <v-sheet class="sheet-recipe-share-area">
          <div class="share-button">
            <i class="fab fa-facebook"></i>
            <v-btn color="primary"><v-icon>fab fa-facebook</v-icon></v-btn>
          </div>
        </v-sheet>
      </div>

      <v-col class="col-ingredients">
        <div class="data-recipe">
          <v-sheet class="data-sheet-recipe-menu">
            <div class="data-time-recipe">
              <div class="data-prep-time">
                <span class="prep-time">เวลาเตรียม :</span>
                <span class="no-DataRecipe" href="#">{{
                  DataRecipe.prep_time
                }}</span>
              </div>
              <div class="data-cook-time">
                <span class="cook-time">เวลาทำอาหาร :</span>
                <span class="no-data" href="#">{{ DataRecipe.cook_time }}</span>
              </div>
            </div>
            <div class="data-serve-recipe">
              <div class="data-serve">
                <span class="serve-no">เสิร์ฟ :</span>
                <span class="no-data" href="#">{{ DataRecipe.serve }} ที่</span>
              </div>
              <div class="data-yield">
                <span class="yield-no">จำนวน :</span>
                <span class="no-data">{{ DataRecipe.yield }}</span>
              </div>
            </div>
          </v-sheet>
        </div>
        <div class="ingredient-recipe">
          <v-sheet class="ingredient-sheet-recipe-menu">
            <span class="ingredients-header-recipe">ส่วนผสม</span>
            <v-divider style="margin: 5px 0px 20px 0px"></v-divider>
            <v-sheet>
              <v-divider
                style="margin: 15px 0px 15px 0px; width: 100%"
              ></v-divider>
              <div style="display: flex; justify-content: space-between">
                <span>{{ DataRecipe.ingredients }}</span
                >n>
              </div>
            </v-sheet>
          </v-sheet>
        </div>
      </v-col>
      <v-col class="col-direction">
        <v-sheet class="direction-sheet-recipe-menu">
          <span class="direction-header-recipe">วิธีทำ</span>
          <v-divider style="margin: 5px 0px 20px 0px"></v-divider>
          <v-sheet>
            <v-divider
              style="margin: 15px 0px 15px 0px; width: 100%"
            ></v-divider>
            <span>{{ DataRecipe.steps }}</span>
          </v-sheet>
        </v-sheet>
      </v-col>
    </v-row>
    <v-dialog persistent v-model="success_add_fav" width="500">
      <v-card>
        <v-card-title color="#00E676"> แจ้งเตือน </v-card-title>
        <v-card-text class="textDetail">
          เพิ่มในเมนูโปรดเรียบร้อย
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="success_add_fav = !success_add_fav"
          >
            ตกลง
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <dialogPopup/>
  </div>
</template>

<script>
import axios from 'axios'
import dialogPopup from '../../components/Popup/DialogPopUp'

export default {
  name: 'recipe',

  data: () => ({
    success_add_fav: false,
    breadcrumbs: [
      {
        text: 'หน้าแรก',
        disabled: false,
        href: '/',
      },
      {
        text: 'เมนู',
        disabled: true,
        href: 'recipe',
      },
    ],
    DataRecipe: [],
  }),
  methods: {
    async addFavoriteRecipe() {
      this.$store.commit('SET_DIALOG_LOADING', true)
      await axios
        .post(
          'http://127.0.0.1:5000/api/addfavorite/' +
            this.DataRecipe.recipe_id +
            '/' +
            this.$store.getters.getUserID
        )
        .then((res) => {
          console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
      this.$store.commit('SET_DIALOG_LOADING', false)
      this.success_add_fav = true
    },
  },

  async mounted() {
    this.$store.commit('SET_DIALOG_LOADING', true)
    var rid = this.$route.query.rid
    var result = await axios
      .get('http://127.0.0.1:5000/api/recipe/' + rid)
      .then((res) => {
        console.log('Here', res.data[0])
        this.DataRecipe = res.data[0]
      })
    this.$store.commit('SET_DIALOG_LOADING', false)
  },
}
</script>

<style lang="scss" scoped>
.recipe-container {
  position: relative;
  justify-content: center;
  margin: 5px auto;
  width: 80%;
}

.header-sheet-recipe-menu {
  border-radius: 10px;
  width: 100%;
  padding: 20px;
}

.recipe-breadcrumbs {
  position: absolute;
  left: 0px;
  top: 0px;
}

.header-recipe-text {
  text-align: left;
  margin: 30px 10px;
  font-size: 9vh;
}

.recipe-header-info {
}

.author-box {
  margin: 30px auto;
  width: 30%;
  display: flex;
  position: relative;
}

.menu-rating {
  display: flex;
}

.auther-text {
  display: inline-block;
  margin: auto;
}

#recipeBy {
  display: inline-block;
  padding: 5px;
}

.author-link {
  text-decoration: none;
  color: red;
  font-weight: bold;
  transition: 0.25s ease-in-out;
  margin: 5px;
  &:hover {
    font-size: 20px;
  }
}

.content-sheet-recipe-menu {
  border-radius: 10px;
  width: 100%;
  padding: 20px;
  margin-top: 30px;
}

.recipe-share-area {
  max-width: 300px;
  width: 50%;
  background-color: #606060;
  background: linear-gradient(180deg, #606060 40%, hsla(0, 0%, 100%, 0) 0);
  background-position: 0;
  background-size: 1px 5px;
  background-repeat: repeat-y;
}

.share-button {
  margin: 40px;
}

.wrapper-recipe-card {
  margin: 20px auto;
  width: 70%;
  display: flex;
  justify-content: center;
}

.wraper-addto-fav-icon {
  display: flex;
  justify-content: center;
  width: 50%;
  margin: 20px auto;
}

#wraper-data-recipe {
  margin-top: 40px;
}

.data-recipe {
  display: flex;
  flex-direction: column;
}

.data-sheet-recipe-menu {
  width: 95%;
  border-radius: 10px;
  padding: 20px;
  height: 150px;
  margin-bottom: 30px;
  display: block;
}

.data-sheet-recipe-menu div > div {
  padding: 10px;
  & > .no-data {
    color: red;
  }
  & > span {
    font-weight: bold;
  }
}

.data-time-recipe {
  display: flex;
}

.data-prep-time {
  width: 50%;
  text-align: left;
  padding: 10px;
  border-right: 1px solid #606060;
  border-bottom: 1px solid #606060;
}

.data-cook-time {
  width: 50%;
  text-align: right;
  border-bottom: 1px solid #606060;

  // & .cook-time {
  //   font-weight: bold;
  // }
}

.data-serve {
  width: 50%;
  text-align: left;
  border-right: 1px solid #606060;
}

.data-yield {
  width: 50%;
  text-align: right;
}

.data-serve-recipe {
  display: flex;
}

.ingredient-sheet-recipe-menu {
  width: 100%;
  border-radius: 10px 0px 0px 10px;
  padding: 20px;
}

.ingredients-header-recipe {
  font-weight: bold;
  font-size: 26px;
}

.direction-sheet-recipe-menu {
  width: 100%;
  border-radius: 10px;
  padding: 20px;
}

#sheet-responsive {
  display: none;
}

.direction-header-recipe {
  font-weight: bold;
  font-size: 26px;
}

.sheet-recipe-share-area {
  width: 100%;
  border-radius: 10px;
  padding: 20px;
  height: auto;
  margin-bottom: 30px;
  display: block;
}

.recipe-share-area-res {
  display: none;
}

@media only screen and (max-width: 1264px) {
  .recipe-container {
    width: 90%;
  }
  .header-recipe-text {
    font-size: 6vh;
  }
  .author-box {
    width: 40%;
  }
}

@media only screen and (max-width: 768px) {
  .recipe-container {
    width: 90%;
  }
  .header-recipe-text {
    font-size: 5vh;
  }
  .author-box {
    width: 50%;
  }
}

@media only screen and (max-width: 600px) {
  .col-direction {
    display: none;
  }
  .recipe-card-img {
    width: 300px;
  }
  .ingredient-sheet-recipe-menu {
    border-radius: 10px;
  }
  #sheet-responsive {
    display: block;
    margin: 30px auto;
  }
  .data-sheet-recipe-menu {
    width: 100%;
    height: auto;
  }
  .header-recipe-text {
    margin: 40px 0px 20px 0px;
  }
  .author-box {
    width: 100%;
    margin: 10px auto;
  }
  .recipe-share-area {
    display: none;
  }
  .data-sheet-recipe-menu div > div {
    font-size: 12px;
  }
  .recipe-share-area-res {
    width: 100%;
    display: block;
  }
  // .sheet-recipe-share-area{
  //   margin-top: 0px;
  // }
}
</style>